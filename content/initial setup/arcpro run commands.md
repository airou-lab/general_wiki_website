---
Type:
  - arcProDocs
Labs:
  - AIROU
---

# Basic ARCPro Run Commands

This reference page provides the standard ROS 2 commands to bring up the motor controller, sensors, teleoperation, and direct Ackermann driving.

> [!tip] Quick Reference
> Make sure your workspace is built and sourced before running these commands (`source ~/arcpro_system/install/setup.bash`).

```bash
# 1. Bring up VESC motor controller
ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false

# 2. Bring up 2D LiDAR (YDLIDAR X4 Pro)
ros2 launch ydlidar_ros2_driver ydlidar_launch.py sim:=false

# 3. Bring up RealSense Camera (Intel D435i)
ros2 launch realsense2_camera rs_launch.py

# 4. Launch Teleoperation with wireless gamepad
ros2 launch f1tenth_teleop teleop.launch.py joy_dev:=ttyUSB0

# 5. Send a direct Ackermann drive command (speed: 0.4 m/s, steering: 0.0 rad)
ros2 topic pub /drive_stamped ackermann_msgs/msg/AckermannDriveStamped \
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
  drive: {steering_angle: 0.0, speed: 0.4}}' -r 10
```

---

## Next Steps
- [[Getting started with ARCPro software|Getting Started with ARCPro Software]]
- [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- [[SP2026-VNAV-CourseContent/labs/index|VNAV Course Labs]]