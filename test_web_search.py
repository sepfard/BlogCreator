#!/usr/bin/env python3
"""
Test script to verify web search functionality in ResearchSourceChain
"""
import json
from app.chains.research_source_chain import ResearchSourceChain


def test_web_search_research():
    """Test the ResearchSourceChain with web search enabled"""

    # Create chain with web search enabled
    chain = ResearchSourceChain(verbose=True, enable_web_search=True)

    # Test inputs
    inputs = {
        "refined_topic": "AI-powered content generation and its impact on digital marketing strategies in 2024",
        "keywords": "AI content generation, digital marketing, automation, personalization, SEO, content strategy",
    }

    print("Testing ResearchSourceChain with web search enabled...")
    print(f"Topic: {inputs['refined_topic']}")
    print(f"Keywords: {inputs['keywords']}")
    print("-" * 80)

    try:
        # Run the chain
        result = chain.run(inputs)

        print("Research sources generated successfully!")
        print(json.dumps(result, indent=2, ensure_ascii=False))

        # Verify the result structure
        if isinstance(result, dict):
            required_keys = [
                "research_sources",
                "research_strategy",
                "priority_sources",
            ]
            missing_keys = [key for key in required_keys if key not in result]

            if missing_keys:
                print(f"Warning: Missing keys in result: {missing_keys}")
            else:
                print("✓ All required keys present in result")

            # Check for web search specific additions
            if "search_queries" in result:
                print("✓ Search queries included (web search feature working)")
            else:
                print("⚠ Search queries not found in result")

        return True

    except Exception as e:
        print(f"Error during test: {str(e)}")
        return False


def test_without_web_search():
    """Test the ResearchSourceChain without web search for comparison"""

    # Create chain without web search
    chain = ResearchSourceChain(verbose=True, enable_web_search=False)

    # Test inputs
    inputs = {
        "refined_topic": "Traditional content marketing approaches for small businesses",
        "keywords": "content marketing, small business, traditional methods, blog writing, social media",
    }

    print("\nTesting ResearchSourceChain without web search...")
    print(f"Topic: {inputs['refined_topic']}")
    print(f"Keywords: {inputs['keywords']}")
    print("-" * 80)

    try:
        # Run the chain
        result = chain.run(inputs)

        print("Research sources generated successfully (no web search)!")
        print(json.dumps(result, indent=2, ensure_ascii=False))

        return True

    except Exception as e:
        print(f"Error during test: {str(e)}")
        return False


if __name__ == "__main__":
    print("=" * 80)
    print("Web Search Integration Test")
    print("=" * 80)

    # Test with web search
    success1 = test_web_search_research()

    # Test without web search
    success2 = test_without_web_search()

    print("\n" + "=" * 80)
    print("Test Results:")
    print(f"Web search enabled: {'✓ PASS' if success1 else '✗ FAIL'}")
    print(f"Web search disabled: {'✓ PASS' if success2 else '✗ FAIL'}")
    print("=" * 80)
