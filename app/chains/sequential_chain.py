from typing import Dict, Any, List
from .base_chain import BaseChain


class SequentialChain(BaseChain):
    """
    A chain that runs multiple chains in sequence.
    The output of one chain becomes the input to the next chain.
    This allows for complex multi-step pipelines.
    """

    def __init__(self, chains: List[BaseChain], verbose: bool = False):
        super().__init__(verbose)
        self.chains = chains
        self._validate_chains()

    def _validate_chains(self):
        """
        Validate that the chains can be connected in sequence.
        """
        if not self.chains:
            raise ValueError("At least one chain must be provided")

        # Check that output keys of one chain match input keys of the next
        for i in range(len(self.chains) - 1):
            current_chain = self.chains[i]
            next_chain = self.chains[i + 1]

            current_outputs = set(current_chain.get_output_keys())
            next_inputs = set(next_chain.get_input_keys())

            # For this simple implementation, we'll be flexible about matching
            # In a real implementation, you'd want stricter validation
            self._log(f"Chain {i} outputs: {current_outputs}")
            self._log(f"Chain {i+1} inputs: {next_inputs}")

    def run(self, inputs: Dict[str, Any]) -> Any:
        """
        Execute all chains in sequence.
        """
        self._log(f"Starting sequential chain with {len(self.chains)} chains")

        current_inputs = inputs.copy()

        for i, chain in enumerate(self.chains):
            self._log(
                f"Executing chain {i+1}/{len(self.chains)}: {chain.__class__.__name__}"
            )

            try:
                # Run the chain
                result = chain.run(current_inputs)
                self._log(f"Chain {i+1} result: {result}")

                # Prepare inputs for next chain
                if i < len(self.chains) - 1:  # Not the last chain
                    if isinstance(result, dict):
                        # If result is a dict, merge it with current inputs
                        current_inputs.update(result)
                    else:
                        # If result is not a dict, add it as 'text' key
                        current_inputs["text"] = result

            except Exception as e:
                raise ValueError(f"Chain {i+1} failed: {e}")

        return result

    def get_input_keys(self) -> List[str]:
        """
        Return the input keys of the first chain.
        """
        return self.chains[0].get_input_keys() if self.chains else []

    def get_output_keys(self) -> List[str]:
        """
        Return the output keys of the last chain.
        """
        return self.chains[-1].get_output_keys() if self.chains else []
