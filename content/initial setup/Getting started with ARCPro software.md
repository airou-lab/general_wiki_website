---
title: "Getting Started with ARCPro Software"
tags:
  - arcProDocs
  - setup
  - software
---

# Getting Started with ARCPro Software

> [!info] ARC Pro Student Onboarding: Step 3 of 5
> Previous: [[Pairing|Step 2: Gamepad Controller Pairing]]. Next: [[YDLidar X4 Pro and 435i realsense|Step 4: Sensor Verification]].

> [!important] ARC Pro Fleet Robots Come Pre-Configured
> If you are working on an ARC Pro lab car (e.g. Car 2 through Car 11), the entire `~/arcpro_system` software stack is **already cloned, configured, and built** on the robot.
>
> **Prerequisites Checklist**:
> 1. You must be remoted into your robot (completed in [[Remote Connection|Step 1: Connecting Remotely]]). All commands in this guide must be typed **inside the robot's remote terminal**, not on your personal laptop.
> 2. Ensure your controller was paired (completed in [[Pairing|Step 2: Controller Pairing]]).
>
> You **do not** need to re-clone the repository or compile from scratch. Proceed directly to **[[#1. First Drive & Teleoperation|Section 1: First Drive & Teleoperation]]**!

---

## 1. First Drive & Teleoperation

Verify that the VESC motor controller and steering servo respond properly to manual inputs before running autonomous code.

### Option A: Using Turnkey Terminal Aliases (Recommended)
On ARC Pro robots, turnkey convenience aliases are pre-configured in your shell:

```bash
# 1. Gamepad Teleoperation (Hold L1/LB deadman + Left Stick throttle + Right Stick steer)
teleop

# 2. Interactive Keyboard Teleoperation (drive using i/j/k/l keys in terminal)
teleop_key

# 3. Quick Drivetrain Verification (drives forward at 0.4 m/s, Ctrl+C stops safely)
move_forward   # (or: straight)
```

> [!tip] Driving Controls
> - **Deadman Switch**: Hold down `L1` or `LB` on your gamepad while moving the sticks. If released, the robot stops immediately.
> - **Left Thumbstick**: Forward / Reverse throttle.
> - **Right Thumbstick**: Left / Right steering angle.
> - **Emergency Stop**: Press `Ctrl + C` in the terminal at any time.

### Option B: Using Direct ROS 2 Launch Commands

If you prefer launching individual ROS 2 nodes manually across terminals:

```bash
# Terminal 1: Launch the VESC hardware driver & odometry publisher
ros2 launch f1tenth_teleop vesc.launch.py

# Terminal 2: Launch teleop node and joystick interface
ros2 launch f1tenth_teleop teleop.launch.py joy_dev:=/dev/input/js0
```

### Option C: Testing Direct Drive Messages (Without Gamepad)
You can test the drivetrain directly from the command line by publishing an `AckermannDriveStamped` message:

```bash
ros2 topic pub /ackermann_cmd ackermann_msgs/msg/AckermannDriveStamped \
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
  drive: {steering_angle: 0.0, speed: 0.4}}' -r 10
```

---

## 2. Verifying Your Robot Workspace

On fleet cars, the workspace resides in `/home/arc/arcpro_system`. Both ROS 2 Jazzy and the workspace overlay are automatically sourced in `~/.bashrc`.

To verify your workspace is ready:

```bash
cd ~/arcpro_system
ls -la install/
```

You should see build overlays for `f1tenth_stack`, `vesc`, `f1tenth_teleop`, `twist_to_ackermann`, and `ydlidar_ros2_driver`.

If opening a non-standard terminal or subshell, source the environment manually:
```bash
source /opt/ros/jazzy/setup.bash
source ~/arcpro_system/install/setup.bash
```

---

## 3. Rebuilding Code (When Making Modifications)

You only need to rebuild the workspace if you edit source code (e.g. implementing custom controllers) or modify configuration files (such as vehicle calibration parameters in [[Tuning Guide|Step 5: Tuning Guide]]):

```bash
cd ~/arcpro_system

# Rebuild all packages
colcon build --symlink-install

# Or rebuild a specific package
colcon build --symlink-install --packages-select f1tenth_stack
source install/setup.bash
```

---

## 4. Testing Onboard Sensors & Cameras

Before heading to the track, run a quick check on the primary sensors. Step 4 covers in-depth sensor configuration:

### Intel RealSense D435i Camera
```bash
# Launch camera node with 3D point cloud enabled
ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true

# In a separate terminal, verify camera topics:
ros2 topic list | grep camera
```
You should see `/camera/camera/color/image_raw` and `/camera/camera/depth/color/points`.

### YDLidar X4 Pro (2D LiDAR)
```bash
# Launch LiDAR driver
ros2 launch ydlidar_ros2_driver ydlidar_launch.py sim:=false

# In a separate terminal, verify laser scan:
ros2 topic echo /scan --once
```

---

## 5. Troubleshooting Common Setup Issues

### Issue 1: Gamepad connected but vehicle does not move
- **Symptom**: `teleop` runs without errors, but the motor and steering servo do not move when moving the sticks.
- **Cause**: Deadman switch button is not held down, or `/dev/input/js0` device node is missing.
- **Fix**:
  1. Ensure you are firmly holding down `L1` or `LB` while moving the sticks.
  2. Verify your joystick is registered at `/dev/input/js0`:
     ```bash
     ls -l /dev/input/js*
     ```
  3. If missing, revisit [[Pairing|Step 2: Gamepad Controller Pairing]] to reconnect via `bluetoothctl`.

### Issue 2: VESC Desync / Motor twitching / Topic crosstalk across computers
- **Symptom**: Odometry values jump randomly, motor twitches, or terminal reports timestamp desync errors.
- **Cause**: Multiple computers or robots on the same network are communicating on the default ROS domain (`ROS_DOMAIN_ID=0`). Nodes from another team are publishing conflicting messages.
- **Fix**: Assign your robot a unique domain ID matching your vehicle number (e.g. car 2 uses domain 2, car 7 uses domain 7):
  ```bash
  echo "export ROS_DOMAIN_ID=2" >> ~/.bashrc
  export ROS_DOMAIN_ID=2
  ```
  If students run ROS 2 tools on their personal laptops, they must set the matching `ROS_DOMAIN_ID` on their laptop.
  If running entirely on the vehicle NUC, you can also restrict traffic to localhost:
  ```bash
  export ROS_LOCALHOST_ONLY=1
  ```

### Issue 3: RViz2 opens with a black or blank window over Remote Desktop (RDP)
- **Symptom**: RViz2 starts, but the 3D viewport remains completely black or transparent.
- **Cause**: XRDP does not pass hardware OpenGL acceleration to remote sessions.
- **Fix**: Enable software OpenGL rendering before starting RViz2:
  ```bash
  export LIBGL_ALWAYS_SOFTWARE=1
  rviz2
  ```

### Issue 4: RealSense depth point cloud topic missing
- **Symptom**: Camera publishes color and depth images, but `/camera/camera/depth/color/points` does not exist.
- **Cause**: Point cloud generation is disabled by default in `realsense2_camera` to conserve CPU.
- **Fix**: Explicitly enable pointcloud in the launch command:
  ```bash
  ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true
  ```

### Issue 5: colcon build fails on YDLidar-SDK with missing doc directory
- **Symptom**: `CMake Error at CMakeLists.txt:... (install): install DIRECTORY given no DESTINATION or DIRECTORY "doc" does not exist.`
- **Cause**: The YDLidar-SDK CMake script attempts to install documentation files that are not included in the git repository.
- **Fix**: Create the empty directory manually before building:
  ```bash
  mkdir -p ~/arcpro_system/src/base/YDLidar-SDK/doc
  cd ~/arcpro_system && colcon build --symlink-install
  ```

---

## 6. (Optional) Setting Up on a Personal Laptop or Fresh Machine

If you are setting up your own personal Linux computer or virtual machine rather than using a pre-configured fleet car:

1. Clone the repository with HTTPS submodules:
   ```bash
   cd ~
   git clone -j8 --recurse-submodules=':!src/examples' https://github.com/airou-lab/arcpro_system.git
   ```
2. Resolve ROS 2 dependencies:
   ```bash
   cd ~/arcpro_system
   rosdep update
   rosdep install --from-paths src -y --ignore-src
   ```
3. Build the workspace:
   ```bash
   colcon build --symlink-install
   ```
4. Source the install environment:
   ```bash
   source ~/arcpro_system/install/setup.bash
   ```

---

## 7. Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| **[[Pairing|&larr; Step 2: Controller Pairing]]** | **Step 3: Software Bringup & First Drive** | **[[YDLidar X4 Pro and 435i realsense|Step 4: Sensor Check &rarr;]]** |
