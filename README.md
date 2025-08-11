# VB.NET to C# Translator

A web application that translates VB.NET code to C# using AI models.

## Features

- **VB.NET to C# Translation**: Convert VB.NET code to equivalent C# code
- **Web Interface**: Modern, responsive web UI built with Next.js
- **FastAPI Backend**: RESTful API with automatic documentation
- **AI-Powered**: Uses Hugging Face transformers for accurate translations

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/vb-to-csharp-translator.git
   cd vb-to-csharp-translator
   ```

2. **Set up the backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   # Copy and configure your .env file
   cp env.example .env
   # Edit .env with your Hugging Face API token and model name
   uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Set up the frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Production Deployment

This application is now deployed using:
- **Frontend**: GitHub Pages
- **Backend**: Vercel (with Hugging Face Inference API integration)
- **AI Model**: Hugging Face Inference API with fine-tuned model

For deployment instructions, see the individual component documentation in their respective directories.

## Project Structure

```
vb-to-csharp-translator/
├── backend/                 # Vercel serverless backend
│   ├── api/                # API functions
│   │   └── index.py        # Main API endpoint
│   ├── vercel.json         # Vercel configuration
│   ├── requirements.txt        # Python dependencies
│   └── env.example         # Environment variables template
├── frontend/               # Next.js frontend (GitHub Pages)
│   ├── app/                # Next.js app directory
│   ├── package.json        # Node.js dependencies
│   ├── next.config.js      # Next.js configuration
│   └── .github/workflows/  # GitHub Actions
│       └── deploy.yml      # GitHub Pages deployment
└── README.md              # Project documentation
```

## Development Commands

```bash
# Backend development
cd backend
pip install -r requirements.txt
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000

# Frontend development
cd frontend
npm install
npm run dev

# Build frontend for production
cd frontend
npm run build

# Check service status
curl http://localhost:8000/health  # Backend health check
curl http://localhost:3000         # Frontend check
```

## API Endpoints

- `GET /health` - Health check
- `POST /translate` - Translate VB.NET to C#
- `GET /docs` - API documentation (Swagger UI)

## Configuration

### Environment Variables

For local development, create a `.env` file in the `backend/` directory:

```bash
# Copy the example file
cp backend/env.example backend/.env

# Edit .env with your actual values:
HUGGINGFACE_API_TOKEN=your_api_key_here
    HUGGINGFACE_MODEL_NAME=HuggingFaceTB/SmolLM3-3B  # or another text generation model
  ```
  
  **Demo Model**: This application uses `HuggingFaceTB/SmolLM3-3B` for demonstration purposes.
  
  **For Production Use**: Consider fine-tuning your own specialized VB.NET ↔ C# translation model for better accuracy and performance. You can:
  - Fine-tune on a large dataset of VB.NET/C# code pairs
  - Use models like `microsoft/DialoGPT-medium` or `meta-llama/Llama-2-7b-chat-hf` as base models
  - Deploy your fine-tuned model to Hugging Face and update the `HUGGINGFACE_MODEL_NAME` environment variable
  
  For production deployment on Vercel, set these as environment variables in your Vercel project settings.

## Cost Optimization

### Free Tier Deployment
- **GitHub Pages**: Free hosting for frontend
- **Vercel**: Free tier includes 100GB-hours/month serverless functions
- **Hugging Face**: Free inference API calls (with limits)
- **Estimated cost**: $0 for moderate usage

### Production Scaling
For higher traffic, consider:
- **Vercel Pro**: $20/month for increased limits
- **Hugging Face Pro**: $9/month for increased API limits
- **Custom domain**: ~$10-15/year

## Monitoring

### Health Checks
- Backend: `https://your-vercel-app.vercel.app/health`
- Frontend: `https://your-username.github.io/vb-to-csharp-translator`

### Logs
- **Vercel**: View logs in Vercel dashboard
- **GitHub Pages**: Deployment logs in GitHub Actions
- **Local development**: Check terminal output

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   sudo lsof -i :3000  # Check what's using port 3000
   sudo lsof -i :8000  # Check what's using port 8000
   ```

2. **Hugging Face API errors**
   - Verify your API token is valid
   - Check if your model is accessible
   - Ensure you have sufficient API credits

3. **Vercel deployment fails**
   - Check Vercel logs in dashboard
   - Verify environment variables are set
   - Ensure requirements.txt is up to date

4. **GitHub Pages deployment fails**
   - Check GitHub Actions logs
   - Verify repository settings
   - Ensure Next.js build succeeds

### Performance Optimization

1. **Reduce API costs**
   - Implement request caching
   - Use model quantization
   - Optimize prompt length

2. **Improve response time**
   - Use Vercel's global CDN
   - Implement client-side caching
   - Optimize Hugging Face API calls

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Create an issue on GitHub
- **Documentation**: Check the `/docs` endpoint at `http://localhost:8000/docs` (local development)
- **API Reference**: Interactive API documentation available when running the application locally
