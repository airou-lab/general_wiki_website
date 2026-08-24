import os
import glob
import urllib.parse

base_dir = "content/SP2026-VNAV-CourseContent"
folders = ["lectures", "notes", " misc", "Final Project + exam"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    index_path = os.path.join(folder_path, "index.md")
    
    if not os.path.exists(index_path):
        continue
        
    # Get all PDF and PPTX files
    files = [f for f in os.listdir(folder_path) if (f.endswith(".pdf") or f.endswith(".pptx") or f.endswith(".ppt")) and os.path.isfile(os.path.join(folder_path, f))]
    files.sort()
    
    with open(index_path, "w") as f:
        title = folder.strip()
        f.write(f"---\ntitle: {title}\n---\n\n")
        f.write(f"# {title}\n\n")
        
        for file in files:
            file_url = urllib.parse.quote(file)
            full_url = f"./{file_url}"
            
            f.write(f"## {file}\n\n")
            f.write(f"[{file}]({full_url}) (Download / Open Full Screen)\n\n")
            if file.endswith(".pdf"):
                f.write(f'<iframe src="{full_url}" width="100%" height="600px" style="border: none; margin-bottom: 40px;"></iframe>\n\n')

