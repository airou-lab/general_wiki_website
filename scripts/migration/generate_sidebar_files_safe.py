import os
import glob
import urllib.parse

base_dir = "content/SP2026-VNAV-CourseContent"
folders = ["lectures", "notes", " misc", "Final Project + exam"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    
    if not os.path.exists(folder_path):
        continue
        
    # Delete old .pdf.md and .pptx.md files
    for f in glob.glob(os.path.join(folder_path, "*.md")):
        if f.endswith(".pdf.md") or f.endswith(".pptx.md") or f.endswith(".ppt.md"):
            os.remove(f)
            
    # Get all PDF and PPTX files
    files = [f for f in os.listdir(folder_path) if (f.endswith(".pdf") or f.endswith(".pptx") or f.endswith(".ppt")) and os.path.isfile(os.path.join(folder_path, f))]
    
    # Create a safe markdown file for each to make them show up in the sidebar
    for file in files:
        md_file = file + "_viewer.md"
        md_path = os.path.join(folder_path, md_file)
        
        file_url = urllib.parse.quote(file)
        
        with open(md_path, "w") as f:
            f.write(f"---\ntitle: {file}\n---\n\n")
            f.write(f"# {file}\n\n")
            f.write(f"[{file}](./{file_url}) (Download / Open)\n\n")
            
            if file.endswith(".pdf"):
                f.write(f'<iframe src="./{file_url}" width="100%" height="800px" style="border: none;"></iframe>\n')

