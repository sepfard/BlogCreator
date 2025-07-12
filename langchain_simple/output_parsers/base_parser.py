from abc import ABC, abstractmethod
from typing import Any


class BaseOutputParser(ABC):
    """
    Abstract base class for output parsers.
    Output parsers transform raw model output into structured data.
    """

    @abstractmethod
    def parse(self, output: str) -> Any:
        """
        Parse the raw output from the model into structured data.
        """
        pass

    def get_format_instructions(self) -> str:
        """
        Return instructions for how the model should format its output.
        This can be added to prompts to guide the model's output format.
        """
        return ""
