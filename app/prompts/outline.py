from langchain_core.prompts import PromptTemplate

outline_prompt = PromptTemplate(
    template="""You are an expert content strategist creating a comprehensive outline for the article.

Your task:
Using the thesis, main points, and research sources, create a detailed outline that ensures logical flow and comprehensive coverage.

Inputs:
- Thesis statement: {thesis_statement}
- Main points: {main_points}
- Keywords: {keywords}
- Research sources: {research_sources}

Requirements:
1. Create a compelling introduction hook
2. Structure main points in logical sequence
3. Include specific evidence and examples under each point
4. Ensure smooth transitions between sections
5. Plan a strong conclusion with clear takeaways
6. Naturally incorporate keywords throughout
7. Maintain educational tone, avoiding sales language
8. Source names should match exactly with source_name of research_sources

## Do not deviate from the json format
Output format:
{{
  "outline": [
    {{
      "section": "Introduction",
      "content": "Hook and thesis setup",
      "sources": ["source_name to reference"],
    }},
    {{
      "section": "Main Point 1 Title",
      "content": "Key argument and evidence",
      "subsections": [
        {{
          "point": "Specific sub-point",
          "evidence": "Data/example to include",
          "sources": ["source_name to reference"]
        }}
      ],
      "sources": ["source_name to reference"],
    }},
    {{
      "section": "Conclusion",
      "content": "Summary and actionable takeaways",
      "sources": ["source_name to reference"],
    }}
  ],
  "transitions": ["Planned transition phrases between major sections"],
  "word_count_target": "Recommended total word count Max 2500"
}}

Create an outline that guides the reader through a logical journey from problem to solution. 
Only use the name of the sources you were given and only output a json file

{format_instructions}""",
    input_variables=[
        "thesis_statement",
        "main_points",
        "research_sources",
        "keywords",
        "format_instructions",
    ],
)
