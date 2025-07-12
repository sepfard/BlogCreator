import os
from .base_model import BaseLanguageModel
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


class AnthropicModel(BaseLanguageModel):
    """
    Anthropic implementation of BaseLanguageModel using langchain's ChatAnthropic.
    """

    def __init__(
        self,
        model_name: str = "claude-3-5-sonnet-20241022",
        api_key: str = None,
        enable_web_search: bool = False,
        **kwargs,
    ):
        super().__init__(model_name, **kwargs)
        load_dotenv()
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key is required. Set it via the api_key parameter or ANTHROPIC_API_KEY environment variable."
            )
        self.provider = "Anthropic"
        self.enable_web_search = enable_web_search

        # Configure base model parameters
        chat_model_kwargs = {
            "anthropic_api_key": self.api_key,
            "temperature": 0.7,
            "max_tokens": 4000,
        }

        # If web search is enabled, use Claude 4 model and configure tools
        if self.enable_web_search:
            # Use Claude 4 model for better web search support
            chat_model_kwargs["model"] = "claude-sonnet-4-20250514"
            # Configure web search tools and betas
            chat_model_kwargs["tools"] = [
                {"name": "web_search", "type": "web_search_20250305"}
            ]
            chat_model_kwargs["betas"] = ["web-search-2025-03-05"]
            print(f"[AnthropicModel] Web search enabled with Claude 4 model")
        else:
            # Use the provided model name when web search is not enabled
            chat_model_kwargs["model"] = self.model_name

        self.chat_model = ChatAnthropic(**chat_model_kwargs)

    def generate(
        self,
        prompt: str,
        system_prompt: str = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs,
    ) -> str:
        """
        Generate response using langchain's ChatAnthropic with proper system prompt handling.
        """
        try:
            # Update model parameters if provided
            if max_tokens != 4000 or temperature != 0.7:
                chat_model_kwargs = {
                    "anthropic_api_key": self.api_key,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }

                if self.enable_web_search:
                    chat_model_kwargs["model"] = "claude-sonnet-4-20250514"
                    chat_model_kwargs["tools"] = [
                        {"name": "web_search", "type": "web_search_20250305"}
                    ]
                    chat_model_kwargs["betas"] = ["web-search-2025-03-05"]
                else:
                    chat_model_kwargs["model"] = self.model_name

                self.chat_model = ChatAnthropic(**chat_model_kwargs)

            # Create messages
            messages = []

            # Add system message if provided
            if system_prompt:
                messages.append(SystemMessage(content=system_prompt))

            # Add human message
            messages.append(HumanMessage(content=prompt))

            # Get response
            response = self.chat_model.invoke(messages)
            return response.content

        except Exception as e:
            raise Exception(f"Anthropic API call failed: {str(e)}")

    def create_chat_prompt_template(self, system_template: str, human_template: str):
        """
        Create a ChatPromptTemplate with system and human message templates.
        """
        return ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(system_template),
                HumanMessagePromptTemplate.from_template(human_template),
            ]
        )

    def get_model_info(self):
        return {
            "provider": self.provider,
            "model_name": self.model_name,
            "api_key_set": self.api_key is not None,
            "config": self.config,
            "web_search_enabled": self.enable_web_search,
        }
