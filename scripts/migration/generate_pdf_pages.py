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
        
    # Get all PDF and PPTX files in the directory
    files = [f for f in os.listdir(folder_path) if (f.endswith(".pdf") or f.endswith(".pptx") or f.endswith(".ppt")) and os.path.isfile(os.path.join(folder_path, f))]
    files.sort()
    
    # Generate a Markdown page for each file
    for file in files:
        md_file = file + ".md"
        md_path = os.path.join(folder_path, md_file)
        
        folder_url = folder.replace(" ", "%20")
        file_url = file.replace(" ", "%20")
        full_url = f"{base_url}/{folder_url}/{file_url}"
        
        with open(md_path, "w") as mf:
            mf.write(f"---\ntitle: {file}\n---\n\n")
            mf.write(f"[{file}]({full_url}) (Download/Open Full Screen)\n\n")
            mf.write(f'<iframe src="{full_url}" width="100%" height="800px" style="border: none;"></iframe>\n')

    # Update index.md to point to the new Markdown pages
    with open(index_path, "w") as f:
        title = folder.strip()
        f.write(f"---\ntitle: {title}\n---\n\n")
        f.write(f"# {title}\n\n")
        for file in files:
            md_file = file + ".md"
            f.write(f"- [{file}]({md_file.replace(' ', '%20')})\n")

