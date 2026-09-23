---
Type:
  - arcProDocs
Labs:
  - AIROU
---
> [!note] Running from our repo directly?
> If you cloned our repository and followed the build steps, skip directly to [[arcpro run commands|Basic Drive and Sensor Commands]].

> [!warning] Port configurations
> Note that serial ports in these guides may differ depending on your USB hub enumeration. Verify with `lsusb` or `ls /dev/tty*`.

# Setting up YDLidar X4 Pro and RealSense D435i

> [!info] ARC Pro Student Onboarding: Step 4 of 5
> Previous: [[Getting started with ARCPro software|Step 3: Software Bringup & First Drive]]. Next: [[Tuning Guide|Step 5: Vehicle Calibration & Tuning]].

## Intel RealSense D435i

Install the RealSense ROS 2 packages and set up udev permissions:

```bash
sudo apt update
sudo apt install -y v4l-utils ros-jazzy-librealsense2 ros-jazzy-realsense2-camera ros-jazzy-realsense2-camera-msgs

# Ensure permissions for the camera
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo usermod -aG video $USER
```

To launch the camera with RGB, depth frames, and 3D depth point cloud enabled:

```bash
ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true
```

Topics published:
- `/camera/camera/color/image_raw`: Color camera stream
- `/camera/camera/depth/image_rect_raw`: Aligned depth frames
- `/camera/camera/depth/color/points`: 3D Point cloud

---

## YDLidar X4 Pro (2D LiDAR)

### 1. Build the SDK
Clone the SDK repository via HTTPS:

```bash
cd ~
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK
mkdir build && cd build
cmake ..
make
sudo make install
```

### 2. Build the ROS 2 Driver
In your ROS 2 workspace `src` directory:

```bash
cd ~/arcpro_system/src
git clone https://github.com/YDLIDAR/ydlidar_ros2_driver.git
cd ~/arcpro_system
colcon build --symlink-install --packages-select ydlidar_ros2_driver
```

To launch the 2D LiDAR driver:

```bash
ros2 launch ydlidar_ros2_driver ydlidar_launch.py sim:=false
```

---

## Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| [[Getting started with ARCPro software\|&larr; Step 3: Software Bringup & First Drive]] | **Step 4: Sensor Verification** | [[Tuning Guide\|Step 5: Vehicle Calibration & Tuning &rarr;]] |