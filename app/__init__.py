"""
Simple LangChain Implementation

This package provides a simple implementation of LangChain-like functionality
with model optionality and pipeline creation capabilities.

Key Components:
- Models: BaseLanguageModel, OpenAIModel, AnthropicModel
- Prompts: PromptTemplate
- Output Parsers: StringOutputParser, JSONOutputParser
- Chains: LLMChain, SequentialChain
"""

# Models
from .models import BaseLanguageModel, OpenAIModel, AnthropicModel

# Prompts
from .prompts import PromptTemplate

# Output Parsers
from .output_parsers import BaseOutputParser, StringOutputParser, JSONOutputParser

# Chains
from .chains import BaseChain, LLMChain, SequentialChain

__version__ = "0.1.0"

__all__ = [
    # Models
    "BaseLanguageModel",
    "OpenAIModel",
    "AnthropicModel",
    # Prompts
    "PromptTemplate",
    # Output Parsers
    "BaseOutputParser",
    "StringOutputParser",
    "JSONOutputParser",
    # Chains
    "BaseChain",
    "LLMChain",
    "SequentialChain",
]
