import json
from typing import Dict, Any
from .base_parser import BaseOutputParser


class JSONOutputParser(BaseOutputParser):
    """
    Parser that extracts and parses JSON from model output.
    This is useful when you want structured data from the model.
    """

    def parse(self, output: str) -> Dict[str, Any]:
        """
        Parse JSON from the model output.
        Handles cases where the JSON might be embedded in other text.
        """
        # Try to parse the entire output as JSON first
        try:
            return json.loads(output.strip())
        except json.JSONDecodeError:
            pass

        # If that fails, try to find JSON within the output
        # Look for content between { and }
        import re

        json_match = re.search(r"\{.*\}", output, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        # If all else fails, raise an error
        raise ValueError(f"Could not parse JSON from output: {output}")

    def get_format_instructions(self) -> str:
        return """Please provide your response as valid JSON format. Example:
{
    "key1": "value1",
    "key2": "value2"
}"""
