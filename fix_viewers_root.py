import os
import re

content_dir = "content/SP2026-VNAV-CourseContent"

updated_files = 0
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if not file.endswith(".md"):
            continue
            
        filepath = os.path.join(root, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace occurrences of (/general_wiki_website/...) or src="/general_wiki_website/..."
        # with (/...) and src="/..."
        new_content = re.sub(r'(\(|src=")/general_wiki_website/', r'\1/', content)
        
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
            updated_files += 1

print(f"Total files updated: {updated_files}")
