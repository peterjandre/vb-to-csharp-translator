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

2. **Set up the development environment**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Start the application**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Production Deployment

This application is designed to run on containerized environments. The repository includes:
- Docker configuration for both frontend and backend
- GitHub Actions workflow for automated deployment
- Health checks and monitoring capabilities

For deployment instructions, please refer to your chosen hosting platform's documentation.

## Project Structure

```
vb-to-csharp-translator/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application
│   ├── main-minimal.py     # Lightweight version for resource-constrained environments
│   ├── requirements.txt    # Full Python dependencies
│   ├── requirements-minimal.txt # Minimal dependencies
│   └── Dockerfile         # Backend container
├── frontend/               # Next.js frontend
│   ├── app/               # Next.js app directory
│   ├── package.json       # Node.js dependencies
│   └── Dockerfile         # Frontend container
├── .github/workflows/     # GitHub Actions
│   └── deploy.yml         # CI/CD pipeline
├── docker-compose.yml     # Container orchestration
├── setup.sh              # Local development setup
└── README.md             # Project documentation
```

## Development Commands

```bash
# Set up development environment
chmod +x setup.sh
./setup.sh

# Start with Docker
docker-compose up --build

# Stop Docker containers
docker-compose down

# View logs
docker-compose logs -f

# Clean up
docker-compose down -v
docker system prune -f

# Install dependencies manually
cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
cd frontend && npm install

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

Create a `.env` file in the `backend/` directory:

```env
# Hugging Face API (optional, for private models)
HUGGINGFACE_API_KEY=your_api_key_here

# Model configuration
MODEL_NAME=microsoft/DialoGPT-medium
```

## Cost Optimization

### Free Tier Deployment
- **EC2 t3.micro**: Free for 12 months (750 hours/month)
- **Estimated cost**: $0 after free tier
- **Performance**: Suitable for development and small-scale usage

### Production Scaling
For higher traffic, consider:
- **EC2 t3.small**: ~$8.50/month
- **Load Balancer**: ~$16/month
- **Auto Scaling**: Based on demand

## Monitoring

### Health Checks
- Backend: `http://your-domain:8000/health`
- Frontend: `http://your-domain:3000`

### Logs
```bash
# View application logs
docker-compose logs -f

# View individual service logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   sudo lsof -i :3000  # Check what's using port 3000
   docker-compose down  # Stop containers
   ```

2. **Docker permission denied**
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Application not accessible**
   - Check if containers are running: `docker-compose ps`
   - Verify ports are not blocked by firewall

4. **Deployment fails**
   ```bash
   # Check logs
   docker-compose logs
   
   # Restart services
   docker-compose restart
   ```

### Performance Optimization

1. **Reduce memory usage**
   - Use smaller models
   - Enable model caching
   - Optimize Docker images

2. **Improve response time**
   - Use model quantization
   - Implement request caching
   - Consider CDN for static assets

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
- **Documentation**: Check the `/docs` endpoint at `http://localhost:8000/docs`
- **API Reference**: Interactive API documentation available when running the application
