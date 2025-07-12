import json
import os

def load_json_file(filename):
    """Load JSON data from file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filename, data):
    """Save JSON data to file with proper formatting"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_source_mapping(sources_data):
    """Create a mapping from source names to URLs and relevance"""
    source_mapping = {}
    for source in sources_data['research_sources']:
        source_mapping[source['source_name']] = {
            'url': source['url'],
            'relevance': source['relevance']
        }
    return source_mapping

def update_outline_with_urls(outline_data, source_mapping):
    """Update outline sections with source URLs and relevance"""
    for section in outline_data['outline']:
        if 'supporting_sources' in section:
            # Create a new field for source URLs and relevance
            section['source_urls'] = []
            
            for source_name in section['supporting_sources']:
                if source_name in source_mapping:
                    section['source_urls'].append({
                        'source_name': source_name,
                        'url': source_mapping[source_name]['url'],
                        'relevance': source_mapping[source_name]['relevance']
                    })
                else:
                    # If source not found, add it with a note
                    section['source_urls'].append({
                        'source_name': source_name,
                        'url': 'URL not found in sources.json',
                        'relevance': 'Relevance not found in sources.json'
                    })
        
        # Also handle subsections if they exist
        if 'subsections' in section:
            for subsection in section['subsections']:
                if 'source' in subsection:
                    source_name = subsection['source']
                    if source_name in source_mapping:
                        subsection['source_url'] = source_mapping[source_name]['url']
                        subsection['source_relevance'] = source_mapping[source_name]['relevance']
                    else:
                        subsection['source_url'] = 'URL not found in sources.json'
                        subsection['source_relevance'] = 'Relevance not found in sources.json'
    
    return outline_data

def main():
    # Load the JSON files
    try:
        outline_data = load_json_file('outline.json')
        sources_data = load_json_file('sources.json')
        
        print("Loaded outline.json and sources.json successfully")
        
        # Create source name to URL and relevance mapping
        source_mapping = create_source_mapping(sources_data)
        print(f"Created mapping for {len(source_mapping)} sources")
        
        # Update outline with URLs and relevance
        updated_outline = update_outline_with_urls(outline_data, source_mapping)
        
        # Save the updated outline
        save_json_file('outline_with_urls_and_relevance.json', updated_outline)
        print("Updated outline saved to outline_with_urls_and_relevance.json")
        
        # Print a summary of matches
        print("\nSource matching summary:")
        for section in updated_outline['outline']:
            if 'source_urls' in section:
                print(f"\nSection: {section['section']}")
                for source_url in section['source_urls']:
                    status = "✓" if source_url['url'] != 'URL not found in sources.json' else "✗"
                    print(f"  {status} {source_url['source_name']}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 