import os
import re

content_dir = "content/SP2026-VNAV-CourseContent"

def slugify(text):
    # This is a basic simulation of Quartz's slugify
    text = text.lower()
    text = text.replace("%20", "-")
    text = text.replace(" ", "-")
    text = text.replace("+", "-")
    text = text.replace("&", "-")
    text = re.sub(r'-+', '-', text)
    return text

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if not file.endswith(".md"):
            continue
            
        filepath = os.path.join(root, file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We need to find all https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/... links
        # and replace them with the slugified version
        
        def repl(match):
            url = match.group(0)
            prefix = "https://airou-lab.github.io/general_wiki_website/"
            if not url.startswith(prefix):
                return url
                
            path = url[len(prefix):]
            parts = path.split("/")
            
            # Slugify all parts EXCEPT the filename!
            # Wait, actually Quartz lowercases the filename too for assets! 
            # I checked public/sp2026-vnav-coursecontent/-misc/cs4733_5733_fall2025_syllabus.pdf
            # Yes! The filename is lowercased too!
            
            slugified_parts = []
            for part in parts:
                if part:
                    slugified_parts.append(slugify(part))
                    
            new_path = "/".join(slugified_parts)
            return prefix + new_path
            
        new_content = re.sub(r'https://airou-lab\.github\.io/general_wiki_website/SP2026-VNAV-CourseContent/[^\s"<>]+', repl, content)
        
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
