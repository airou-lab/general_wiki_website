---
Type:
  - arcProDocs
Labs:
  - AIROU
---

# Basic ARCPro Run Commands

This reference page provides the standard commands to bring up motor control, teleoperation, LiDAR SLAM, and sensors on ARC Pro robots.

> [!tip] Turnkey Aliases (Pre-Configured in Zsh)
> If you are connected to an ARC Pro robot as user `arc`, the following turnkey command aliases are available in any terminal:
> - **`move_forward`** (or **`straight`**): Test drivetrain forward at 0.4 m/s (auto-stops on `Ctrl+C`)
> - **`teleop`** (or **`teleop_joy`**): Gamepad teleop (Hold `L1/LB` deadman + left stick throttle, right stick steer)
> - **`teleop_key`**: Interactive keyboard driving in terminal
> - **`lidar`**: Standalone 2D LiDAR bringup (`/scan`)
> - **`camera`**: Standalone Intel RealSense camera bringup
> - **`telemetry`**: Foxglove Bridge (`:8765`), LiDAR, and RealSense camera streaming
> - **`slam`**: Real-time 2D SLAM Toolbox mapping (`/scan` + VESC odom &rarr; `/map`)
> - **`killall`** (or **`killall_nodes`**): Cleanly terminate all robot ROS processes and clear shared memory

---

## Direct ROS 2 Commands

```bash
# 1. Bring up VESC motor controller & odometry
ros2 launch launches vesc.launch.py

# 2. Bring up 2D LiDAR (YDLIDAR X4 Pro)
ros2 launch ydlidar_ros2_driver ydlidar_launch.py

# 3. Bring up RealSense Camera (Intel D435i)
ros2 launch realsense2_camera rs_launch.py

# 4. Launch Gamepad Teleoperation
ros2 launch launches teleop.launch.py joy_dev:=/dev/input/js0

# 5. Launch SLAM Toolbox (Online Async Mapping)
ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/home/arc/arcpro_system/scripts/config/slam_toolbox_params.yaml

# 6. Save your SLAM map
ros2 run nav2_map_server map_saver_cli -f ~/my_lab_map

# 7. Send a direct Ackermann drive command (speed: 0.4 m/s, steering: 0.0 rad)
ros2 topic pub /ackermann_cmd ackermann_msgs/msg/AckermannDriveStamped \
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
  drive: {steering_angle: 0.0, speed: 0.4}}' -r 10
```

---

## Next Steps
- [[Getting started with ARCPro software|Getting Started with ARCPro Software]]
- [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- [[SP2026-VNAV-CourseContent/labs/index|VNAV Course Labs]]