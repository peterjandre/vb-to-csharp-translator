from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import logging
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(title="VB.NET to C# Translator", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for model and tokenizer
model = None
tokenizer = None

class TranslationRequest(BaseModel):
    code: str
    source_language: str  # "vb" or "csharp"
    target_language: str  # "csharp" or "vb"

class TranslationResponse(BaseModel):
    translated_code: str
    source_language: str
    target_language: str

def load_model():
    """Load the model and tokenizer from Hugging Face Hub"""
    global model, tokenizer
    
    model_name = os.getenv("MODEL_NAME", "Helsinki-NLP/opus-mt-en-fr")
    logger.info(f"Loading model: {model_name}")
    
    try:
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            
        logger.info("Model and tokenizer loaded successfully")
        
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise Exception(f"Failed to load model: {str(e)}")

def generate_translation(prompt: str, max_length: int = 2048) -> str:
    """Generate translation using the loaded model"""
    global model, tokenizer
    
    if model is None or tokenizer is None:
        raise Exception("Model not loaded")
    
    try:
        # Tokenize the input
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        
        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                inputs["input_ids"],
                max_length=max_length,
                temperature=0.1,
                do_sample=True,
                num_return_sequences=1
            )
        
        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return generated_text
        
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        raise Exception(f"Failed to generate translation: {str(e)}")

@app.on_event("startup")
async def startup_event():
    """Load the model when the application starts"""
    load_model()

@app.get("/")
async def root():
    return {"message": "VB.NET to C# Translator API"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "tokenizer_loaded": tokenizer is not None
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 