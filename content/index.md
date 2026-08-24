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

## VNAV - Start Here

- **[[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]** (Labs 1–7)
- **[[SP2026-VNAV-CourseContent/lectures/index|Lecture Slides & Viewers]]**
- **[[SP2026-VNAV-CourseContent/notes/index|Course Notes]]**
- **[[initial setup/Getting started with ARCPro software|Getting Started with ARCPro Software]]**
- **[[initial setup/Tuning Guide|ARCPro Tuning Guide (Calibrating your car)]]**

---

## Platform Setup & Documentation

### Hardware
- [[initial setup/hardware|Hardware Setup & Initial Boot]] (Start here for physical car setup)
- [[initial setup/ARCPro specifications|Vehicle Specifications & Dimensions]]
- [[initial setup/Pairing|Bluetooth Gamepad Pairing]]

### Software
- [[initial setup/Getting started with ARCPro software|Software Bringup & Ansible Setup]]
- [[initial setup/Tuning Guide|Tuning Guide (Steering Trim & Speed Scaling)]]
- [[initial setup/YDLidar X4 Pro and 435i realsense|Sensors: YDLIDAR X4 Pro & Intel RealSense D435i]]
- [[initial setup/arcpro run commands|Basic Drive & Sensor Commands]]

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