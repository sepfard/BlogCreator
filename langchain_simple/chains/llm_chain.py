from typing import Dict, Any, List, Optional
from .base_chain import BaseChain
from ..models.base_model import BaseLanguageModel
from ..prompts.prompt_template import PromptTemplate
from ..output_parsers.base_parser import BaseOutputParser
from ..output_parsers.string_parser import StringOutputParser


class LLMChain(BaseChain):
    """
    A chain that connects a prompt template, language model, and output parser.
    This is the fundamental building block of our pipeline system.

    Flow: Input -> Prompt Template -> Model -> Output Parser -> Output
    """

    def __init__(
        self,
        llm: BaseLanguageModel,
        prompt: PromptTemplate,
        output_parser: Optional[BaseOutputParser] = None,
        verbose: bool = False,
    ):
        super().__init__(verbose)
        self.llm = llm
        self.prompt = prompt
        self.output_parser = output_parser or StringOutputParser()

    def run(self, inputs: Dict[str, Any]) -> Any:
        """
        Execute the chain:
        1. Format the prompt template with inputs
        2. Send to the language model
        3. Parse the output
        """
        self._log(f"Starting chain with inputs: {inputs}")

        # Step 1: Format the prompt template
        try:
            formatted_prompt = self.prompt.format(**inputs)
            self._log(f"Formatted prompt: {formatted_prompt[:100]}...")
        except Exception as e:
            raise ValueError(f"Failed to format prompt: {e}")

        # Step 2: Add format instructions if output parser provides them
        format_instructions = self.output_parser.get_format_instructions()
        if format_instructions:
            formatted_prompt += f"\n\n{format_instructions}"
            self._log("Added format instructions to prompt")

        # Step 3: Send to language model
        try:
            raw_output = self.llm.generate(formatted_prompt)
            self._log(f"Raw model output: {raw_output[:100]}...")
        except Exception as e:
            raise ValueError(f"Failed to generate response: {e}")

        # Step 4: Parse the output
        try:
            parsed_output = self.output_parser.parse(raw_output)
            self._log(f"Parsed output: {parsed_output}")
            return parsed_output
        except Exception as e:
            raise ValueError(f"Failed to parse output: {e}")

    def get_input_keys(self) -> List[str]:
        """
        Return the input keys expected by the prompt template.
        """
        return self.prompt.input_variables

    def get_output_keys(self) -> List[str]:
        """
        Return the output keys. For LLMChain, this is typically just 'text'.
        """
        return ["text"]

    def predict(self, **kwargs) -> Any:
        """
        Convenience method for making predictions with keyword arguments.
        """
        return self.run(kwargs)
