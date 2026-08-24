---
title: "Getting Started with ARCPro Software"
tags:
  - arcProDocs
  - setup
  - software
---

# Getting Started with ARCPro Software

Welcome to the ARCPro software stack! This guide walks you through cloning the system repository, building the ROS 2 workspace, testing manual driving (teleoperation), verifying onboard sensors (LiDAR & RealSense cameras), and moving forward to vehicle calibration and tuning.

> [!info] Prerequisites
> - Ensure your robot's onboard Intel NUC is powered on and connected to the network.
> - Ensure hardware batteries and USB cables for the VESC, YDLidar, and RealSense camera are connected (see [[hardware|Hardware Setup]]).
> - Ensure your gamepad is paired (see [[Pairing|Bluetooth Gamepad Pairing]]).

---

## 1. Getting the Codebase

> [!tip] Using an Ansible-Provisioned Robot?
> If your ARCPro robot was set up using the **[ARCPRO Ansible Image](https://github.com/airou-lab/ARCPRO_Ansible-Images)**, the entire `arcpro_system` repository, ROS 2 environment, and core dependencies are **already pre-installed and pre-built** in `~/arcpro_system`!
> You can skip the manual cloning and build steps below and jump directly to **[[#3. Testing Teleoperation & Driving|Section 3: Testing Teleoperation]]**.

The primary codebase for ARCPro is hosted at [`airou-lab/arcpro_system`](https://github.com/airou-lab/arcpro_system). 

If you are setting up on a fresh machine or personal laptop, clone the repository to your home directory:

```bash
cd ~
git clone -j8 --recurse-submodules=':!src/examples' https://github.com/airou-lab/arcpro_system.git
```

> [!tip] Submodule Flag
> The flag `--recurse-submodules=':!src/examples'` clones all core robotics packages (VESC drivers, teleop, YDLidar SDK, Ackermann mux) while omitting large optional simulation examples.

> [!info] Repository & Submodule Architecture
> The core robot hardware drivers and bringup launch files are maintained in the [`airou-lab/f1tenth_to_arcpro`](https://github.com/airou-lab/f1tenth_to_arcpro) repository, included as a git submodule under `src/base/f1tenth_to_arcpro`. This submodule provides:
> - **`f1tenth_stack`**: Main bringup launch files and configuration parameters (`config/vesc.yaml`).
> - **`vesc`**: VESC motor controller driver and odometry node.
> - **`f1tenth_teleop`**: Gamepad joystick teleoperation node.
> - **`ackermann_mux`**: Command priority multiplexer.

---

## 2. Resolving Dependencies & Building

Navigate to the workspace and install all required ROS 2 dependencies using `rosdep`:

```bash
cd ~/arcpro_system
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

> [!tip] Automatic Sourcing
> Add the commands above to your `~/.bashrc` file so every new terminal session is automatically configured:
> ```bash
> echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
> echo "source ~/arcpro_system/install/setup.bash" >> ~/.bashrc
> ```

---

## 3. Testing Teleoperation & Driving

Before running autonomous stacks, verify that the VESC motor controller and servo respond properly to manual control.

### Option A: Using Helper Scripts
`arcpro_system` provides convenience launch scripts:

```bash
# Terminal 1: Launch VESC hardware driver
./hardware_scripts/vesc.sh

# Terminal 2: Launch Teleoperation node
./movement_scripts/teleop.sh
```

### Option B: Using Direct ROS 2 Launch Commands

1. **Launch the VESC Stack**:
   ```bash
   ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false
   ```

2. **Launch Teleop**:
   ```bash
   ros2 launch f1tenth_teleop teleop.launch.py joy_dev:=ttyUSB0
   ```

3. **Drive Test**:
   - Hold the deadman button on your wireless controller (typically `L1` or `R1`).
   - Gently move the left thumbstick for throttle and right thumbstick for steering.

### Testing Direct Drive Messages (Without Gamepad)
You can also send a test Ackermann drive command directly from the command line:

```bash
ros2 topic pub /drive_stamped ackermann_msgs/msg/AckermannDriveStamped \
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
  drive: {steering_angle: 0.0, speed: 0.4}}' -r 10
```

---

## 4. Testing Onboard Sensors & Cameras

### Intel RealSense D435i Camera

1. Launch the RealSense ROS 2 node:
   ```bash
   ./hardware_scripts/realsense.sh
   # OR directly:
   ros2 launch realsense2_camera rs_launch.py
   ```

2. Verify image topics:
   ```bash
   ros2 topic list | grep camera
   ```
   You should see:
   - `/camera/camera/color/image_raw`
   - `/camera/camera/depth/image_rect_raw`
   - `/camera/camera/imu`

3. Visualize image feeds in RViz2 or `rqt_image_view`:
   ```bash
   ros2 run rqt_image_view rqt_image_view
   ```

### YDLidar X4 Pro (2D LiDAR)

1. Launch the LiDAR driver:
   ```bash
   ./hardware_scripts/lidar.sh
   # OR directly:
   ros2 launch ydlidar_ros2_driver ydlidar_launch.py sim:=false
   ```

2. Verify that the laser scan is publishing on `/scan`:
   ```bash
   ros2 topic echo /scan --once
   ```

---

## 5. Next Steps

Now that your software stack and sensors are operational, proceed to tune your car's physical steering trim, speed multiplier, and odometry, then proceed with the course lab exercises:

- 🏎️ **Next Step**: [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- 📚 **Course Curriculum**: [[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises (Labs 1–7)]]
