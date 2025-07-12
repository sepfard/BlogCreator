from typing import Dict, Any, List
import re


class PromptTemplate:
    """
    A template for creating prompts with variable substitution.
    This allows us to create reusable prompt templates and fill them with different values.

    Example:
        template = PromptTemplate(
            template="Translate {text} to {language}",
            input_variables=["text", "language"]
        )
        prompt = template.format(text="Hello", language="Spanish")
    """

    def __init__(self, template: str, input_variables: List[str]):
        self.template = template
        self.input_variables = input_variables
        self._validate_template()

    def _validate_template(self):
        """
        Validate that all variables in the template are listed in input_variables.
        This helps catch errors early.
        """
        # Find all variables in the template using regex
        template_variables = set(re.findall(r"\{(\w+)\}", self.template))
        input_variables_set = set(self.input_variables)

        missing_variables = template_variables - input_variables_set
        if missing_variables:
            raise ValueError(
                f"Template contains variables not listed in input_variables: {missing_variables}"
            )

        extra_variables = input_variables_set - template_variables
        if extra_variables:
            raise ValueError(
                f"input_variables contains variables not found in template: {extra_variables}"
            )

    def format(self, **kwargs) -> str:
        """
        Format the template with the provided variables.
        """
        # Check that all required variables are provided
        missing_vars = set(self.input_variables) - set(kwargs.keys())
        if missing_vars:
            raise ValueError(f"Missing required variables: {missing_vars}")

        # Format the template
        return self.template.format(**kwargs)

    def partial(self, **kwargs) -> "PromptTemplate":
        """
        Create a new PromptTemplate with some variables pre-filled.
        This is useful for creating specialized versions of a template.
        """
        # Replace the specified variables
        new_template = self.template.format(**kwargs)

        # Remove the filled variables from input_variables
        new_input_variables = [var for var in self.input_variables if var not in kwargs]

        return PromptTemplate(
            template=new_template, input_variables=new_input_variables
        )

    def __str__(self) -> str:
        return f"PromptTemplate(template='{self.template}', input_variables={self.input_variables})"
