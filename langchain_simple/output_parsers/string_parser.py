from .base_parser import BaseOutputParser


class StringOutputParser(BaseOutputParser):
    """
    Simple parser that returns the raw output as-is.
    This is useful when you just want the plain text response.
    """

    def parse(self, output: str) -> str:
        """
        Return the output as-is, with optional trimming.
        """
        return output.strip()

    def get_format_instructions(self) -> str:
        return "Please provide your response as plain text."
