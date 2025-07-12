from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser
from app.prompts.research_sources import research_sources_prompt
from app.prompts.System_prompt import system_prompt
from app.models.anthropic_model import AnthropicModel


class ResearchSourceChain:
    """
    Chain to generate research sources based on refined topic and keywords.
    Uses system prompt and research sources prompt template, and parses the output as JSON.
    Supports web search capability for real-time research.
    """

    def __init__(
        self,
        model=None,
        output_parser=None,
        verbose: bool = False,
        enable_web_search: bool = True,
    ):
        self.model = model or AnthropicModel(enable_web_search=enable_web_search)
        self.output_parser = output_parser or JsonOutputParser()
        self.verbose = verbose
        self.enable_web_search = enable_web_search

        # Create chat prompt template with system and human messages
        self.chat_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(prompt=system_prompt),
                HumanMessagePromptTemplate(prompt=research_sources_prompt),
            ]
        )

        # Create the chain using the modern langchain approach
        self.chain = self.chat_prompt | self.model.chat_model | self.output_parser

    def run(self, inputs):
        """
        Run the research source chain with the given inputs.
        """
        refined_topic = inputs.get("refined_topic")
        keywords = inputs.get("keywords")

        if not refined_topic:
            raise ValueError("Input 'refined_topic' is required.")
        if not keywords:
            raise ValueError("Input 'keywords' is required.")

        # Add format instructions to the input
        format_instructions = self.output_parser.get_format_instructions()

        # Prepare inputs with format instructions
        chain_inputs = {
            "refined_topic": refined_topic,
            "keywords": keywords,
            "format_instructions": format_instructions,
        }

        if self.verbose:
            print(f"[ResearchSourceChain] Running with inputs: {chain_inputs}")
            print(f"[ResearchSourceChain] Web search enabled: {self.enable_web_search}")

        # Run the chain using the modern approach
        result = self.chain.invoke(chain_inputs)

        if self.verbose:
            print(f"[ResearchSourceChain] Result: {result}")

        return result

    def get_input_keys(self):
        """Return the input keys this chain expects."""
        return ["refined_topic", "keywords"]

    def get_output_keys(self):
        """Return the output keys this chain produces."""
        return [
            "research_sources",
        ]
