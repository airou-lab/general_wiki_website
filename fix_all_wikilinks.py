import os
import re
import urllib.parse

content_dir = os.path.abspath("content")

# 1. Build a registry of all markdown files
# Map lowercase filename (without .md) to its absolute path
registry = {}
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            abs_path = os.path.join(root, file)
            basename = file[:-3]
            registry[basename.lower()] = abs_path
            # Also register the full relative path from content, just in case
            rel_from_content = os.path.relpath(abs_path, content_dir)
            registry[rel_from_content.lower()[:-3]] = abs_path

# 2. Iterate through all markdown files and fix wikilinks
wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')

def process_file(filepath):
    with open(filepath, 'r') as f:
        text = f.read()

    def repl(match):
        inner = match.group(1).strip()
        
        # Split alias
        if '|' in inner:
            target, alias = inner.split('|', 1)
            target = target.strip()
            alias = alias.strip()
        else:
            target = inner
            alias = target
            
        target_lower = target.lower()
        
        if target_lower in registry:
            target_abs = registry[target_lower]
            # Calculate relative path from current file's directory to target file
            current_dir = os.path.dirname(filepath)
            rel_path = os.path.relpath(target_abs, current_dir)
            
            # URL encode spaces and special characters for markdown links
            # We must use forward slashes even on Windows for web links
            rel_path = urllib.parse.quote(rel_path.replace('\\', '/'))
            
            return f"[{alias}]({rel_path})"
        
        # If not found in registry, leave it as is or try to guess
        return match.group(0)

    new_text = wikilink_pattern.sub(repl, text)
    
    if new_text != text:
        with open(filepath, 'w') as f:
            f.write(new_text)
            
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))

