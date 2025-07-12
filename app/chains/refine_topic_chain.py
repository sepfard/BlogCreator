from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser
from app.prompts.refine_topic import refine_topic_prompt
from app.prompts.System_prompt import system_prompt
from app.models.anthropic_model import AnthropicModel


class RefineTopicChain:
    """
    Chain to refine a given topic using langchain's modern approach.
    Uses system prompt and refine topic prompt template, and parses the output as JSON.
    """

    def __init__(self, model=None, output_parser=None, verbose: bool = False):
        self.model = model or AnthropicModel()
        self.output_parser = output_parser or JsonOutputParser()
        self.verbose = verbose

        # Create chat prompt template with system and human messages
        self.chat_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(prompt=system_prompt),
                HumanMessagePromptTemplate(prompt=refine_topic_prompt),
            ]
        )

        # Create the chain using the modern langchain approach
        self.chain = self.chat_prompt | self.model.chat_model | self.output_parser

    def run(self, inputs):
        """
        Run the refine topic chain with the given inputs.
        """
        topic = inputs.get("topic")
        keywords = inputs.get("keywords")

        if not topic:
            raise ValueError("Input 'topic' is required.")
        if not keywords:
            raise ValueError("Input 'keywords' is required.")

        # Add format instructions to the input
        format_instructions = self.output_parser.get_format_instructions()

        # Prepare inputs with format instructions
        chain_inputs = {
            "topic": topic,
            "keywords": keywords,
            "format_instructions": format_instructions,
        }

        if self.verbose:
            print(f"[RefineTopicChain] Running with inputs: {chain_inputs}")

        # Run the chain using the modern approach
        result = self.chain.invoke(chain_inputs)

        if self.verbose:
            print(f"[RefineTopicChain] Result: {result}")

        return result

    def get_input_keys(self):
        """Return the input keys this chain expects."""
        return ["topic", "keywords"]

    def get_output_keys(self):
        """Return the output keys this chain produces."""
        return [
            "angles_considered",
            "refined_topic",
            "primary_keyword",
            "secondary_keywords",
        ]
