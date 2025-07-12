#!/usr/bin/env python3
"""
Complete Example: LangChain-like System with Model Optionality and Pipelines

This example demonstrates:
1. Model optionality (switching between OpenAI and Anthropic)
2. Prompt templates with variables
3. Output parsers for structured data
4. Simple chains (single step)
5. Sequential chains (multi-step pipelines)
"""

from langchain_simple import (
    OpenAIModel,
    AnthropicModel,
    PromptTemplate,
    StringOutputParser,
    JSONOutputParser,
    LLMChain,
    SequentialChain,
)


def demo_model_optionality():
    """
    Demonstrate switching between different models without changing code.
    """
    print("=== DEMO 1: Model Optionality ===")

    # Create the same prompt template
    prompt = PromptTemplate(
        template="Write a haiku about {topic}", input_variables=["topic"]
    )

    # Create different models
    openai_model = OpenAIModel(model_name="gpt-4")
    anthropic_model = AnthropicModel(model_name="claude-3-sonnet-20240229")

    # Create chains with different models but same prompt
    openai_chain = LLMChain(llm=openai_model, prompt=prompt, verbose=True)
    anthropic_chain = LLMChain(llm=anthropic_model, prompt=prompt, verbose=True)

    # Run the same task with different models
    topic = "artificial intelligence"

    print(f"\n--- Using OpenAI Model ---")
    result1 = openai_chain.predict(topic=topic)
    print(f"Result: {result1}")

    print(f"\n--- Using Anthropic Model ---")
    result2 = anthropic_chain.predict(topic=topic)
    print(f"Result: {result2}")

    print(f"\n--- Model Info ---")
    print(f"OpenAI: {openai_model.get_model_info()}")
    print(f"Anthropic: {anthropic_model.get_model_info()}")


def demo_output_parsers():
    """
    Demonstrate structured output parsing.
    """
    print("\n\n=== DEMO 2: Output Parsers ===")

    # Create a prompt that asks for JSON output
    prompt = PromptTemplate(
        template="Analyze the sentiment of this text: '{text}'. Rate the sentiment and explain why.",
        input_variables=["text"],
    )

    model = OpenAIModel()

    # Compare string vs JSON output
    string_chain = LLMChain(
        llm=model, prompt=prompt, output_parser=StringOutputParser(), verbose=True
    )

    json_chain = LLMChain(
        llm=model, prompt=prompt, output_parser=JSONOutputParser(), verbose=True
    )

    text = "I love sunny days and ice cream!"

    print(f"\n--- String Output ---")
    string_result = string_chain.predict(text=text)
    print(f"Type: {type(string_result)}")
    print(f"Result: {string_result}")

    print(f"\n--- JSON Output (with format instructions) ---")
    try:
        json_result = json_chain.predict(text=text)
        print(f"Type: {type(json_result)}")
        print(f"Result: {json_result}")
    except Exception as e:
        print(f"JSON parsing failed (expected in demo): {e}")


def demo_sequential_pipeline():
    """
    Demonstrate a multi-step pipeline.
    """
    print("\n\n=== DEMO 3: Sequential Pipeline ===")

    # Step 1: Generate a story outline
    outline_prompt = PromptTemplate(
        template="Create a brief story outline about {theme}. Keep it to 2-3 sentences.",
        input_variables=["theme"],
    )

    # Step 2: Write the story based on the outline
    story_prompt = PromptTemplate(
        template="Write a short story based on this outline: {text}",
        input_variables=["text"],
    )

    # Step 3: Summarize the story
    summary_prompt = PromptTemplate(
        template="Summarize this story in one sentence: {text}",
        input_variables=["text"],
    )

    # Create the models
    model = OpenAIModel()

    # Create individual chains
    outline_chain = LLMChain(
        llm=model,
        prompt=outline_prompt,
        output_parser=StringOutputParser(),
        verbose=True,
    )

    story_chain = LLMChain(
        llm=model, prompt=story_prompt, output_parser=StringOutputParser(), verbose=True
    )

    summary_chain = LLMChain(
        llm=model,
        prompt=summary_prompt,
        output_parser=StringOutputParser(),
        verbose=True,
    )

    # Create the sequential pipeline
    pipeline = SequentialChain(
        chains=[outline_chain, story_chain, summary_chain], verbose=True
    )

    # Run the pipeline
    print(f"\n--- Running Multi-Step Pipeline ---")
    theme = "time travel"
    final_result = pipeline.run({"theme": theme})

    print(f"\nFinal Result: {final_result}")


def demo_configuration_flexibility():
    """
    Demonstrate how easy it is to reconfigure the system.
    """
    print("\n\n=== DEMO 4: Configuration Flexibility ===")

    # Create a template
    template = PromptTemplate(
        template="Explain {concept} to a {audience}",
        input_variables=["concept", "audience"],
    )

    # Create different configurations
    configs = [
        {"model": OpenAIModel("gpt-3.5-turbo"), "parser": StringOutputParser()},
        {
            "model": AnthropicModel("claude-3-sonnet-20240229"),
            "parser": StringOutputParser(),
        },
        {"model": OpenAIModel("gpt-4"), "parser": JSONOutputParser()},
    ]

    inputs = {"concept": "machine learning", "audience": "5-year-old"}

    for i, config in enumerate(configs, 1):
        print(f"\n--- Configuration {i} ---")
        print(f"Model: {config['model']}")
        print(f"Parser: {config['parser']}")

        chain = LLMChain(
            llm=config["model"],
            prompt=template,
            output_parser=config["parser"],
            verbose=True,
        )

        try:
            result = chain.run(inputs)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


def main():
    """
    Run all demos to show the complete system.
    """
    print("🚀 LangChain-like System Demo")
    print("=" * 50)

    # Run all demos
    demo_model_optionality()
    demo_output_parsers()
    demo_sequential_pipeline()
    demo_configuration_flexibility()

    print("\n\n✅ Demo completed!")
    print("\nKey Features Demonstrated:")
    print(
        "1. ✅ Model Optionality - Switch between OpenAI/Anthropic without code changes"
    )
    print("2. ✅ Prompt Templates - Reusable prompts with variables")
    print("3. ✅ Output Parsers - Structured data extraction")
    print("4. ✅ Simple Chains - Single-step pipelines")
    print("5. ✅ Sequential Chains - Multi-step pipelines")
    print("6. ✅ Configuration Flexibility - Easy reconfiguration")


if __name__ == "__main__":
    main()
