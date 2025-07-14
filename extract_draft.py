import json
import re
import os
from pathlib import Path


def extract_draft_to_markdown(
    json_file_path="data/run_data/results.json", output_file_path=None
):
    """
    Extract draft content from JSON file and save as markdown file.

    Args:
        json_file_path (str): Path to the JSON file containing the draft
        output_file_path (str): Path for the output markdown file (optional)

    Returns:
        str: Path to the created markdown file
    """
    try:
        # Load the JSON file
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract the draft content
        draft = data.get("draft", {})
        title = draft.get("title", "Untitled")
        description = draft.get("description", "No description")
        content = draft.get("content", "")

        # Replace literal \n with actual newlines
        content = content.replace("\\n", "\n")

        # Fix any double newlines that might have been created
        content = re.sub(r"\n\n\n+", "\n\n", content)

        # Create output filename if not provided
        if output_file_path is None:
            # Create filename from title (sanitize for filesystem)
            filename = re.sub(r"[^\w\s-]", "", title)
            filename = re.sub(r"[-\s]+", "-", filename)
            filename = filename.strip("-")
            output_file_path = f"data/{filename}.md"

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Save the markdown file
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(f"# {title}\n\n")
            file.write(f"## {description}\n\n")
            file.write(f"###########################\n\n")
            file.write(content)

        print(f"✅ Draft extracted and saved to: {output_file_path}")
        print(f"📄 Title: {title}")
        print(f"📊 Content length: {len(content)} characters")

        return output_file_path

    except FileNotFoundError:
        print(f"❌ Error: JSON file not found at {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in {json_file_path}")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def validate_markdown(file_path):
    """
    Validate that the markdown file was created correctly.

    Args:
        file_path (str): Path to the markdown file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Basic validation checks
        has_title = content.startswith("#")
        has_headers = "##" in content
        has_links = "[" in content and "]" in content
        has_paragraphs = "\n\n" in content

        print(f"\n📋 Markdown Validation for {file_path}:")
        print(f"   • Has title (starts with #): {'✅' if has_title else '❌'}")
        print(f"   • Has headers (##): {'✅' if has_headers else '❌'}")
        print(f"   • Has links: {'✅' if has_links else '❌'}")
        print(f"   • Has proper paragraphs: {'✅' if has_paragraphs else '❌'}")
        print(f"   • File size: {len(content)} characters")

        return True

    except Exception as e:
        print(f"❌ Validation error: {str(e)}")
        return False


if __name__ == "__main__":
    # Run the extraction
    output_path = extract_draft_to_markdown()

    # Validate the output if successful
    if output_path:
        validate_markdown(output_path)
