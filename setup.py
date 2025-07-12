#!/usr/bin/env python3
"""
Setup script for LangChain Simple implementation
"""

import os
import subprocess
import sys


def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True


def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    env_example = """# OpenAI API Key
OPENAI_API_KEY=your-openai-api-key-here

# Anthropic API Key
ANTHROPIC_API_KEY=your-anthropic-api-key-here
"""

    if not os.path.exists(env_file):
        print("📝 Creating .env file...")
        with open(env_file, "w") as f:
            f.write(env_example)
        print("✅ .env file created!")
        print("🔑 Please edit .env and add your actual API keys")
    else:
        print("⚠️  .env file already exists")

    return True


def check_api_keys():
    """Check if API keys are set"""
    from dotenv import load_dotenv

    load_dotenv()

    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if not openai_key or openai_key == "your-openai-api-key-here":
        print("⚠️  OpenAI API key not set or using placeholder")
    else:
        print("✅ OpenAI API key is set")

    if not anthropic_key or anthropic_key == "your-anthropic-api-key-here":
        print("⚠️  Anthropic API key not set or using placeholder")
    else:
        print("✅ Anthropic API key is set")


def main():
    """Main setup function"""
    print("🚀 LangChain Simple Setup")
    print("=" * 50)

    # Step 1: Install requirements
    if not install_requirements():
        sys.exit(1)

    # Step 2: Create .env file
    create_env_file()

    # Step 3: Check API keys
    print("\n🔍 Checking API keys...")
    check_api_keys()

    print("\n📋 Setup Summary:")
    print("1. ✅ Requirements installed")
    print("2. ✅ .env file created (if needed)")
    print("3. 🔑 Edit .env with your actual API keys")
    print("4. 🎯 Run: python Data/example_usage.py")

    print("\n🔗 Get API Keys:")
    print("• OpenAI: https://platform.openai.com/api-keys")
    print("• Anthropic: https://console.anthropic.com/")


if __name__ == "__main__":
    main()
