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

### 1. Installation & Permissions
On ARC Pro robots, the RealSense driver and udev rules are installed automatically. If setting up manually:

```bash
sudo apt update
sudo apt install -y v4l-utils ros-jazzy-librealsense2 ros-jazzy-realsense2-camera ros-jazzy-realsense2-camera-msgs

# Install official RealSense udev rules (required for USB buffer allocation & IMU access)
sudo curl -sL https://raw.githubusercontent.com/realsenseai/librealsense/master/config/99-realsense-libusb.rules \
    -o /etc/udev/rules.d/99-realsense-libusb.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo usermod -aG video,plugdev $USER
```

> [!important] Firmware Compatibility Requirement (5.17.0.9+ for ROS 2 Jazzy)
> ROS 2 Jazzy's `librealsense2` package (v2.56.4+) strictly requires camera firmware **`5.17.0.9 or later`**.
> If your camera holds older firmware (such as `5.12.x`), the node will crash on startup with `xioctl(VIDIOC_QBUF) failed: No such device` and USB protocol errors (`-EPROTO -71`).
>
> To check your camera firmware version:
> ```bash
> bash -c '. /opt/ros/jazzy/setup.bash && /opt/ros/jazzy/bin/rs-fw-update -l'
> ```
> To update outdated firmware using the official binary:
> ```bash
> bash -c '. /opt/ros/jazzy/setup.bash && /opt/ros/jazzy/bin/rs-fw-update -f /path/to/D4XX_FW_Image-5.17.0.9.bin'
> ```

### 2. Launching the Camera

#### Option A: Turnkey Command (Recommended)
On fleet robots, run the turnkey command in any terminal:
```bash
camera
# or: bash ~/example_scripts/camera.sh
```

#### Option B: Direct ROS 2 Launch
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

### 3. Persistent Port Configuration (`/dev/ydlidar`)
ARC Pro robots use udev rule `99-ydlidar.rules` mapping vendor `10c4:ea60` to `/dev/ydlidar`.
Ensure `~/arcpro_system/src/base/ydlidar_ros2_driver/params/ydlidar.yaml` specifies:
```yaml
port: /dev/ydlidar
```

### 4. Launching the LiDAR

#### Option A: Turnkey Command (Recommended)
```bash
lidar
# or: bash ~/example_scripts/lidar.sh
```

#### Option B: Direct ROS 2 Launch
```bash
ros2 launch ydlidar_ros2_driver ydlidar_launch.py
```

Topics published:
- `/scan`: `sensor_msgs/msg/LaserScan` (360-degree laser scan at ~11.6 Hz)

---

## Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| [[Getting started with ARCPro software\|&larr; Step 3: Software Bringup & First Drive]] | **Step 4: Sensor Verification** | [[Tuning Guide\|Step 5: Vehicle Calibration & Tuning &rarr;]] |