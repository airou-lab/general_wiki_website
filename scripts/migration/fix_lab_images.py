import os
import re

labs_dir = "content/SP2026-VNAV-CourseContent/labs"

base_url = "https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media"

for file in os.listdir(labs_dir):
    if not file.endswith(".md"):
        continue
    filepath = os.path.join(labs_dir, file)
    with open(filepath, "r") as f:
        text = f.read()
    
    # Replace ![[filename.ext]] with ![filename.ext](base_url/filename.ext)
    # The regex looks for ![[filename.ext]]
    def replacer(match):
        filename = match.group(1)
        file_url = filename.replace(" ", "%20")
        if not filename:
            return ""
        return f"![{filename}]({base_url}/{file_url})"
        
    text = re.sub(r'!\[\[(.*?\.png|.*?\.jpg|.*?\.JPG|.*?\.gif)\]\]', replacer, text)
    
    with open(filepath, "w") as f:
        f.write(text)

