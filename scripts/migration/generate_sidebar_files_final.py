import os
import glob
import urllib.parse

base_dir = "content/SP2026-VNAV-CourseContent"
folder_slugs = {
    "lectures": "lectures",
    "notes": "notes",
    " misc": "-misc",
    "Final Project + exam": "Final-Project-+-exam"
}

for folder, slug in folder_slugs.items():
    folder_path = os.path.join(base_dir, folder)
    
    if not os.path.exists(folder_path):
        continue
        
    # Get all PDF and PPTX files
    files = [f for f in os.listdir(folder_path) if (f.endswith(".pdf") or f.endswith(".pptx") or f.endswith(".ppt")) and os.path.isfile(os.path.join(folder_path, f))]
    
    # Update the safe markdown files
    for file in files:
        md_file = file + "_viewer.md"
        md_path = os.path.join(folder_path, md_file)
        
        file_url = urllib.parse.quote(file)
        full_url = f"/general_wiki_website/SP2026-VNAV-CourseContent/{slug}/{file_url}"
        
        with open(md_path, "w") as f:
            f.write(f"---\ntitle: {file}\n---\n\n")
            f.write(f"# {file}\n\n")
            f.write(f"[{file}]({full_url}) (Download / Open)\n\n")
            
            if file.endswith(".pdf"):
                f.write(f'<iframe src="{full_url}" width="100%" height="800px" style="border: none;"></iframe>\n')

