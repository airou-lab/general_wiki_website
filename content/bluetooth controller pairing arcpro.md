---
Type:
  - arcProDocs
Labs:
  - AIROU
---
> [!Warning] repository Issue
    > Due to the current repo not being finished, please use deprcated repo to launch teleop found [here](https://github.com/louis6962/Vnavros2setup). We will hopefully have the new repo updated to include the teleop nodes.

# Bluetooth repairing  
 1) Enter `bluetoothctl` in terminal  
 2) Press the center bottom button and the share button at same time for around 5 seconds until lighbar rapidly flashes  
 3) Enter "scan on" in bluetoothctl and find the wireless controller. Example:     (Note that there may be multiple wireless controllers in room you may need to trial and error and unpair), Additionally may need to repeat step 2 if pairing mode on controller stops early  

```bash
[bluetooth]# [CHG] Device BB:8E:41:F5:5D:C7 Name: Wireless Controller  
[bluetooth]# [CHG] Device BB:8E:41:F5:5D:C7 Alias: Wireless Controller  
```

  
## Pair/trust/&connect with wireless controller. Example:  
```bash
[bluetooth]# pair BB:8E:41:F5:5D:C7  
[bluetooth]# trust BB:8E:41:F5:5D:C7  
[bluetooth]# connect BB:8E:41:F5:5D:C7  
```

# Running teleop
```bash
#Bringup vesc:
ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false

# Launch teleop
ros2 launch launches teleop.launch.py joy_dev:=ttyUSB0
```

Note note you may need to install several missing dependencies, if so follow the command below
```bash
source /opt/ros/jazzy/setup.bash  
rosdep update  
rosdep install --from-paths src --ignore-src -r -y || true  
sudo apt install -y ros-jazzy-asio-cmake-module ros-jazzy-io-context ros-jazzy-serial-driver  
```