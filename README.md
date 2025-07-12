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
- **Anthropic** - Claude models

That's it! The environment stays active for quick testing. 🎯
