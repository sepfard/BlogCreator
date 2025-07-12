"""
BlogCreator Application

This package provides a blog content creation pipeline using LangChain components.
Now uses langchain's built-in functionality instead of custom implementations.

Key Components:
- Models: AnthropicModel (OpenAI removed to focus on Anthropic)
- Prompts: Uses langchain's PromptTemplate
- Output Parsers: Uses langchain's built-in parsers
- Chains: RefineTopicChain, ResearchSourceChain, ChainManager
"""

# Models
from .models import AnthropicModel

# Prompts
from .prompts import refine_topic_prompt, system_prompt, research_sources_prompt

# Output Parsers (using langchain's built-in parsers)
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

# Chains
from .chains import ChainManager, RefineTopicChain, ResearchSourceChain

__version__ = "0.1.0"

__all__ = [
    # Models
    "AnthropicModel",
    # Prompts
    "refine_topic_prompt",
    "system_prompt",
    "research_sources_prompt",
    # Output Parsers
    "JsonOutputParser",
    "StrOutputParser",
    # Chains
    "ChainManager",
    "RefineTopicChain",
    "ResearchSourceChain",
]
