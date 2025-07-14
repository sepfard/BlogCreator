#!/usr/bin/env python3
"""
Full Pipeline Runner for BlogCreator - simplified and direct workflow.
This script runs both the RefineTopicChain and ResearchSourceChain in sequence.
"""

import os
import sys
import json
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

from app.chains.refine_topic_chain import RefineTopicChain
from app.chains.research_source_chain import ResearchSourceChain
from app.chains.key_messaage import KeyMessageChain
from app.chains.outline import OutlineChain
from app.chains.first_draft import FirstDraftChain

API_KEY = os.getenv("ANTHROPIC_API_KEY")


class BlogState:
    def __init__(self):
        self.topic = None
        self.keywords = None
        self.refined_topic = None
        self.secondary_keywords = None
        self.research_sources = None
        self.thesis_statement = None
        self.main_points = None
        self.reader_takeaway = None
        self.content_style = None
        self.cta_direction = None
        self.outline = None
        self.transitions = None
        self.word_count_target = None
        self.draft = None
        self.writer_notes = None


def create_anthropic_model(
    model_name: str,
    enable_web_search: bool = False,
    temperature: float = 1.0,
    max_tokens: int = 10000,
):
    load_dotenv()
    if not API_KEY:
        raise ValueError("ANTHROPIC_API_KEY environment variable is required.")

    # Configure model parameters
    chat_model_kwargs = {
        "anthropic_api_key": API_KEY,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "disable_streaming": True,
    }

    # Configure model_kwargs for prompt caching
    model_kwargs = {}

    # Set model name
    if enable_web_search:
        chat_model_kwargs["model"] = "claude-sonnet-4-20250514"
        print(f"[Model] Using Claude 4 for web search")
    else:
        chat_model_kwargs["model"] = model_name

    # Add model_kwargs if prompt caching is enabled
    if model_kwargs:
        chat_model_kwargs["model_kwargs"] = model_kwargs

    # Create base model
    print(chat_model_kwargs)
    llm = ChatAnthropic(**chat_model_kwargs)

    # Bind web search tools if enabled
    if enable_web_search:
        web_search_tool = {
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 3,
        }
        llm = llm.bind_tools([web_search_tool])
        print(f"[Model] Web search tools bound successfully")

    return llm


def main():
    """Main function to run the full BlogCreator pipeline."""

    # Configuration
    model_name = "claude-sonnet-4-20250514"
    verbose = False

    print("=== BlogCreator: Full Pipeline Runner ===\n")
    print(
        "🚀 Running complete workflow: Topic Refinement → Research Source Generation\n"
    )

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
    blog_state = BlogState()
    blog_state.topic = inputs["topic"]
    blog_state.keywords = inputs["keywords"]

    print("Initial Input Parameters:")
    print(f"  Topic: {inputs['topic']}")
    print(f"  Keywords: {inputs['keywords']}")
    print(f"  Model: {model_name}")

    try:
        print("\n" + "=" * 70)
        print("STEP 1: Refining Topic")
        print("=" * 70)

        refine_model = create_anthropic_model(model_name, enable_web_search=False)
        refine_chain = RefineTopicChain(model=refine_model, verbose=verbose)

        refine_inputs = {"topic": inputs["topic"], "keywords": inputs["keywords"]}

        refine_result = refine_chain.run(refine_inputs)

        blog_state.refined_topic = refine_result["refined_topic"]
        blog_state.keywords = refine_result["secondary_keywords"] + [
            refine_result["primary_keyword"]
        ]

        print("\n" + "=" * 70)
        print("STEP 2: Generating Research Sources")
        print("=" * 70)

        research_model = create_anthropic_model(model_name, enable_web_search=True)
        research_chain = ResearchSourceChain(model=research_model, verbose=verbose)

        research_inputs = {
            "refined_topic": blog_state.refined_topic,
            "keywords": blog_state.keywords,
        }

        research_result = research_chain.run(research_inputs)
        blog_state.research_sources = research_result["research_sources"]
        print("✓ Research source generation completed successfully!\n")

        print("\n" + "=" * 70)
        print("STEP 3: Generating Key Message")
        print("=" * 70)

        key_message_model = create_anthropic_model(model_name, enable_web_search=False)
        key_message_chain = KeyMessageChain(model=key_message_model, verbose=verbose)

        key_message_inputs = {
            "refined_topic": blog_state.refined_topic,
            "keywords": blog_state.keywords,
        }

        key_message_result = key_message_chain.run(key_message_inputs)
        for key, value in key_message_result.items():
            setattr(blog_state, key, value)

        print("✓ Key message generation completed successfully!\n")

        print("\n" + "=" * 70)
        print("STEP 4: Generating Outline")
        print("=" * 70)

        outline_model = create_anthropic_model(model_name, enable_web_search=False)
        outline_chain = OutlineChain(model=outline_model, verbose=verbose)

        outline_inputs = {
            "thesis_statement": blog_state.thesis_statement,
            "main_points": blog_state.main_points,
            "research_sources": blog_state.research_sources,
            "keywords": blog_state.keywords,
        }

        outline_result = outline_chain.run(outline_inputs)
        for key, value in outline_result.items():
            setattr(blog_state, key, value)

        print("\n" + "=" * 70)
        print("STEP 5: Generating First Draft")
        print("=" * 70)

        first_draft_model = create_anthropic_model(model_name, enable_web_search=False)
        first_draft_chain = FirstDraftChain(model=first_draft_model, verbose=verbose)

        # update outline - match source names to URLs
        source_name_to_url = {
            source["source_name"]: source["url"]
            for source in blog_state.research_sources
        }

        def add_urls_to_sources(item):
            """Helper function to add URLs to any item with sources"""
            if "sources" in item:
                item["url"] = [
                    url
                    for source_name in item["sources"]
                    if (url := source_name_to_url.get(source_name)) is not None
                ]

        for section in blog_state.outline:
            add_urls_to_sources(section)

            # Process subsections if they exist
            for subsection in section.get("subsections", []):
                add_urls_to_sources(subsection)

        first_draft_inputs = {
            "outline": blog_state.outline,
            "content_style": blog_state.content_style,
            "reader_takeaway": blog_state.reader_takeaway,
            "keywords": blog_state.keywords,
            "word_count_target": blog_state.word_count_target,
        }

        first_draft_result = first_draft_chain.run(first_draft_inputs)
        for key, value in first_draft_result.items():
            setattr(blog_state, key, value)
        # save results to file
        output_file = "data/run_data/results.json"
        os.makedirs(os.path.dirname("data/run_data/"), exist_ok=True)
        with open(output_file, "w") as f:
            json.dump(blog_state.__dict__, f, indent=2)
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


if __name__ == "__main__":
    main()
