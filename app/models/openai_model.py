import os
from typing import Dict, Any
from .base_model import BaseLanguageModel

try:
    from openai import OpenAI
except ImportError:
    raise ImportError(
        "OpenAI package is required. Install it with: pip install openai>=1.0.0"
    )


class OpenAIModel(BaseLanguageModel):
    """
    OpenAI implementation of BaseLanguageModel.
    Makes real API calls to OpenAI's GPT models.
    """

    def __init__(
        self, model_name: str = "gpt-3.5-turbo", api_key: str = None, **kwargs
    ):
        super().__init__(model_name, **kwargs)

        # Get API key from parameter, environment variable, or raise error
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenAI API key is required. Set it via the api_key parameter or OPENAI_API_KEY environment variable."
            )

        self.provider = "OpenAI"
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Make actual OpenAI API call.
        """
        try:
            # Extract parameters with defaults
            max_tokens = kwargs.get("max_tokens", 150)
            temperature = kwargs.get("temperature", 0.7)

            # Make the API call
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"OpenAI API call failed: {str(e)}")

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model_name": self.model_name,
            "api_key_set": self.api_key is not None,
            "config": self.config,
        }
