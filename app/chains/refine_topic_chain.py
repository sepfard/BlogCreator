from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from app.prompts.refine_topic import refine_topic_prompt
from app.prompts.System_prompt import system_prompt


class RefineTopicChain:
    def __init__(self, model, verbose: bool = False):
        self.chat_model = model
        self.verbose = verbose
        self.output_parser = JsonOutputParser()
        self.input_keys = ["topic", "keywords"]
        self.output_keys = [
            "angles_considered",
            "refined_topic",
            "primary_keyword",
            "secondary_keywords",
        ]
        messages = [
            SystemMessagePromptTemplate(prompt=system_prompt),
            HumanMessagePromptTemplate(prompt=refine_topic_prompt),
        ]

        self.chat_prompt = ChatPromptTemplate.from_messages(messages)

        self.chain = self.chat_prompt | self.chat_model | self.output_parser

    def run(self, inputs):

        for key in self.input_keys:
            if key not in inputs:
                raise ValueError(f"Input '{key}' is required.")

        format_instructions = self.output_parser.get_format_instructions()

        chain_inputs = {}
        for key in self.input_keys:
            chain_inputs[key] = inputs[key]

        chain_inputs["format_instructions"] = format_instructions

        if self.verbose:
            print(f"[RefineTopicChain] Running with inputs: {chain_inputs}")

        result = self.chain.invoke(chain_inputs)

        if self.verbose:
            print(f"[RefineTopicChain] Result: {result}")

        return result

    def get_input_keys(self):
        return self.input_keys

    def get_output_keys(self):
        return self.output_keys
