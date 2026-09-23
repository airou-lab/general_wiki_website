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

Welcome to the ARCPro software stack. This guide covers cloning the system repository, pairing your controller, compiling the ROS 2 workspace, testing manual driving (teleoperation), verifying onboard sensors (LiDAR and RealSense camera), and troubleshooting common setup issues.

> [!info] Prerequisites
> - Ensure the onboard Intel NUC is powered on (see [[hardware|Hardware Setup]]).
> - Connect your laptop to the robot via **Wi-Fi Hotspot** (`ARCPRO_XX` on `192.168.4.1`) or **Campus Static IP** (`10.204.x.x`) or **Tailscale** (see [[Remote Connection|Connecting Remotely to Your Robot]]).
> - Ensure hardware batteries and USB cables for the VESC, YDLidar, and RealSense camera are connected.

---

## 0. Gamepad Controller Pairing (Bluetooth)

Before running teleoperation, pair your Bluetooth gamepad controller with the onboard NUC.

### Step 1: Put the Controller in Pairing Mode
Press and hold the **Share** button and the **Center PS** button simultaneously for approximately 5 seconds until the lightbar begins rapidly blinking.

### Step 2: Pair Using bluetoothctl
Open a terminal on the robot (via SSH or Remote Desktop) and execute:

```bash
bluetoothctl
```

Inside the `bluetoothctl` prompt:

```text
[bluetooth]# agent on
[bluetooth]# default-agent
[bluetooth]# scan on
```

Watch the terminal for your controller MAC address (named "Wireless Controller"):

```text
[CHG] Device BB:8E:41:F5:5D:C7 Name: Wireless Controller
[CHG] Device BB:8E:41:F5:5D:C7 Alias: Wireless Controller
```

Run the following commands using your controller's MAC address:

```text
[bluetooth]# pair BB:8E:41:F5:5D:C7
[bluetooth]# trust BB:8E:41:F5:5D:C7
[bluetooth]# connect BB:8E:41:F5:5D:C7
[bluetooth]# scan off
[bluetooth]# exit
```

### Step 3: Verify Controller Device Node
Verify that Linux has registered the joystick interface:

```bash
ls -l /dev/input/js*
```

You should see `/dev/input/js0`. If not found, repeat the pairing steps above.

---

## 1. Getting the Codebase

