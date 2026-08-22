import re

with open('content/SP2026-VNAV-CourseContent/labs/index.md', 'r') as f:
    text = f.read()

# Replace spaces in the markdown link URLs
def replacer(match):
    text_part = match.group(1)
    url_part = match.group(2)
    url_part = url_part.replace(' ', '%20')
    return f"[{text_part}]({url_part})"

text = re.sub(r'\[(.*?)\]\((.*?\.md)\)', replacer, text)

with open('content/SP2026-VNAV-CourseContent/labs/index.md', 'w') as f:
    f.write(text)

