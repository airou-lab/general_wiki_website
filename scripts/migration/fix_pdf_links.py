import os
import re

base_dir = "content/SP2026-VNAV-CourseContent"
folders = ["lectures", "notes", " misc", "Final Project + exam"]

base_url = "https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent"

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    index_path = os.path.join(folder_path, "index.md")
    
    if not os.path.exists(index_path):
        continue
        
    with open(index_path, "r") as f:
        lines = f.readlines()
        
    with open(index_path, "w") as f:
        for line in lines:
            # Look for lines like - [filename.pdf](./filename.pdf)
            m = re.match(r'^- \[(.*?)\]\(\./(.*?)\)', line)
            if m:
                filename = m.group(1)
                # Note: folder might be " misc" which we need to urlencode as "%20misc"
                # but let's just use replace space with %20
                folder_url = folder.replace(" ", "%20")
                file_url = filename.replace(" ", "%20")
                full_url = f"{base_url}/{folder_url}/{file_url}"
                f.write(f"- [{filename}]({full_url})\n")
            elif "Test PDF" in line:
                continue # remove test lines
            else:
                f.write(line)

