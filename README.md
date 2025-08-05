# VB.NET to C# Translator

A web application that translates code between VB.NET and C# using a fine-tuned Hugging Face model. Built with FastAPI backend, Next.js frontend, and Docker for easy deployment.

## Features

- Translate VB.NET code to C#
- Translate C# code to VB.NET
- Modern, responsive UI with Tailwind CSS
- Local model inference using transformers
- Copy translated code to clipboard
- Swap translation direction easily
- Docker-based deployment for easy setup

## Project Structure

```
vb-to-csharp-translator/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main FastAPI application
│   ├── Dockerfile          # Backend Docker configuration
│   ├── .dockerignore       # Docker ignore file
│   ├── requirements.txt    # Backend Python dependencies
│   └── env.example         # Environment variables template
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js app directory
│   ├── Dockerfile          # Frontend Docker configuration
│   ├── .dockerignore       # Docker ignore file
│   ├── package.json        # Frontend dependencies
│   └── ...                 # Other Next.js files
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # This file
```

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vb-to-csharp-translator
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build and start the FastAPI backend on `http://localhost:8000`
   - Build and start the Next.js frontend on `http://localhost:3000`
   - Download and cache the model locally (first run may take several minutes)

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Stopping the Application

```bash
docker-compose down
```

## Manual Setup (Alternative)

### Prerequisites

- Python 3.11+
- Node.js 18+
- Git

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and configure your model:
   ```
   MODEL_NAME=Helsinki-NLP/opus-mt-en-fr
   ```

5. Start the backend server:
   ```bash
   python main.py
   ```
   
   The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   
   The frontend will run on `http://localhost:3000`

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Choose the translation direction (VB.NET → C# or C# → VB.NET)
3. Enter your code in the input textarea
4. Click "Translate" to get the translated code
5. Use the "Copy to Clipboard" button to copy the translated code
6. Use the "Swap" button to switch the input and output

## API Endpoints

### GET /health

Health check endpoint to verify the service is running and the model is loaded.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "tokenizer_loaded": true
}
```

### POST /translate

Translates code between VB.NET and C#.

**Request Body:**
```json
{
  "code": "string",
  "source_language": "vb" | "csharp",
  "target_language": "csharp" | "vb"
}
```

**Response:**
```json
{
  "translated_code": "string",
  "source_language": "string",
  "target_language": "string"
}
```

## Configuration

### Model Configuration

The application uses the Hugging Face transformers library to load models locally. You can configure the model by setting the `MODEL_NAME` environment variable:

```bash
MODEL_NAME=Helsinki-NLP/opus-mt-en-fr
```

### Model Requirements

The model should be:
- A causal language model (like GPT-style models)
- Fine-tuned for code translation between VB.NET and C#
- Available on Hugging Face Hub

### Performance Considerations

- First startup may take several minutes to download the model
- Model is cached locally for subsequent runs
- GPU acceleration is automatically used if available
- Memory usage depends on model size

## Development

### Backend Development

- The FastAPI backend includes CORS configuration for local development
- API documentation is available at `http://localhost:8000/docs`
- Model is loaded once at startup and reused for all requests
- Includes comprehensive error handling and logging

### Frontend Development

- Built with Next.js 14 and TypeScript
- Uses Tailwind CSS for styling
- Responsive design that works on desktop and mobile
- Real-time error handling and loading states

### Docker Development

For development with Docker:

```bash
# Start services in development mode
docker-compose up --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up --build --force-recreate
```

## Deployment

### Environment Variables for Production

Set these environment variables in your Railway project:

- `MODEL_NAME`: The Hugging Face model to use
- `HOST`: Server host (usually 0.0.0.0)
- `PORT`: Server port (Railway will set this)

## Troubleshooting

1. **Model Download Issues**: Check your internet connection and ensure the model name is correct
2. **Memory Issues**: Use a smaller model or increase your system's available memory
3. **CORS Errors**: Ensure the backend is running on port 8000 and the frontend is running on port 3000
4. **Translation Errors**: Verify your model is properly fine-tuned for code translation

## License

This project is open source and available under the MIT License. 