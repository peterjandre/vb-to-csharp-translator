#!/bin/bash

echo "🧹 Setting up clean VB.NET to C# Translator environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found"

# Create clean virtual environment
echo "📦 Creating clean virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
cd backend
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp env.example .env
    echo "📝 Created .env file. Please edit it with your Hugging Face API credentials."
fi

cd ..

echo ""
echo "✅ Clean setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit backend/.env with your Hugging Face API token and model name"
echo "2. Activate the environment: source .venv/bin/activate"
echo "3. Start the backend: cd backend && uvicorn api.index:app --reload --host 0.0.0.0 --port 8000"
echo "4. Start the frontend: cd frontend && npm run dev"
echo "5. Test the setup: python3 test_setup.py"
echo ""
echo "🎉 Happy coding!"
