import os
import glob
import urllib.parse

base_dir = "content/SP2026-VNAV-CourseContent"
folders = ["lectures", "notes", " misc", "Final Project + exam"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    
    if not os.path.exists(folder_path):
        continue
        
    # Get all PDF and PPTX files
    files = [f for f in os.listdir(folder_path) if (f.endswith(".pdf") or f.endswith(".pptx") or f.endswith(".ppt")) and os.path.isfile(os.path.join(folder_path, f))]
    
    # Create a markdown file for each to make them show up in the sidebar
    for file in files:
        md_file = file + ".md"
        md_path = os.path.join(folder_path, md_file)
        
        # We need a relative path from this md file to the actual asset
        # Since they are in the same directory, it's just the filename
        # But we must URL encode it for the link
        file_url = urllib.parse.quote(file)
        
        with open(md_path, "w") as f:
            # The title will be the filename, which makes it look nice in the sidebar
            f.write(f"---\ntitle: {file}\n---\n\n")
            f.write(f"# {file}\n\n")
            f.write(f"[{file}](.m/{file_url}) (Download / Open)\n\n")
            
            if file.endswith(".pdf"):
                # Use standard markdown image syntax which Quartz might intercept, 
                # or just use an iframe pointing to the relative file
                f.write(f'<iframe src="./{file_url}" width="100%" height="800px" style="border: none;"></iframe>\n')

