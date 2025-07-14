from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from app.prompts.research_sources import research_sources_prompt
from app.prompts.System_prompt import system_prompt


class ResearchSourceChain:

    def __init__(self, model, verbose: bool = False):
        self.chat_model = model
        self.verbose = verbose
        self.output_parser = JsonOutputParser()
        self.input_keys = ["refined_topic", "keywords"]
        self.output_keys = ["research_sources"]

        messages = [
            SystemMessagePromptTemplate(prompt=system_prompt),
            HumanMessagePromptTemplate(prompt=research_sources_prompt),
        ]

        self.chat_prompt = ChatPromptTemplate.from_messages(messages)

        self.chain = self.chat_prompt | self.chat_model | self.output_parser

    def _check_web_search_enabled(self):
        if hasattr(self.chat_model, "bound_tools") and self.chat_model.bound_tools:
            return any(
                "web_search" in str(tool) for tool in self.chat_model.bound_tools
            )

        if hasattr(self.chat_model, "kwargs") and "tools" in self.chat_model.kwargs:
            return bool(self.chat_model.kwargs["tools"])

        return False

    def run(self, inputs):
        for key in self.input_keys:
            if key not in inputs:
                raise ValueError(f"Input '{key}' is required.")

        format_instructions = self.output_parser.get_format_instructions()

        chain_inputs = {}
        for key in self.input_keys:
            chain_inputs[key] = inputs[key]

        chain_inputs["format_instructions"] = format_instructions

        result = self.chain.invoke(chain_inputs)

        if self.verbose:
            print(f"[ResearchSourceChain] Result: {result}")

        return result

    def get_input_keys(self):
        return self.input_keys

    def get_output_keys(self):
        return self.output_keys
