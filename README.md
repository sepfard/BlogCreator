# BlogCreator

A Python backend project for generating, refining, and managing blog content using LLMs, with modular chains, prompt templates, and output parsers.

## 🚀 Quick Start

1. **One-time setup** (creates virtual environment and installs dependencies):

   ```bash
   ./activate.sh
   ```

2. **Daily usage** (activates environment):

   ```bash
   source venv/bin/activate
   ```

3. **Add your API keys** to the `.env` file:

   ```
   OPENAI_API_KEY=your-actual-openai-key
   ANTHROPIC_API_KEY=your-actual-anthropic-key
   ```

4. **Run the project**:
   ```bash
   python run_refine_topic.py
   # or
   python Data/example_usage.py
   ```

## 🔑 Get API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/

## 📁 Project Structure

```
app/
├── chains/        # Chain logic and orchestration
├── models/        # LLM model wrappers
├── prompts/       # Prompt templates
└── output_parsers/ # Output parsing logic
Data/              # Example data and generated outputs
```

## 🛠️ Tech Stack

- **Python 3.10+**
- **LangChain** - LLM orchestration
- **OpenAI** - GPT models
- **Anthropic** - Claude models with **Web Search** capabilities

## 🔍 Web Search Integration

BlogCreator now supports real-time web search for enhanced research capabilities!

### Features

- **Real-time information gathering** - Access current data and recent developments
- **Authoritative source discovery** - Find credible, up-to-date sources automatically
- **Enhanced research quality** - Improve article authority with latest information
- **Flexible configuration** - Enable/disable web search as needed

### Usage

**Full Pipeline with Web Search (Default):**

```bash
python run_full_pipeline.py
```

**Demo Web Search Capabilities:**

```bash
python demo_web_search.py
```

**Test Web Search Integration:**

```bash
python test_web_search.py
```

### Configuration

**Enable Web Search (Default):**

```python
from app.chains.research_source_chain import ResearchSourceChain

# Web search enabled by default
chain = ResearchSourceChain(enable_web_search=True)
```

**Disable Web Search:**

```python
# Traditional research without web search
chain = ResearchSourceChain(enable_web_search=False)
```

**Using ChainManager:**

```python
from app.chains.chain_manager import ChainManager

manager = ChainManager()
manager.setup_research_source_chain(
    enable_web_search=True  # Default is True
)
```

### Web Search Benefits

- 🔍 **Current Information**: Access latest statistics, trends, and developments
- 📊 **Real-time Data**: Get up-to-date market data and industry reports
- 🎯 **Targeted Research**: Execute specific search queries for precise information
- ✅ **Source Verification**: Verify credibility and currency of sources
- 🚀 **Enhanced Quality**: Improve article authority and relevance

That's it! The environment stays active for quick testing. 🎯
