import os
from typing import Dict, Any
from .base_model import BaseLanguageModel

try:
    from anthropic import Anthropic
except ImportError:
    raise ImportError(
        "Anthropic package is required. Install it with: pip install anthropic>=0.18.0"
    )


class AnthropicModel(BaseLanguageModel):
    """
    Anthropic implementation of BaseLanguageModel.
    Makes real API calls to Anthropic's Claude models.
    """

    def __init__(
        self,
        model_name: str = "claude-3-sonnet-20240229",
        api_key: str = None,
        **kwargs,
    ):
        super().__init__(model_name, **kwargs)

        # Get API key from parameter, environment variable, or raise error
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key is required. Set it via the api_key parameter or ANTHROPIC_API_KEY environment variable."
            )

        self.provider = "Anthropic"
        self.client = Anthropic(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Make actual Anthropic API call.
        """
        try:
            # Extract parameters with defaults
            max_tokens = kwargs.get("max_tokens", 150)
            temperature = kwargs.get("temperature", 0.7)

            # Make the API call
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text

        except Exception as e:
            raise Exception(f"Anthropic API call failed: {str(e)}")

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model_name": self.model_name,
            "api_key_set": self.api_key is not None,
            "config": self.config,
        }
