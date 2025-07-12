#!/usr/bin/env python3
"""
Demo script showcasing web search functionality in BlogCreator.
This script demonstrates how to use the ResearchSourceChain with web search enabled.
"""

import os
import sys
import json
from typing import Dict, Any

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

from app.chains.chain_manager import ChainManager
from app.chains.research_source_chain import ResearchSourceChain


def demo_web_search_integration():
    """Demonstrate web search integration with ResearchSourceChain."""

    print("=" * 80)
    print("🔍 BlogCreator Web Search Integration Demo")
    print("=" * 80)

    # Demo topic: something current that would benefit from web search
    demo_inputs = {
        "refined_topic": "AI Content Creation Tools and Their Impact on Content Marketing ROI in 2024",
        "keywords": "AI content creation, marketing ROI, automation tools, content strategy, GPT, Claude, content optimization",
    }

    print(f"📝 Demo Topic: {demo_inputs['refined_topic']}")
    print(f"🔑 Keywords: {demo_inputs['keywords']}")
    print("\n" + "=" * 80)

    # Demo 1: Direct ResearchSourceChain with web search
    print("DEMO 1: Direct ResearchSourceChain with Web Search")
    print("=" * 80)

    try:
        # Create chain with web search enabled
        research_chain = ResearchSourceChain(verbose=True, enable_web_search=True)
        result = research_chain.run(demo_inputs)

        print("✅ Web search enabled research completed!")
        print("\nKey findings:")

        if isinstance(result, dict):
            # Show search queries if available
            if "search_queries" in result:
                print("\n🔍 Search queries that would be executed:")
                for i, query in enumerate(result["search_queries"], 1):
                    print(f"  {i}. {query}")

            # Show priority sources
            if "priority_sources" in result:
                print("\n📈 Priority sources identified:")
                for i, source in enumerate(result["priority_sources"], 1):
                    print(f"  {i}. {source}")

            # Show research strategy
            if "research_strategy" in result:
                print(f"\n📋 Research strategy: {result['research_strategy']}")

        print("\n" + "=" * 80)

    except Exception as e:
        print(f"❌ Error in Demo 1: {e}")
        return False

    # Demo 2: Using ChainManager with web search
    print("DEMO 2: ChainManager with Web Search Pipeline")
    print("=" * 80)

    try:
        manager = ChainManager()

        # Set up research chain with web search
        manager.setup_research_source_chain(
            model_name="claude-sonnet-4-20250514",
            verbose=True,
            enable_web_search=True,
        )

        # Run the research source chain
        result = manager.run_chain("research_sources", demo_inputs, as_json=False)

        print("✅ ChainManager web search research completed!")

        # Save results for inspection
        output_file = "Data/web_search_demo_output.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"📁 Results saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error in Demo 2: {e}")
        return False

    # Demo 3: Comparison with web search disabled
    print("\n" + "=" * 80)
    print("DEMO 3: Comparison - Web Search Disabled")
    print("=" * 80)

    try:
        # Create chain without web search
        research_chain_no_web = ResearchSourceChain(
            verbose=True, enable_web_search=False
        )
        result_no_web = research_chain_no_web.run(demo_inputs)

        print("✅ Traditional research (no web search) completed!")

        # Compare results
        print("\n📊 Comparison Summary:")
        print(
            f"  Web search enabled: {'search_queries' in result if isinstance(result, dict) else 'Unknown'}"
        )
        print(
            f"  Traditional approach: {'search_queries' in result_no_web if isinstance(result_no_web, dict) else 'Unknown'}"
        )

        # Save comparison results
        comparison_output = "Data/web_search_comparison.json"
        comparison_data = {
            "web_search_enabled": result,
            "web_search_disabled": result_no_web,
            "comparison_notes": "Web search enabled version should include search_queries and more current source recommendations",
        }

        with open(comparison_output, "w") as f:
            json.dump(comparison_data, f, indent=2, ensure_ascii=False)

        print(f"📁 Comparison saved to: {comparison_output}")

    except Exception as e:
        print(f"❌ Error in Demo 3: {e}")
        return False

    return True


def main():
    """Main function to run the web search demo."""

    print("🚀 Starting BlogCreator Web Search Demo...\n")

    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY not found!")
        print("Please set up your Anthropic API key in a .env file:")
        print("ANTHROPIC_API_KEY=your_key_here")
        return

    # Run the demo
    success = demo_web_search_integration()

    print("\n" + "=" * 80)
    if success:
        print("🎉 Web Search Demo Completed Successfully!")
        print("=" * 80)
        print("\n💡 Key Benefits of Web Search Integration:")
        print("✓ Real-time access to current information")
        print("✓ Discovery of latest sources and research")
        print("✓ Improved source quality and relevance")
        print("✓ Better coverage of recent developments")
        print(
            "\n📖 Check the generated JSON files in the Data/ folder for detailed results."
        )
    else:
        print("❌ Demo encountered errors. Please check your setup.")
        print("=" * 80)
        print("\n🔧 Troubleshooting:")
        print("1. Ensure ANTHROPIC_API_KEY is set correctly")
        print("2. Check your internet connection")
        print("3. Verify all dependencies are installed")


if __name__ == "__main__":
    main()
