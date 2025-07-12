#!/bin/bash
# Simple activation script for BlogCreator
echo "🚀 Activating BlogCreator environment..."

# Activate virtual environment
source venv/bin/activate

# Install missing packages if needed
echo "📦 Checking dependencies..."
pip install -q langchain>=0.1.0 openai>=1.0.0 anthropic>=0.15.0 python-dotenv>=1.0.0

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << EOF
# API Keys - Replace with your actual keys
OPENAI_API_KEY=your-openai-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here
EOF
    echo "✅ .env file created! Please add your API keys."
else
    echo "✅ .env file already exists"
fi

echo "🎯 Environment ready! You can now run:"
echo "   python run_refine_topic.py"
echo "   python Data/example_usage.py"
echo ""
echo "💡 To get API keys:"
echo "   OpenAI: https://platform.openai.com/api-keys"
echo "   Anthropic: https://console.anthropic.com/" 