import re

with open('content/SP2026-VNAV-CourseContent/index.md', 'r') as f:
    text = f.read()

# Replace links
text = text.replace("lectures/index.md", "./lectures/index.md")
text = text.replace("labs/index.md", "./labs/index.md")
text = text.replace("notes/index.md", "./notes/index.md")
text = text.replace("%20misc/index.md", "./%20misc/index.md")
text = text.replace("Final%20Project%20+%20exam/index.md", "./Final%20Project%20+%20exam/index.md")

with open('content/SP2026-VNAV-CourseContent/index.md', 'w') as f:
    f.write(text)
