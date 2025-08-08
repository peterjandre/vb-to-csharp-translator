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
   make setup
   ```

3. **Start the application**
   ```bash
   make docker-up
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Free Tier AWS Deployment

Deploy to AWS EC2 using the free tier (t3.micro instance):

#### Option 1: Automated Setup (Recommended)

1. **Install AWS CLI and configure credentials**
   ```bash
   aws configure
   ```

2. **Run the AWS setup script**
   ```bash
   chmod +x scripts/aws-setup.sh
   ./scripts/aws-setup.sh
   ```

3. **SSH into your EC2 instance**
   ```bash
   ssh -i vb-to-csharp-key.pem ubuntu@YOUR_PUBLIC_IP
   ```

4. **Set up the EC2 instance**
   ```bash
   chmod +x scripts/setup-ec2.sh
   ./scripts/setup-ec2.sh
   ```

5. **Configure GitHub Secrets**
   Go to your GitHub repository → Settings → Secrets and variables → Actions, and add:
   - `EC2_HOST`: Your EC2 public IP
   - `EC2_USERNAME`: `ubuntu`
   - `EC2_SSH_KEY`: Content of your `vb-to-csharp-key.pem` file

6. **Deploy**
   Push to the `main` branch to trigger automatic deployment.

#### Option 2: Manual Setup

1. **Launch EC2 instance**
   - Instance type: `t3.micro` (free tier eligible)
   - OS: Ubuntu 22.04 LTS
   - Security group: Allow ports 22, 80, 443, 3000, 8000

2. **SSH into the instance and run setup**
   ```bash
   ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
   chmod +x scripts/setup-ec2.sh
   ./scripts/setup-ec2.sh
   ```

3. **Clone your repository**
   ```bash
   cd /home/ubuntu
   git clone https://github.com/your-username/vb-to-csharp-translator.git
   cd vb-to-csharp-translator
   ```

4. **Deploy manually**
   ```bash
   chmod +x scripts/deploy-ec2.sh
   ./scripts/deploy-ec2.sh
   ```

## Project Structure

```
vb-to-csharp-translator/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend container
├── frontend/               # Next.js frontend
│   ├── app/               # Next.js app directory
│   ├── package.json       # Node.js dependencies
│   └── Dockerfile         # Frontend container
├── scripts/               # Deployment scripts
│   ├── aws-setup.sh      # AWS infrastructure setup
│   ├── setup-ec2.sh      # EC2 instance setup
│   └── deploy-ec2.sh     # Deployment script
├── .github/workflows/     # GitHub Actions
│   └── deploy.yml         # CI/CD pipeline
├── docker-compose.yml     # Local development
└── Makefile              # Development commands
```

## Development Commands

```bash
# Set up development environment
make setup

# Start with Docker
make docker-up

# Stop Docker containers
make docker-down

# View logs
make docker-logs

# Clean up
make clean

# Install dependencies
make install-deps

# Check service status
make status
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

# View EC2 monitoring logs
tail -f /home/ubuntu/monitor.log
```

### Backup and Recovery
- Automatic backups created before each deployment
- Manual backup: `tar -czf backup.tar.gz /home/ubuntu/vb-to-csharp-translator`
- Restore: `tar -xzf backup.tar.gz`

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

3. **EC2 instance not accessible**
   - Check security group rules
   - Verify key pair permissions: `chmod 400 your-key.pem`

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
- **Documentation**: Check the `/docs` endpoint
- **Deployment**: Follow the free tier setup guide above 
# Deployment Test
