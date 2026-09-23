---
title: Setup
slug: setup
---

# ARC Pro Setup & Documentation

Welcome to the ARC Pro setup documentation. Follow the tracks below based on your role:

---

## Student Onboarding Track (Linear Steps 1 to 5)

Students taking VNAV or working with fleet cars should follow these steps in sequential order before starting Lab 1:

1. **[[Remote Connection|Step 1: Connecting Remotely to Your Robot]]**
   - Connect via robot hostname (`arcproX.local` / `arcproX`), campus Wi-Fi, direct Ethernet, or robot hotspot.
   - Access via SSH or Windows Remote Desktop (XRDP).
2. **[[Pairing|Step 2: Bluetooth Gamepad Pairing]]**
   - Pair Sony DualShock or Bluetooth wireless controller using `bluetoothctl`.
   - Verify `/dev/input/js0` joystick device registration.
3. **[[Getting started with ARCPro software|Step 3: Software Bringup & First Drive]]**
   - Source the ROS 2 workspace, run turnkey movement commands (`teleop`, `teleop_key`, `move_forward`), and review common troubleshooting fixes.
4. **[[YDLidar X4 Pro and 435i realsense|Step 4: Sensor Verification]]**
   - Verify 2D LiDAR scans on `/scan` and Intel RealSense color, depth, and 3D point cloud feeds.
5. **[[Tuning Guide|Step 5: Vehicle Calibration & Tuning]]**
   - Calibrate steering trim, servo gain, and speed/odometry scaling in `vesc.yaml`.
   - **Next:** Proceed directly to **[[SP2026-VNAV-CourseContent/labs/Lab 1 - Exercises|VNAV Lab 1: First Exercises]]**.

---

## Hardware Assembly & Maintenance Track (Builders & Staff)

For team members assembling new chassis, wiring power systems, or flashing motor controller firmware:

- **[[hardware|Hardware Overview & Initial Powerup]]**: Component layout, battery connection, and power distribution board.
- **[[building the bot/index|Chassis Assembly & 3D Print Files (STL)]]**: Top plates, camera hinges, standoffs, and mechanical drawings.
- **[[VESC aka FSEC|VESC Motor Controller Setup & Firmware Recovery]]**: VESC Tool configuration, baud rates, and ST-Link unbricking procedures.
- **[[ARCPro specifications|Platform Dimensions & Technical Specifications]]**: Wheelbase, track width, gear ratio, sensor FOV, and payload limits.

---

## Quick Reference & Commands

- **[[arcpro run commands|Turnkey Robot Commands Reference]]**: Complete list of alias scripts (`teleop`, `teleop_key`, `lidar`, `camera`, `slam`, `telemetry`, `killall`).
- **[[Calibrating your car|Quick Calibration Notes]]**: Fast parameter lookups for on-track trim adjustments.

---

## Course Curriculum

- **[[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises (Labs 1 to 7)]]**
- **[[SP2026-VNAV-CourseContent/lectures/index|Lecture Slides & Viewers]]**
- **[[SP2026-VNAV-CourseContent/notes/index|Course Notes & Readings]]**