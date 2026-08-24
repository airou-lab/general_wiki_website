---
title: "ARCPro Tuning Guide"
tags:
  - arcProDocs
  - setup
  - calibration
  - tuning
---

# ARCPro Tuning Guide

Fine-tuning car-specific control parameters for steering trim, steering gain, and speed/odometry scaling.

> [!info] Based on MuSHR & F1TENTH Calibration
> This guide is adapted from the [MuSHR Racecar Tuning Guide](https://mushr.io/tutorials/tuning/) and configured specifically for the ARCPro robotics platform and the ROS 2 [`f1tenth_stack`](https://github.com/airou-lab/arcpro_system) repository.

---

## 1. Introduction

The VESC electronic speed controller maps high-level commanded velocities ($v$ in $\text{m/s}$) and steering angles ($\delta$ in radians) to electrical RPM (ERPM) and servo PWM values. Due to small physical variations in linkage geometry, tire diameter, and motor characteristics between individual robots, these conversion parameters must be tuned specifically for each car.

If uncalibrated, commands issued by your autonomous controllers, planners, and trajectory trackers will not match physical motion on the track.

### The Conversion Model

The conversions are linear functions of input commands:

$$\text{servo\_value} = \text{steering\_angle\_to\_servo\_gain} \cdot \delta + \text{steering\_angle\_to\_servo\_offset}$$

$$\text{erpm} = \text{speed\_to\_erpm\_gain} \cdot v + \text{speed\_to\_erpm\_offset}$$

### Configuration File Location

All tuning parameters are located in the [`f1tenth_to_arcpro`](https://github.com/airou-lab/f1tenth_to_arcpro) submodule inside your `arcpro_system` workspace at:

```text
~/arcpro_system/src/base/f1tenth_to_arcpro/f1tenth_stack/config/vesc.yaml
```

```yaml
/**:
  ros__parameters:
    # Velocity to ERPM mapping
    speed_to_erpm_gain: 4571.5
    speed_to_erpm_offset: 0.0

    # Steering angle to Servo mapping
    steering_angle_to_servo_gain: -1.2135
    steering_angle_to_servo_offset: 0.4705

    # Physical parameters
    wheelbase: 0.2413 # 24.13 cm
    port: /dev/ttyACM0
```

---

## 2. Requirements & Setup

- A computer with `ssh` access to your ARCPro robot.
- A tape measure (at least 5 meters / 15 feet).
- Painter's tape or chalk to mark the floor.
- An open, flat driving area (~5m $\times$ 3m).

---

## 3. Step 1: Tuning Steering Angle Offset (`steering_angle_to_servo_offset`)

The goal of this step is to find the servo center position where the car drives in a perfectly straight line when commanded with $\delta = 0\text{ rad}$.

### Procedure:

1. **Mark a Straight Line**: Place a 3 to 5 meter piece of tape in a straight line on the floor.
2. **Align the Robot**: Position the car with its center aligned along the tape line.
3. **Command Straight Drive**: Send a slow, forward command with zero steering:
   ```bash
   ros2 topic pub /drive_stamped ackermann_msgs/msg/AckermannDriveStamped \
   '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
     drive: {steering_angle: 0.0, speed: 0.5}}' -r 10
   ```
4. **Observe the Trajectory**:
   - If the car drifts to the **RIGHT**: **Increase** `steering_angle_to_servo_offset` (e.g., $0.4705 \to 0.485$).
   - If the car drifts to the **LEFT**: **Decrease** `steering_angle_to_servo_offset` (e.g., $0.4705 \to 0.455$).

5. **Iterate**: Adjust the value in `vesc.yaml`, re-launch `f1tenth_stack`, and test until the car tracks the tape line straight for at least 3 meters.

---

## 4. Step 2: Tuning Steering Angle Gain (`steering_angle_to_servo_gain`)

The steering gain maps radians of requested steering angle to the physical range of servo motion.

Using the kinematic bicycle model, the theoretical turning circle radius $R$ for a car with wheelbase $L$ and steering angle $\delta$ is:

$$R = \frac{L}{\tan(\delta)}$$

For ARCPro with wheelbase $L \approx 0.2413\text{ m}$:
- At $\delta = 0.30\text{ rad} \approx 17.18^\circ$, expected turning radius $R \approx \frac{0.2413}{\tan(0.30)} \approx 0.78\text{ m}$ (diameter $\approx 1.56\text{ m}$).

### Procedure:

1. Command a constant turning angle:
   ```bash
   ros2 topic pub /drive_stamped ackermann_msgs/msg/AckermannDriveStamped \
   '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"}, \
     drive: {steering_angle: 0.30, speed: 0.4}}' -r 10
   ```
2. Measure the physical diameter of the circle driven by the front axle with your tape measure.
3. Compute the actual turning radius $R_{\text{actual}} = \frac{\text{Diameter}}{2}$.
4. **Adjust Gain**:
   - If the car turns **too wide** ($R_{\text{actual}} > R_{\text{expected}}$): Increase the magnitude of `steering_angle_to_servo_gain` (e.g., $-1.21 \to -1.35$).
   - If the car turns **too sharp** ($R_{\text{actual}} < R_{\text{expected}}$): Decrease the magnitude of `steering_angle_to_servo_gain` (e.g., $-1.21 \to -1.10$).

---

## 5. Step 3: Tuning Speed to ERPM Gain (`speed_to_erpm_gain`)

The `speed_to_erpm_gain` parameter ensures that commanding a speed of $1.0\text{ m/s}$ results in an actual ground speed of $1.0\text{ m/s}$, and produces accurate wheel odometry on `/odom`.

### Procedure:

1. **Mark Start and End Points**: Lay down two parallel tape lines exactly **5.0 meters** apart.
2. **Align Front Wheels**: Align the front tire contact point with the start line.
3. **Echo Odometry in Terminal**:
   ```bash
   ros2 topic echo /odom/pose/pose/position/x
   ```
4. **Drive Forward**: Slowly drive the car forward until the front wheels touch the 5.0-meter finish line.
5. **Calculate Odometry Error**: Note the distance recorded by the odometry topic ($\Delta x_{\text{odom}}$).
6. **Update the Gain**:
   Use the scaling ratio to compute your new gain:

   $$\text{speed\_to\_erpm\_gain}_{\text{new}} = \text{speed\_to\_erpm\_gain}_{\text{current}} \cdot \left(\frac{\Delta x_{\text{odom}}}{5.0\text{ m}}\right)$$

   *(Example: If current gain is $4571.5$ and the `/odom` reported $5.4\text{ m}$ over a $5.0\text{ m}$ physical distance, set new gain to $4571.5 \cdot \frac{5.4}{5.0} = 4937.22$)*.

7. Save `vesc.yaml`, re-launch, and repeat to confirm $\Delta x_{\text{odom}} \approx 5.00\text{ m}$.

---

## 6. Verification & Saving Changes

Once tuning is complete:
1. Re-build your package to ensure install overlays pick up changes:
   ```bash
   cd ~/arcpro_system
   colcon build --symlink-install --packages-select f1tenth_stack
   ```
2. Commit your car's tuned configuration to your team's branch or repository.
3. Test your tuned vehicle in teleoperation and proceed with your lab deliverables:
   - [[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]
   - [[SP2026-VNAV-CourseContent/labs/Lab 7 - Exercises|Lab 7 - Vehicle Control & Trajectory Tracking]]
