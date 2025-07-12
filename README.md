# Simple LangChain Implementation

A lightweight implementation of LangChain-like functionality demonstrating **model optionality** and **pipeline creation** for LLM applications with **real API integrations**.

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

## 🚀 Quick Start

### 1. **Installation**

```bash
pip install -r requirements.txt
```

### 2. **Set up API Keys**

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```
OPENAI_API_KEY=your-openai-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

### 3. **Run the Example**

```bash
python Data/example_usage.py
```

## 🏗️ Architecture

Our system follows LangChain's core architecture:

```
Input → Prompt Template → Language Model → Output Parser → Result
```

### Components:

1. **Models** (`langchain_simple/models/`)

   - `BaseLanguageModel`: Abstract interface for all models
   - `OpenAIModel`: OpenAI GPT integration with real API calls
   - `AnthropicModel`: Anthropic Claude integration with real API calls

2. **Prompts** (`langchain_simple/prompts/`)

   - `PromptTemplate`: Reusable templates with variables

3. **Output Parsers** (`langchain_simple/output_parsers/`)

   - `StringOutputParser`: Plain text output
   - `JSONOutputParser`: Structured JSON output

4. **Chains** (`langchain_simple/chains/`)
   - `LLMChain`: Single-step pipeline
   - `SequentialChain`: Multi-step pipeline

## 🔧 Usage Examples

### 1. **Simple Chain:**

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

### 2. **Multi-step Pipeline:**

```python
from langchain_simple import SequentialChain

pipeline = SequentialChain(chains=[chain1, chain2, chain3])
result = pipeline.run({"input": "value"})
```

### 3. **Switch Models:**

```python
# Change this line to switch providers
model = AnthropicModel()  # Instead of OpenAIModel()
# Everything else stays the same!
```

## 📋 Requirements

- Python 3.7+
- OpenAI API key (for OpenAI models)
- Anthropic API key (for Claude models)
- Internet connection for API calls

## 🔧 Why This Approach?

**Benefits of our LangChain-like system:**

1. **🔄 Model Agnostic**: Switch between OpenAI, Anthropic, or any provider without code changes
2. **🧩 Modular**: Mix and match prompts, models, and parsers
3. **📊 Structured**: Get clean, parsed outputs instead of raw text
4. **🔗 Pipelines**: Chain multiple steps together for complex workflows
5. **🎯 Reusable**: Create templates once, use them everywhere
6. **🚀 Production Ready**: Real API integrations, not simulations

**Real-world applications:**

- **Content Generation**: Create multi-step content pipelines
- **Research Automation**: Chain research, analysis, and summarization
- **Customer Support**: Build intelligent response systems
- **Data Processing**: Extract and structure information from text
- **Creative Writing**: Generate stories, poems, and creative content

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Store API keys securely and rotate them regularly
- Use environment variables in production deployments
- Monitor API usage and costs

## 🐛 Troubleshooting

**Common Issues:**

1. **API Key Errors**: Make sure your API keys are set correctly in `.env`
2. **Rate Limiting**: Both OpenAI and Anthropic have rate limits
3. **Model Names**: Ensure you're using valid model names for each provider
4. **Network Issues**: Check your internet connection for API calls

**Error Handling:**

The system includes comprehensive error handling for:

- Missing API keys
- Invalid model names
- Network connectivity issues
- API rate limits
- Malformed prompts

## 📈 Performance Considerations

- **OpenAI Models**: Generally faster responses, various pricing tiers
- **Anthropic Models**: Longer context windows, different pricing structure
- **Caching**: Consider implementing response caching for repeated queries
- **Batch Processing**: Use batch APIs when available for better efficiency

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is provided as-is for educational and development purposes.
