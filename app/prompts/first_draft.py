from langchain_core.prompts import PromptTemplate

first_draft_prompt = PromptTemplate(
    template="""
You are an expert content writer creating the first draft of an article.

Your task:
Using the detailed outline, write a complete first draft that brings the research and structure to life.

Inputs:
- Detailed outline: {outline}
- Content style: {content_style}
- Reader takeaway: {reader_takeaway}
- Keywords: {keywords}
- Word Count Target: {word_count_target}

Requirements:
1. Follow the outline structure closely
2. Write in a conversational, engaging tone
3. Integrate research naturally without over-citing
4. Use storytelling and examples to illustrate points
5. Include keywords organically (no keyword stuffing)
6. Maintain educational focus throughout
7. Keep paragraphs concise (3-5 sentences)
8. Use subheadings to improve readability
9. Don't worry about perfection - focus on getting ideas down
10. Use bullet points and numbered lists sparingly if needed
11. Include useful supporting links embedded in relevant words in places across the article in .md format with the link included

Output format:
{{
  "draft": {{
    "title": "Compelling article title",
    "content": "Full article text with proper .md formatting"
    "description": "1 sentence description of the article in concise terms for SEO"
  }},
  "writer_notes": ["Any concerns or areas that need improvement in revision"]
}}

Write fluidly and naturally, focusing on providing value to the reader. Remember: this is a first draft - perfection comes in revision.

{format_instructions}
""",
    input_variables=[
        "outline",
        "content_style",
        "reader_takeaway",
        "keywords",
        "word_count_target",
        "format_instructions",
    ],
)
