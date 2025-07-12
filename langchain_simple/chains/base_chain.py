from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseChain(ABC):
    """
    Abstract base class for all chains.
    Chains represent pipelines that process inputs through multiple steps.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    @abstractmethod
    def run(self, inputs: Dict[str, Any]) -> Any:
        """
        Execute the chain with the given inputs.
        """
        pass

    @abstractmethod
    def get_input_keys(self) -> List[str]:
        """
        Return the list of input keys this chain expects.
        """
        pass

    @abstractmethod
    def get_output_keys(self) -> List[str]:
        """
        Return the list of output keys this chain produces.
        """
        pass

    def _log(self, message: str):
        """
        Log a message if verbose mode is enabled.
        """
        if self.verbose:
            print(f"[{self.__class__.__name__}] {message}")

    def __call__(self, inputs: Dict[str, Any]) -> Any:
        """
        Allow the chain to be called like a function.
        """
        return self.run(inputs)
