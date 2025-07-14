from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser
from app.prompts.first_draft import first_draft_prompt


class FirstDraftChain:
    def __init__(self, model, verbose: bool = False):
        self.chat_model = model
        self.verbose = verbose
        self.output_parser = JsonOutputParser()
        self.input_keys = [
            "outline",
            "content_style",
            "reader_takeaway",
            "keywords",
            "word_count_target",
        ]
        self.output_keys = ["draft", "writer_notes"]

        messages = [
            HumanMessagePromptTemplate(prompt=first_draft_prompt),
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
            print(f"[FirstDraftChain] Running with inputs: {chain_inputs}")

        result = self.chain.invoke(chain_inputs)

        if self.verbose:
            print(f"[FirstDraftChain] Result: {result}")

        return result

    def get_input_keys(self):
        return self.input_keys

    def get_output_keys(self):
        return self.output_keys
