from langchain_core.prompts import PromptTemplate

key_message_prompt = PromptTemplate(
    template="""
You are an expert content strategist defining the core message and structure for an article.

Your task:
Given the refined topic "{refined_topic}" and keywords "{keywords}", establish a clear thesis and supporting points that will guide the article.

Requirements:
1. Create a compelling, specific thesis statement (1 sentence)
2. Identify 3-5 main points that strongly support the thesis
3. Ensure each point provides unique value without overlap
4. Make the message actionable and relevant to the target audience
5. Naturally incorporate the target keywords into the messaging
6. Focus on educational value first - this should feel like genuine thought leadership, not a sales pitch
7. Any UnrealCRM mentions should be subtle, contextual examples rather than promotional

CRITICAL: Return ONLY valid JSON. Do not provide any conversational text, explanations, or descriptions. Just return the JSON object.

Output format:
{{
  "thesis_statement": "One clear sentence that captures the article's core argument",
  "main_points": [
    {{
      "point": "Main point description",
      "value_prop": "What readers gain from this point",
      "evidence_needed": "Type of proof/data to support this",
      "unrealcrm_angle": "Optional: Subtle way to weave in relevant UnrealCRM context if natural"
    }}
  ],
  "reader_takeaway": "What readers should remember and be able to do after reading",
  "content_style": "Educational and value-first approach notes",
  "cta_direction": "Soft, value-driven call-to-action that helps readers take next steps"
}}

Remember: The best content marketing teaches first and sells second. Focus on solving reader problems.

{format_instructions}""",
    input_variables=["refined_topic", "keywords", "format_instructions"],
)
