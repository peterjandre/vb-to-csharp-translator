# VB.NET ↔ C# Translator Backend

This is the backend API for the VB.NET to C# code translator, designed to be deployed on Vercel with Hugging Face Inference API integration.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   # Copy and configure your .env file
   cp env.example .env
   # Edit .env with your Hugging Face API token and model name
   ```

3. Start the development server:
   ```bash
   uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
   ```

4. Access the API:
   - API: http://localhost:8000
   - Health check: http://localhost:8000/health
   - API docs: http://localhost:8000/docs

## Deployment to Vercel

### Prerequisites

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Get your Hugging Face API token from https://huggingface.co/settings/tokens

3. Note your fine-tuned model name (format: `username/model-name`)

### Deployment Steps

1. **Login to Vercel**:
   ```bash
   vercel login
   ```

2. **Deploy the backend**:
   ```bash
   cd backend
   vercel
   ```

3. **Set environment variables**:
   ```bash
   vercel env add HUGGINGFACE_API_TOKEN
   vercel env add HUGGINGFACE_MODEL_NAME
   ```

4. **Deploy to production**:
   ```bash
   vercel --prod
   ```

### Environment Variables

Set these in your Vercel project settings:

- `HUGGINGFACE_API_TOKEN`: Your Hugging Face API token
- `HUGGINGFACE_MODEL_NAME`: Your fine-tuned model name (e.g., `your-username/your-model-name`)

### API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /translate` - Translate code between VB.NET and C#

### Example Usage

```bash
curl -X POST "https://your-vercel-app.vercel.app/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "Dim message As String = \"Hello World\"",
    "source_language": "vb",
    "target_language": "csharp"
  }'
```

## Configuration

The backend is configured for:
- Vercel serverless deployment
- Hugging Face Inference API integration
- CORS support for GitHub Pages frontend
- 30-second timeout for API calls

## Troubleshooting

1. **API token issues**: Ensure your Hugging Face API token is valid and has inference permissions
2. **Model not found**: Verify your model name is correct and the model is public or you have access
3. **Timeout errors**: The function has a 30-second timeout limit on Vercel
4. **CORS errors**: Ensure the frontend URL is in the allowed origins list
