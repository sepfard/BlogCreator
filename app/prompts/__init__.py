"""
BlogCreator Prompts Module

This module contains prompt templates for the BlogCreator application.
Now uses langchain's built-in PromptTemplate.
"""

from .refine_topic import refine_topic_prompt
from .System_prompt import system_prompt
from .research_sources import research_sources_prompt

__all__ = ["refine_topic_prompt", "system_prompt", "research_sources_prompt"]
