import re

with open('content/index.md', 'r') as f:
    text = f.read()

# I want to fix `[[VESC aka FSEC]]` to correctly point to `initial setup/VESC aka FSEC.md`
# Because it's breaking. I'll just change wikilinks in index.md to use standard markdown links
# that actually point to the correct file relative to `content/` root.

# Actually, wait... the user's issue with VESC aka FSEC is that `crawl-links` lowercased it 
# but DIDN'T PREPEND the subfolder!
# The file is in `content/initial setup/VESC aka FSEC.md`.
# Let's fix the links manually in index.md to be sure they are correct.
