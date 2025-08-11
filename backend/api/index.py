from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import logging
import requests
import json
from typing import Optional
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="VB.NET to C# Translator", version="1.0.0")

# Configure CORS for GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://peterjandre.github.io",  # GitHub Pages
        "https://*.github.io",  # Any GitHub Pages site
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    code: str
    source_language: str  # "vb" or "csharp"
    target_language: str  # "csharp" or "vb"

class TranslationResponse(BaseModel):
    translated_code: str
    source_language: str
    target_language: str

def call_huggingface_inference_api(prompt: str, model_name: str) -> str:
    """Call Hugging Face Router API for chat completions"""
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not api_token:
        raise Exception("HUGGINGFACE_API_TOKEN environment variable not set")
    
    return call_router_api(prompt, model_name, api_token)

def call_router_api(prompt: str, model_name: str, api_token: str) -> str:
    """Call Hugging Face Router API using the working approach from test"""
    try:
        API_URL = "https://router.huggingface.co/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_token}",
        }

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a VB.NET to C# code converter. Output ONLY the C# code equivalent. No explanations, no thinking, just the code. Example: VB.NET 'Dim x As String' becomes C# 'string x;'"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": f"{model_name}:hf-inference",
            "max_tokens": 200,
            "temperature": 0.1,
            "top_p": 0.9,
            "do_sample": True
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code != 200:
            logger.error(f"Router API error: {response.status_code} - {response.text}")
            raise Exception(f"Router API error: {response.status_code}")
        
        result = response.json()
        logger.info(f"Router API response: {result}")
        
        content = result["choices"][0]["message"]["content"].strip()
        
        # Remove <think> tags and their content if they appear
        import re
        
        # Remove complete <think>...</think> blocks
        content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL)
        
        # Remove <think> tags that aren't closed (common with this model)
        content = re.sub(r'<think>.*', '', content, flags=re.DOTALL)
        
        # Clean up any remaining whitespace and newlines
        content = re.sub(r'\n\s*\n', '\n', content)  # Remove extra blank lines
        content = content.strip()
        
        # If we still have no content after removing think tags, try a different approach
        if not content:
            # Extract just the code part if it exists after the thinking
            code_match = re.search(r'</think>\s*(.*)', result["choices"][0]["message"]["content"], flags=re.DOTALL)
            if code_match:
                content = code_match.group(1).strip()
        
        return content
        
    except requests.exceptions.Timeout:
        raise Exception("Router API request timed out")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Router API request failed: {str(e)}")
    except Exception as e:
        logger.error(f"Router API error: {str(e)}")
        raise Exception(f"Router API failed: {str(e)}")

def generate_translation(prompt: str) -> str:
    """Generate translation using Hugging Face Inference API"""
    # Use your fine-tuned model name here
    model_name = os.getenv("HUGGINGFACE_MODEL_NAME", "your-username/your-model-name")
    
    try:
        translated_text = call_huggingface_inference_api(prompt, model_name)
        return translated_text.strip()
        
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        raise Exception(f"Failed to generate translation: {str(e)}")

@app.get("/")
async def root():
    return {"message": "VB.NET to C# Translator API (Vercel)"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    model_name = os.getenv("HUGGINGFACE_MODEL_NAME")
    
    return {
        "status": "healthy",
        "api_token_configured": api_token is not None,
        "model_name_configured": model_name is not None,
        "deployment": "vercel"
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate_code(request: TranslationRequest):
    try:
        # Validate language combination
        if request.source_language == "vb" and request.target_language == "csharp":
            prompt = f"Translate this VB.NET code to C#:\n\n{request.code}"
        elif request.source_language == "csharp" and request.target_language == "vb":
            prompt = f"Translate this C# code to VB.NET:\n\n{request.code}"
        else:
            raise HTTPException(status_code=400, detail="Invalid language combination")
        
        logger.info(f"Translating from {request.source_language} to {request.target_language}")
        logger.info(f"Input code length: {len(request.code)}")
        
        # Generate translation
        translated_code = generate_translation(prompt)
        
        logger.info(f"Translation completed. Output length: {len(translated_code)}")
        
        return TranslationResponse(
            translated_code=translated_code,
            source_language=request.source_language,
            target_language=request.target_language
        )
        
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")


