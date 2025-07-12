from langchain_core.prompts import PromptTemplate

# Example refine topic prompt (customize as needed)
refine_topic_prompt = PromptTemplate(
    template="""You are an expert content strategist helping to refine a broad topic into a focused, engaging article angle.
Your task:
Given the broad topic {topic} and target keywords {keywords}, develop focused angles that would resonate with our target audience while aligning with UnrealCRM's mission. Consider current trends, common customer questions and problem they run into, and competitive differentiation when developing angles.

Requirements:
1. Each angle must be specific enough to cover in one article (800-2000 words)
2. Must be relevant to our target audience's pain points or interests
3. Should showcase UnrealCRM's expertise or value proposition
4. Must be actionable or provide clear value to readers
5. Should naturally incorporate the provided keywords

## DO NOT DEVIATE FROM THE OUTPUT FORMAT
Output format:
{{
  "angles_considered": [
    {{
      "angle": "Specific angle description",
      "rationale": "Why this angle works for our audience",
      "scope": "What this article would cover"
    }}
  ],
  "refined_topic": "One clear, focused sentence describing the chosen angle",
 "primary_keyword": "Main keyword to optimize for",
  "secondary_keywords": ["Additional keywords to include"]
}}

{format_instructions}""",
    input_variables=["topic", "keywords", "format_instructions"],
)
