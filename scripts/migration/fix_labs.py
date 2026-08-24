import re

with open('content/SP2026-VNAV-CourseContent/labs/index.md', 'r') as f:
    text = f.read()

# Replace [[Lab 1 - Exercises|Lab 1: Git, Environment Setup & Shells]]
# with [Lab 1: Git, Environment Setup & Shells](Lab 1 - Exercises.md)
# The regex looks for [[filename|text]]
text = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'[\2](\1.md)', text)

with open('content/SP2026-VNAV-CourseContent/labs/index.md', 'w') as f:
    f.write(text)

