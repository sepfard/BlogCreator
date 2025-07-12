# Simple LangChain Implementation

A lightweight implementation of LangChain-like functionality demonstrating **model optionality** and **pipeline creation** for LLM applications.

## 🎯 Key Features

### 1. **Model Optionality**

Switch between different LLM providers without changing your code:

```python
from langchain_simple import OpenAIModel, AnthropicModel, LLMChain, PromptTemplate

# Same prompt, different models
prompt = PromptTemplate(template="Explain {topic}", input_variables=["topic"])

# Just swap the model - everything else stays the same!
openai_chain = LLMChain(llm=OpenAIModel(), prompt=prompt)
anthropic_chain = LLMChain(llm=AnthropicModel(), prompt=prompt)
```

### 2. **Pipeline Creation**

Build complex multi-step workflows:

```python
from langchain_simple import SequentialChain

# Create a 3-step pipeline
pipeline = SequentialChain(chains=[
    outline_chain,  # Step 1: Generate outline
    story_chain,    # Step 2: Write story
    summary_chain   # Step 3: Summarize
])

result = pipeline.run({"theme": "time travel"})
```

### 3. **Structured Outputs**

Parse model responses into structured data:

```python
from langchain_simple import JSONOutputParser

chain = LLMChain(
    llm=model,
    prompt=prompt,
    output_parser=JSONOutputParser()  # Automatically parses JSON
)
```

## 🏗️ Architecture

Our system follows LangChain's core architecture:

```
Input → Prompt Template → Language Model → Output Parser → Result
```

### Components:

1. **Models** (`langchain_simple/models/`)

   - `BaseLanguageModel`: Abstract interface for all models
   - `OpenAIModel`: OpenAI implementation
   - `AnthropicModel`: Anthropic implementation

2. **Prompts** (`langchain_simple/prompts/`)

   - `PromptTemplate`: Reusable templates with variables

3. **Output Parsers** (`langchain_simple/output_parsers/`)

   - `StringOutputParser`: Plain text output
   - `JSONOutputParser`: Structured JSON output

4. **Chains** (`langchain_simple/chains/`)
   - `LLMChain`: Single-step pipeline
   - `SequentialChain`: Multi-step pipeline

## 🚀 Quick Start

1. **Simple Chain:**

```python
from langchain_simple import OpenAIModel, PromptTemplate, LLMChain

model = OpenAIModel()
prompt = PromptTemplate(
    template="Write a haiku about {topic}",
    input_variables=["topic"]
)
chain = LLMChain(llm=model, prompt=prompt)

result = chain.predict(topic="artificial intelligence")
```

2. **Multi-step Pipeline:**

```python
from langchain_simple import SequentialChain

pipeline = SequentialChain(chains=[chain1, chain2, chain3])
result = pipeline.run({"input": "value"})
```

3. **Switch Models:**

```python
# Change this line to switch providers
model = AnthropicModel()  # Instead of OpenAIModel()
# Everything else stays the same!
```

## 📋 Example Output

Running `python3 example_usage.py` demonstrates:

```
🚀 LangChain-like System Demo
==================================================
=== DEMO 1: Model Optionality ===

--- Using OpenAI Model ---
[LLMChain] Starting chain with inputs: {'topic': 'artificial intelligence'}
[LLMChain] Formatted prompt: Write a haiku about artificial intelligence...
Result: [OpenAI gpt-4] Simulated response...

--- Using Anthropic Model ---
[LLMChain] Starting chain with inputs: {'topic': 'artificial intelligence'}
[LLMChain] Formatted prompt: Write a haiku about artificial intelligence...
Result: [Anthropic claude-3-sonnet-20240229] Simulated response...
```

## 🔧 Why This Approach?

**Benefits of our LangChain-like system:**

1. **🔄 Model Agnostic**: Switch between OpenAI, Anthropic, or any provider without code changes
2. **🧩 Modular**: Mix and match prompts, models, and parsers
3. **📊 Structured**: Get clean, parsed outputs instead of raw text
4. **🔗 Pipelines**: Chain multiple steps together for complex workflows
5. **🎯 Reusable**: Create templates once, use them everywhere

**Real-world applications:**

- Content generation pipelines
- Data analysis workflows
- Multi-step reasoning tasks
- A/B testing different models
- Building LLM-powered applications

## 🎓 Understanding the Code

Each component is designed to be:

- **Extensible**: Easy to add new models or parsers
- **Testable**: Clear interfaces for unit testing
- **Maintainable**: Well-structured with clear responsibilities

This implementation gives you the power of LangChain's concepts in a simple, understandable codebase!
