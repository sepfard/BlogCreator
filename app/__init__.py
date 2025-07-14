"""
BlogCreator Application

This package provides a blog content creation pipeline using LangChain components.
Uses langchain's ChatAnthropic directly for maximum simplicity.

Key Components:
- Prompts: Uses langchain's PromptTemplate
- Chains: RefineTopicChain, ResearchSourceChain
"""

# Prompts
from .prompts import refine_topic_prompt, system_prompt, research_sources_prompt

# Chains
from .chains import RefineTopicChain, ResearchSourceChain

__version__ = "0.1.0"

__all__ = [
    # Prompts
    "refine_topic_prompt",
    "system_prompt",
    "research_sources_prompt",
    # Chains
    "RefineTopicChain",
    "ResearchSourceChain",
]
