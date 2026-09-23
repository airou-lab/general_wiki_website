---
Type:
  - arcProDocs
Labs:
  - AIROU
slug: index
title: ARCPro Docs Home
---

# AirOU Race Cars Pro (ARCPro)

Our robotic car platform is designed and built to autonomously navigate unknown environments, map in 2D/3D, and execute real-time state estimation and control. This site contains course materials for VNAV (Visual Navigation for Autonomous Vehicles), platform hardware and software guides, vehicle calibration instructions, and example projects.

> [!Warning] Running ROS 1?
> Please refer to our legacy ROS 1 documentation under [[archived_material/index|Archived Material]] or at the [AirOU Legacy ROS 1 Docs](https://airou-lab.github.io/docs/intro.html).

---

## Student Onboarding Track (Linear Steps 1 to 5)

Follow these steps sequentially before starting course labs:

1. **[[initial setup/Remote Connection|Step 1: Connecting Remotely to Your Robot]]** (Robot Hostname, Wi-Fi, Hotspot, SSH & RDP)
2. **[[initial setup/Pairing|Step 2: Bluetooth Gamepad Pairing]]** (DualShock pairing and joystick input verification)
3. **[[initial setup/Getting started with ARCPro software|Step 3: Software Bringup & First Drive]]** (ROS 2 workspace build, teleop, and troubleshooting)
4. **[[initial setup/YDLidar X4 Pro and 435i realsense|Step 4: Sensor Verification]]** (LiDAR 2D scan and RealSense RGB-D point clouds)
5. **[[initial setup/Tuning Guide|Step 5: Vehicle Calibration & Tuning]]** (Steering trim, servo gain, and speed scaling)
   - **Proceed to Lab 1:** **[[SP2026-VNAV-CourseContent/labs/Lab 1 - Exercises|VNAV Lab 1: First Exercises]]**

---

## VNAV Course Curriculum

- **[[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]** (Labs 1 to 7)
- **[[SP2026-VNAV-CourseContent/lectures/index|Lecture Slides & Viewers]]**
- **[[SP2026-VNAV-CourseContent/notes/index|Course Notes & Readings]]**

---

## Hardware Assembly & Maintenance Track (Builders & Staff)

- **[[initial setup/hardware|Hardware Setup & Initial Powerup]]**: Component layout, battery connection, and power board.
- **[[initial setup/building the bot/index|Chassis Assembly & 3D Print Platforms (STL)]]**: Top plates, camera hinges, and mechanical drawings.
- **[[initial setup/VESC aka FSEC|VESC Motor Controller Setup & Recovery]]**: VESC Tool configuration and ST-Link unbricking.
- **[[initial setup/ARCPro specifications|Vehicle Specifications & Dimensions]]**: Physical dimensions, wheelbase, track width, and payload limits.
- **[[initial setup/arcpro run commands|Turnkey Robot Commands Reference]]**: Alias scripts (`teleop`, `teleop_key`, `lidar`, `camera`, `slam`, `telemetry`, `killall`).

### Reference Examples
- [[waypointer/arcpro waypointer example run|Waypointer Example Run]]
- [[waypointer/guides/Fusing sensors with robot_localization|Sensor Fusion with Robot Localization (EKF)]]
- [[passive reinforcement learning/Running the Sim and sim2real|Reinforcement Learning Simulation & Sim2Real]]

### Archived Material
- [[archived_material/index|Legacy ROS 1 ARCPro, LIONN Drone & JetBot Documentation]]

---

## Repository Layout

All packages live inside the `src` directory of [`airou-lab/arcpro_system`](https://github.com/airou-lab/arcpro_system):

- **`base/`**: Core packages for robot bringup, sensor drivers, and Ackermann conversion:
  - `f1tenth_to_arcpro`: Hardware stack (`f1tenth_stack`, `vesc`, `f1tenth_teleop`, `ackermann_mux`).
  - `YDLidar`: YDLidar X4 Pro ROS 2 driver.
  - `twist_to_ackermann`: Twist to Ackermann drive message converter.
- **`examples/`**: Reference navigation and reinforcement learning projects:
  - `waypointer`: Waypoint following and navigation examples.
  - `arc_rl_interface`: Reinforcement learning sim2real interface.

---

## Credits & Outside Resources

ARCPro hardware and software architecture is derived from the [MuSHR Project](https://mushr.io/) and [F1TENTH](https://roboracer.ai/build).

For questions or assistance:
- **Software & Systems**: Arika Khor (`arikak@ou.edu`)
- **Hardware & MiniCity**: Daniel Vargas (`dvargas88@ou.edu`)
- **MuSHR Discussions**: [MuSHR GitHub Discussions](https://github.com/prl-mushr/mushr/discussions)