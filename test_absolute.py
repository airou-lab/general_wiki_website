with open('content/archived_material/index.md', 'r') as f:
    text = f.read()
text = text.replace("[BluetoothController](./ROS1_arc_pro/misc/bluetoothController.md)", "[BluetoothController](/general_wiki_website/archived_material/ROS1_arc_pro/misc/bluetoothController)")
with open('content/archived_material/index.md', 'w') as f:
    f.write(text)