> [!tip] Using an Ansible-Provisioned Robot?
> If your ARCPro robot was set up using the **ARCPRO Ansible Image**, the entire `arcpro_system` repository, ROS 2 Jazzy desktop environment, SLAM Toolbox, Nav2, and turnkey test scripts are already pre-installed and pre-built in `~/arcpro_system`.
> You can proceed directly to **[[#3. Testing Teleoperation & Driving|Section 3: Testing Teleoperation]]**.

The primary codebase for ARCPro is hosted at `https://github.com/airou-lab/arcpro_system.git`.

If setting up on a fresh machine or student laptop, clone the repository using HTTPS:

```bash
cd ~
git clone -j8 --recurse-submodules=':!src/examples' https://github.com/airou-lab/arcpro_system.git
```

> [!note] Submodule Flag
> The flag `--recurse-submodules=':!src/examples'` clones all core robotics packages (VESC drivers, teleop, YDLidar SDK, Ackermann mux) while omitting large optional simulation assets.

If submodules fail to clone due to SSH authentication errors, tell Git to resolve GitHub SSH URLs over HTTPS:

```bash
git config --global url."https://github.com/".insteadOf "git@github.com:"
cd ~/arcpro_system
git submodule update --init --recursive
```

---

## 2. Resolving Dependencies & Building

Navigate to the workspace, ensure the required YDLidar-SDK directory structure is in place, and install all ROS 2 dependencies:

```bash
cd ~/arcpro_system

# Ensure YDLidar-SDK doc directory exists for CMake install target
mkdir -p src/base/YDLidar-SDK/doc

# Resolve ROS package dependencies
rosdep update
rosdep install --from-paths src -y --ignore-src
```

Now compile the workspace using `colcon`:

```bash
colcon build --symlink-install
```

### Source the Environment
To use the newly built packages, source both the ROS 2 base installation and your local overlay:

```bash
source /opt/ros/jazzy/setup.bash
source ~/arcpro_system/install/setup.bash
```

To automatically configure every new terminal session, add them to `~/.bashrc`:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "source ~/arcpro_system/install/setup.bash" >> ~/.bashrc
```

---

## 3. Testing Teleoperation & Driving

Verify that the VESC motor controller and steering servo respond properly to manual inputs before running autonomous code.

### Option A: Using Turnkey Terminal Aliases
On ARC Pro robots, the following convenience aliases are available:

```bash
# 1. Gamepad Teleop (Hold L1/LB deadman + Left Stick throttle + Right Stick steer)
teleop

# 2. Interactive Keyboard Teleop (drive using i/j/k/l keys in terminal)
teleop_key

# 3. Quick Drivetrain Verification (drives forward at 0.4 m/s, Ctrl+C stops)
straight
```

### Option B: Using Direct ROS 2 Launch Commands

1. **Launch the VESC Hardware Driver & Odometry**:
   ```bash
   ros2 launch f1tenth_teleop vesc.launch.py
   ```

2. **Launch Teleop & Translator**:
   ```bash
   # In terminal 2:
   ros2 launch f1tenth_teleop teleop.launch.py joy_dev:=/dev/input/js0
   ```

3. **Drive Test**:
   - Hold the deadman button on your controller (button `L1` or `LB`).
   - Gently move the left thumbstick for throttle and right thumbstick for steering.

### Testing Direct Drive Messages (Without Gamepad)
You can test the drivetrain directly from the command line by publishing an `AckermannDriveStamped` message:

```bash
ros2 topic pub /ackermann_cmd ackermann_msgs/msg/AckermannDriveStamped \
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
  drive: {steering_angle: 0.0, speed: 0.4}}' -r 10
```

---

## 4. Testing Onboard Sensors & Cameras

### Intel RealSense D435i Camera

1. Launch the RealSense ROS 2 node (with pointcloud enabled):
   ```bash
   ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true
   ```

2. Verify image and depth cloud topics:
   ```bash
   ros2 topic list | grep camera
   ```
   You should see:
   - `/camera/camera/color/image_raw`
   - `/camera/camera/depth/image_rect_raw`
   - `/camera/camera/depth/color/points` (3D Point Cloud)
   - `/camera/camera/imu`

3. Visualize image feeds in `rqt_image_view`:
   ```bash
   ros2 run rqt_image_view rqt_image_view
   ```

### YDLidar X4 Pro (2D LiDAR)

1. Launch the LiDAR driver:
   ```bash
   ros2 launch ydlidar_ros2_driver ydlidar_launch.py sim:=false
   ```

2. Verify that the laser scan is publishing on `/scan`:
   ```bash
   ros2 topic echo /scan --once
   ```

---

## 5. Troubleshooting Common Setup Issues

### Issue 1: colcon build fails on YDLidar-SDK with missing doc directory
- **Symptom**: `CMake Error at CMakeLists.txt:... (install): install DIRECTORY given no DESTINATION or DIRECTORY "doc" does not exist.`
- **Cause**: The YDLidar-SDK CMake script attempts to install documentation files that are not included in the git repository.
- **Fix**: Create the empty directory manually before building:
  ```bash
  mkdir -p ~/arcpro_system/src/base/YDLidar-SDK/doc
  cd ~/arcpro_system && colcon build --symlink-install
  ```

### Issue 2: Git submodule clone asks for SSH key or gives Permission Denied
- **Symptom**: `git@github.com: Permission denied (publickey). fatal: Could not read from remote repository.`
- **Cause**: Submodule definitions point to SSH URLs while your machine does not have an SSH key configured with GitHub.
- **Fix**: Rewrite SSH URLs to HTTPS:
  ```bash
  git config --global url."https://github.com/".insteadOf "git@github.com:"
  cd ~/arcpro_system && git submodule update --init --recursive
  ```

### Issue 3: Gamepad connected but vehicle does not move
- **Symptom**: Teleop runs without errors, but the motor and steering servo do not move when using joysticks.
- **Cause**: Deadman switch button is not held down, or `/dev/input/js0` device node is wrong.
- **Fix**:
  1. Ensure you are holding down `L1` or `LB` while moving the sticks.
  2. Verify your joystick is registered at `/dev/input/js0`:
     ```bash
     ls -l /dev/input/js*
     ```
  3. Echo the joy topic to confirm stick and button events:
     ```bash
     ros2 topic echo /joy --once
     ```

### Issue 4: VESC Desync / Motor twitching / Topic crosstalk across computers
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

### Issue 5: RViz2 opens with a black or blank window over Remote Desktop (RDP)
- **Symptom**: RViz2 starts, but the 3D viewport remains completely black or transparent.
- **Cause**: XRDP does not pass hardware OpenGL acceleration to remote sessions.
- **Fix**: Enable software OpenGL rendering before starting RViz2:
  ```bash
  export LIBGL_ALWAYS_SOFTWARE=1
  rviz2
  ```

### Issue 6: RealSense depth point cloud topic missing
- **Symptom**: Camera publishes color and depth images, but `/camera/camera/depth/color/points` does not exist.
- **Cause**: Point cloud generation is disabled by default in `realsense2_camera` to conserve CPU.
- **Fix**: Explicitly enable pointcloud in the launch command:
  ```bash
  ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true
  ```

---

## 6. Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| **[[Pairing|&larr; Step 2: Controller Pairing]]** | **Step 3: Software Bringup & First Drive** | **[[YDLidar X4 Pro and 435i realsense|Step 4: Sensor Check &rarr;]]** |
