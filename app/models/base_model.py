from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseLanguageModel(ABC):
    """
    Abstract base class for all language models.
    This provides the interface that all LLM providers must implement,
    allowing us to switch between different models without changing our code.
    """

    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.config = kwargs

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response from the model given a prompt.
        This is the core method that all models must implement.
        """
        pass

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """
        Return information about the model (name, provider, etc.)
        """
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model_name})"
