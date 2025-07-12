#!/usr/bin/env python3
"""
Full Pipeline Runner for BlogCreator - demonstrates the complete workflow.
This script runs both the RefineTopicChain and ResearchSourceChain in sequence.
"""

import os
import sys
from typing import Dict, Any
import json

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

from app.chains.chain_manager import ChainManager


def main():
    """Main function to run the full BlogCreator pipeline."""

    # Configuration - Updated to use Claude 4 for better web search support
    model_name = (
        "claude-sonnet-4-20250514"  # Will use Claude 4 for web search when enabled
    )
    verbose = True

    print("=== BlogCreator: Full Pipeline Runner ===\n")
    print(
        "🚀 Running complete workflow: Topic Refinement → Research Source Generation\n"
    )
    print("🔍 Web search enabled for real-time research source discovery\n")

    # Initialize the chain manager
    manager = ChainManager()

    # Define inputs for the pipeline
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

    print("Initial Input Parameters:")
    print(f"  Topic: {inputs['topic']}")
    print(f"  Keywords: {inputs['keywords']}")
    print("\n" + "=" * 70)
    print("STEP 1: Refining Topic")
    print("=" * 70)

    try:
        # Run the full pipeline
        results = manager.run_full_pipeline(
            topic=inputs["topic"],
            keywords=inputs["keywords"],
            model_name=model_name,
            verbose=verbose,
        )

        print("\n✓ Pipeline execution completed successfully!\n")

        # Display results
        print("=" * 70)
        print("STEP 1 RESULTS: Refined Topic")
        print("=" * 70)

        refine_result = results["refine_topic_result"]
        print(f"Refined Topic: {refine_result['refined_topic']}")
        print(f"Primary Keyword: {refine_result['primary_keyword']}")
        print(f"Secondary Keywords: {refine_result['secondary_keywords']}")

        print("\nAngles Considered:")
        for i, angle in enumerate(refine_result["angles_considered"], 1):
            print(f"  {i}. {angle['angle']}")
            print(f"     Rationale: {angle['rationale']}")
            print(f"     Scope: {angle['scope']}\n")

        print("\n" + "=" * 70)
        print("STEP 2 RESULTS: Research Sources")
        print("=" * 70)

        research_result = results["research_sources_result"]
        print(f"Research Strategy: {research_result['research_strategy']}\n")

        print("Priority Sources:")
        for i, source in enumerate(research_result["priority_sources"], 1):
            print(f"  {i}. {source}")

        print("\nDetailed Research Sources:")
        for i, source in enumerate(research_result["research_sources"], 1):
            print(f"\n  {i}. {source['source_name']}")
            print(f"     Category: {source['category']}")
            print(f"     Relevance: {source['relevance']}")
            print(f"     Key Questions: {source['key_questions']}")
            print(f"     URL: {source['url']}")

        # Save results to file
        output_file = "Data/full_pipeline_output.json"
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)

        print(f"\n📁 Results saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error running pipeline: {e}")
        if "authentication" in str(e) or "invalid x-api-key" in str(e):
            print("\n💡 This appears to be an API key issue.")
            print(
                "Please ensure your ANTHROPIC_API_KEY is set correctly in your .env file."
            )
        return

    print("\n" + "=" * 70)
    print("🎉 Full Pipeline Completed Successfully!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Review the research sources and begin gathering information")
    print("2. Use the refined topic as your article title/focus")
    print("3. Structure your article around the identified angles")
    print("4. Incorporate the secondary keywords throughout the content")


if __name__ == "__main__":
    main()
