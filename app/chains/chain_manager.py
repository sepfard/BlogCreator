from typing import Dict, Any
from .refine_topic_chain import RefineTopicChain
from .research_source_chain import ResearchSourceChain
from app.models.anthropic_model import AnthropicModel
import json


class ChainManager:
    """
    Simplified chain manager for BlogCreator application.
    Manages specific chains using langchain components.
    """

    def __init__(self):
        self.chains = {}

    def register_chain(self, name: str, chain_instance):
        """Register a chain instance with a given name."""
        self.chains[name] = chain_instance

    def run_chain(self, name: str, inputs: Dict[str, Any], as_json: bool = True) -> Any:
        """
        Run a registered chain with given inputs.

        Args:
            name: The name of the chain to run
            inputs: Dictionary of inputs for the chain
            as_json: Whether to return output as JSON string

        Returns:
            Chain output as JSON string or raw output
        """
        if name not in self.chains:
            raise ValueError(f"Chain '{name}' is not registered.")

        chain = self.chains[name]
        output = chain.run(inputs)

        if as_json:
            try:
                return json.dumps(output, indent=2)
            except TypeError:
                # If output is not serializable, return as string
                return json.dumps({"result": str(output)}, indent=2)
        return output

    def list_chains(self):
        """List all registered chains."""
        return list(self.chains.keys())

    def setup_refine_topic_chain(
        self, model_name: str = "claude-sonnet-4-20250514", verbose: bool = False
    ):
        """
        Set up the refine topic chain with Anthropic model.

        Args:
            model_name: Anthropic model name (default: claude-sonnet-4-20250514)
            verbose: Whether to enable verbose logging
        """
        model = AnthropicModel(model_name=model_name)
        refine_chain = RefineTopicChain(model=model, verbose=verbose)
        self.register_chain("refine_topic", refine_chain)
        return refine_chain

    def setup_research_source_chain(
        self,
        model_name: str = "claude-sonnet-4-20250514",
        verbose: bool = False,
        enable_web_search: bool = True,
    ):
        """
        Set up the research source chain with Anthropic model and optional web search.

        Args:
            model_name: Anthropic model name (default: claude-sonnet-4-20250514)
            verbose: Whether to enable verbose logging
            enable_web_search: Whether to enable web search capabilities (default: True)
        """
        model = AnthropicModel(
            model_name=model_name, enable_web_search=enable_web_search
        )
        research_chain = ResearchSourceChain(
            model=model, verbose=verbose, enable_web_search=enable_web_search
        )
        self.register_chain("research_sources", research_chain)
        return research_chain

    def run_full_pipeline(
        self,
        topic: str,
        keywords: list,
        model_name: str = "claude-sonnet-4-20250514",
        verbose: bool = False,
        enable_web_search: bool = True,
    ):
        """
        Run the complete pipeline: topic refinement -> research source generation.

        Args:
            topic: The broad topic to refine
            keywords: List of keywords to focus on
            model_name: Anthropic model name to use
            verbose: Whether to enable verbose logging
            enable_web_search: Whether to enable web search for research sources (default: True)

        Returns:
            Dict containing results from both chains
        """
        # Set up both chains
        self.setup_refine_topic_chain(model_name, verbose)
        self.setup_research_source_chain(model_name, verbose, enable_web_search)

        # Run refine topic chain
        refine_inputs = {"topic": topic, "keywords": keywords}
        refine_result = self.run_chain("refine_topic", refine_inputs, as_json=False)

        # Use refined topic and keywords for research source generation
        research_inputs = {
            "refined_topic": refine_result["refined_topic"],
            "keywords": refine_result["secondary_keywords"],
        }
        research_result = self.run_chain(
            "research_sources", research_inputs, as_json=False
        )

        return {
            "refine_topic_result": refine_result,
            "research_sources_result": research_result,
        }
