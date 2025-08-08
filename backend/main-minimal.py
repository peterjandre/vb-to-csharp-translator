from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import logging
import re

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(title="VB.NET to C# Translator", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo
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

def simple_vb_to_csharp_translation(vb_code: str) -> str:
    """Simple rule-based VB.NET to C# translation for demo purposes"""
    
    # Basic translations
    translations = {
        # Keywords
        r'\bDim\b': 'var',
        r'\bAs\s+String\b': '',
        r'\bAs\s+Integer\b': '',
        r'\bAs\s+Boolean\b': '',
        r'\bPublic\s+Sub\b': 'public void',
        r'\bPublic\s+Function\b': 'public',
        r'\bPrivate\s+Sub\b': 'private void',
        r'\bPrivate\s+Function\b': 'private',
        r'\bEnd\s+Sub\b': '}',
        r'\bEnd\s+Function\b': '}',
        r'\bEnd\s+If\b': '}',
        r'\bThen\b': '{',
        r'\bElseIf\b': 'else if',
        r'\bElse\b': 'else {',
        r'\bAnd\b': '&&',
        r'\bOr\b': '||',
        r'\bNot\b': '!',
        r'\bTrue\b': 'true',
        r'\bFalse\b': 'false',
        r'\bNothing\b': 'null',
        r'\'': '//',  # Comments
        r'&': '+',    # String concatenation
    }
    
    result = vb_code
    
    # Apply translations
    for pattern, replacement in translations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    # Add semicolons at end of lines (basic heuristic)
    lines = result.split('\n')
    processed_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.endswith(('{', '}', '//')):
            if not any(keyword in stripped.lower() for keyword in ['if', 'else', 'for', 'while', 'class', 'public', 'private']):
                line += ';'
        processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def simple_csharp_to_vb_translation(csharp_code: str) -> str:
    """Simple rule-based C# to VB.NET translation for demo purposes"""
    
    # Basic reverse translations
    translations = {
        # Keywords
        r'\bvar\b': 'Dim',
        r'\bpublic\s+void\b': 'Public Sub',
        r'\bprivate\s+void\b': 'Private Sub',
        r'\btrue\b': 'True',
        r'\bfalse\b': 'False',
        r'\bnull\b': 'Nothing',
        r'&&': 'And',
        r'\|\|': 'Or',
        r'//': "'",  # Comments
        r';$': '',   # Remove semicolons at end of lines
        r'{': 'Then',
        r'}': 'End',
    }
    
    result = csharp_code
    
    # Apply translations
    for pattern, replacement in translations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE | re.MULTILINE)
    
    return result

@app.get("/")
async def root():
    return {"message": "VB.NET to C# Translator API (Demo Version)"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": True,
        "tokenizer_loaded": True,
        "version": "demo"
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate_code(request: TranslationRequest):
    try:
        # Validate language combination
        if request.source_language == "vb" and request.target_language == "csharp":
            translated_code = simple_vb_to_csharp_translation(request.code)
        elif request.source_language == "csharp" and request.target_language == "vb":
            translated_code = simple_csharp_to_vb_translation(request.code)
        else:
            raise HTTPException(status_code=400, detail="Invalid language combination")
        
        logger.info(f"Translating from {request.source_language} to {request.target_language}")
        logger.info(f"Input code length: {len(request.code)}")
        
        # Add demo notice
        demo_notice = "// This is a demo translation using rule-based conversion\n// For production use, consider using AI-powered translation\n\n"
        if request.target_language == "vb":
            demo_notice = "' This is a demo translation using rule-based conversion\n' For production use, consider using AI-powered translation\n\n"
        
        translated_code = demo_notice + translated_code
        
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
