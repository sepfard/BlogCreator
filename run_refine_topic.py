#!/usr/bin/env python3
"""
Runner script for the RefineTopicChain - the first step in the BlogCreator pipeline.
This script sets up the chain manager, configures the refine topic chain, and executes it with sample inputs.
Now uses the updated Anthropic-focused implementation with langchain integration.

For the complete workflow including research source generation, use run_full_pipeline.py instead.
"""

import os
import sys
from typing import Dict, Any

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

from app.chains.chain_manager import ChainManager


def main():
    """Main function to run the refine topic chain."""

    # Configuration - Now using Anthropic exclusively
    model_name = "claude-3-5-sonnet-20241022"  # Latest Claude model
    verbose = True  # Enable verbose logging to see prompts

    print("=== BlogCreator: Refine Topic Chain Runner ===\n")
    print("🚀 Using Anthropic's Claude with langchain integration\n")

    # Initialize the chain manager
    manager = ChainManager()

    # Set up the refine topic chain
    print(f"Setting up refine topic chain with {model_name}...")
    try:
        refine_chain = manager.setup_refine_topic_chain(
            model_name=model_name, verbose=verbose
        )
        print("✓ Chain setup complete\n")
    except Exception as e:
        print(f"❌ Error setting up chain: {e}")
        if "API key" in str(e) or "authentication" in str(e):
            print("\n🔑 API Key Setup Required:")
            print("   Please set up your Anthropic API key before running the script.")
            print("   See README.md for detailed instructions.")
            print("\n   Quick setup - Create a .env file with:")
            print("   ANTHROPIC_API_KEY=your_key_here")
            print("\n   Get your API key from: https://console.anthropic.com/")
        return

    # Define inputs for the refine topic chain
    inputs = {
        "topic": "real estate lead generation strategies",
        "keywords": [
            "CRM",
            "property outreach",
            "sales automation",
            "lead qualification",
            "prospecting",
        ],
    }

    print("Input parameters:")
    print(f"  Topic: {inputs['topic']}")
    print(f"  Keywords: {inputs['keywords']}")
    print("\n" + "=" * 50)
    print("Running refine topic chain...")
    print("=" * 50 + "\n")

    # Run the chain
    try:
        result = manager.run_chain("refine_topic", inputs, as_json=True)

        print("✓ Chain execution completed successfully!\n")
        print("--- Refined Topic Output ---")
        print(result)

    except Exception as e:
        print(f"❌ Error running chain: {e}")
        if "authentication" in str(e) or "invalid x-api-key" in str(e):
            print("\n💡 This appears to be an API key issue.")
            print(
                "Please ensure your ANTHROPIC_API_KEY is set correctly in your .env file."
            )
        return

    print("\n" + "=" * 50)
    print("Chain execution completed!")
    print("=" * 50)
    print("\n💡 Want to see the complete workflow?")
    print("   Run: python run_full_pipeline.py")
    print("   This will chain topic refinement → research source generation")


if __name__ == "__main__":
    main()
