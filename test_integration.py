#!/usr/bin/env python3
"""
Simple integration test to verify all components are working with real APIs
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import (
    OpenAIModel,
    AnthropicModel,
    PromptTemplate,
    StringOutputParser,
    LLMChain,
)

# Load environment variables from .env file
load_dotenv()


def test_openai_integration():
    """Test OpenAI model integration"""
    print("🔍 Testing OpenAI Integration...")
    try:
        model = OpenAIModel(model_name="gpt-3.5-turbo")
        prompt = PromptTemplate(
            template="Say hello in {language}", input_variables=["language"]
        )
        chain = LLMChain(llm=model, prompt=prompt)
        result = chain.predict(language="Spanish")
        print(f"✅ OpenAI Result: {result}")
        return True
    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return False


def test_anthropic_integration():
    """Test Anthropic model integration"""
    print("🔍 Testing Anthropic Integration...")
    try:
        model = AnthropicModel(model_name="claude-3-sonnet-20240229")
        prompt = PromptTemplate(
            template="Say hello in {language}", input_variables=["language"]
        )
        chain = LLMChain(llm=model, prompt=prompt)
        result = chain.predict(language="French")
        print(f"✅ Anthropic Result: {result}")
        return True
    except Exception as e:
        print(f"❌ Anthropic Error: {e}")
        return False


def test_api_keys():
    """Test API key configuration"""
    print("🔍 Testing API Key Configuration...")
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if openai_key and openai_key != "your-openai-api-key-here":
        print("✅ OpenAI API key is configured")
    else:
        print("❌ OpenAI API key is not configured")
        return False

    if anthropic_key and anthropic_key != "your-anthropic-api-key-here":
        print("✅ Anthropic API key is configured")
    else:
        print("❌ Anthropic API key is not configured")
        return False

    return True


def main():
    """Run all integration tests"""
    print("🧪 LangChain Simple Integration Test")
    print("=" * 50)

    # Test API key configuration
    if not test_api_keys():
        print("\n❌ API keys not configured. Please set up your .env file.")
        return

    print()

    # Test OpenAI integration
    openai_success = test_openai_integration()
    print()

    # Test Anthropic integration
    anthropic_success = test_anthropic_integration()
    print()

    # Summary
    print("📋 Test Summary:")
    print(f"OpenAI Integration: {'✅ PASS' if openai_success else '❌ FAIL'}")
    print(f"Anthropic Integration: {'✅ PASS' if anthropic_success else '❌ FAIL'}")

    if openai_success and anthropic_success:
        print("\n🎉 All tests passed! Your system is ready to go!")
    else:
        print(
            "\n⚠️  Some tests failed. Please check your API keys and internet connection."
        )


if __name__ == "__main__":
    main()
