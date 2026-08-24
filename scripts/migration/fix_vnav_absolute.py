import re

with open('content/SP2026-VNAV-CourseContent/index.md', 'r') as f:
    text = f.read()

base_url = "https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent"

# Replace links with full external absolute links to bypass crawl-links lowercasing
text = text.replace("/SP2026-VNAV-CourseContent/lectures/index.md", f"{base_url}/lectures/")
text = text.replace("/SP2026-VNAV-CourseContent/labs/index.md", f"{base_url}/labs/")
text = text.replace("/SP2026-VNAV-CourseContent/notes/index.md", f"{base_url}/notes/")
text = text.replace("/SP2026-VNAV-CourseContent/%20misc/index.md", f"{base_url}/%20misc/")
text = text.replace("/SP2026-VNAV-CourseContent/Final%20Project%20+%20exam/index.md", f"{base_url}/Final%20Project%20+%20exam/")

with open('content/SP2026-VNAV-CourseContent/index.md', 'w') as f:
    f.write(text)
