import re

with open('content/index.md', 'r') as f:
    text = f.read()

replacements = {
    "hardware": "initial setup/hardware.md",
    "VESC aka FSEC": "initial setup/VESC aka FSEC.md",
    "YDLidar X4 Pro and 435i realsense": "initial setup/YDLidar X4 Pro and 435i realsense.md",
    "Calibrating your car": "initial setup/Calibrating your car.md",
    "Fusing sensors with robot_localization": "waypointer/guides/Fusing sensors with robot_localization.md",
    "Pairing": "initial setup/Pairing.md",
    "arcpro run commands | Sensor and motor drive commands": "initial setup/arcpro run commands.md",
    "arcpro waypointer example run | Example waypointing run commands": "waypointer/arcpro waypointer example run.md",
    "Running the Sim and sim2real": "passive reinforcement learning/Running the Sim and sim2real.md",
    "arcpro waypointer example run | waypointer": "waypointer/arcpro waypointer example run.md",
    "index": "initial setup/index.md",
    "arcpro run commands": "initial setup/arcpro run commands.md",
    "arcpro waypointer example run": "waypointer/arcpro waypointer example run.md",
    "original docs": "initial setup/original docs.md",
    "Using nav2 with slamtoolbox": "waypointer/guides/Using nav2 with slamtoolbox.md",
}

for wikilink, target in replacements.items():
    if " | " in wikilink:
        display_text = wikilink.split(" | ")[1]
    else:
        display_text = wikilink
        
    url = target.replace(" ", "%20")
    text = text.replace(f"[[{wikilink}]]", f"[{display_text}]({url})")

with open('content/index.md', 'w') as f:
    f.write(text)

