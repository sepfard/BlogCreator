from langchain_core.prompts import PromptTemplate

# Research sources prompt template
research_sources_prompt = PromptTemplate(
    template="""CRITICAL: Return ONLY valid JSON. Do not provide any conversational text, explanations, or descriptions. Just return the JSON object.

Your task:
Given the refined topic "{refined_topic}" and keywords "{keywords}", create a thorough research plan that will provide authoritative, credible information for the article.

Requirements:
1. Identify high-quality sources across different categories
2. Avoid using direct competitors as primary sources when possible
3. Focus on academic papers, industry reports, expert blogs, case studies, and authoritative publications
4. Ensure sources provide diverse perspectives and comprehensive coverage
5. Include both foundational knowledge and recent developments
6. Every source should have a valid link

Source categories to consider:
- Academic/research papers
- Industry reports and whitepapers
- Expert interviews or quotes
- Case studies and real-world examples
- Government or regulatory sources
- Thought leadership articles (non-competitive)
- Data and statistics sources
- Technical documentation

REQUIRED JSON FORMAT (return exactly this structure):
{{
  "research_sources": [
    {{
      "source_name": "Name of source",
      "category": "Source category (e.g., Academic, Industry Report, Case Study)",
      "relevance": "Why this source matters for our topic",
      "key_questions": ["What specific information to extract"],
      "url": "Link for the source"
    }}
  ],
}}

REMEMBER: Return ONLY the JSON object. No explanatory text before or after the JSON.

{format_instructions}""",
    input_variables=["refined_topic", "keywords", "format_instructions"],
)
