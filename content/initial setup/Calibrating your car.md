---
title: "Calibrating Your Car"
tags:
  - arcProDocs
  - setup
  - calibration
---

# Calibrating Your Car

For the complete step-by-step procedure and quickstart reference on fine-tuning your ARCPro steering angle offset, steering gain, and speed/odometry scaling using `vesc.yaml`, please refer to the dedicated **[[Tuning Guide|ARCPro Tuning Guide]]**.

## Quick Summary

- **Configuration File**: `~/arcpro_system/src/base/f1tenth_to_arcpro/f1tenth_stack/config/vesc.yaml`
- **Key Parameters**:
  - `steering_angle_to_servo_offset`: Steering center trim (adjust if car drifts left/right).
  - `steering_angle_to_servo_gain`: Steering sharpness (adjust if turning circle is too wide/sharp).
  - `speed_to_erpm_gain`: Odometry & speed multiplier (adjust to match physical distance driven).

> [!tip] Quick Links
> - **Full Guide & Quickstart:** [[Tuning Guide|ARCPro Tuning Guide]]
> - **Software Setup:** [[Getting started with ARCPro software|Getting Started with ARCPro Software]]
> - **Hardware Specs:** [[ARCPro specifications|Vehicle Specifications]]