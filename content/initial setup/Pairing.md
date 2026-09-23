---
Type:
  - arcProDocs
Labs:
  - AIROU
---

# Bluetooth Controller Pairing (ARC Pro)

> [!info] ARC Pro Student Onboarding: Step 2 of 5
> Previous: [[Remote Connection|Step 1: Connecting Remotely]]. Next: [[Getting started with ARCPro software|Step 3: Software Bringup & First Drive]].

> [!important] Prerequisite: Remote Session Active
> Ensure you have remoted into your robot via [[Remote Connection|Step 1: Connecting Remotely]] before running these commands.
>
> You must run `bluetoothctl` **inside the robot's terminal** (via SSH or within Windows Remote Desktop), not on your personal laptop.

This guide covers pairing a Sony DualShock or compatible Bluetooth wireless gamepad controller with the ARC Pro robot onboard Intel NUC.

---

## 1. Bluetooth Pairing Procedure

### Option A: Turnkey Pairing Wizard (Recommended)

On fleet robots, run the turnkey pairing script in your robot terminal:
```bash
pair_controller
# or: bash ~/example_scripts/pair_controller.sh
```
Follow the interactive prompts:
1. Put your controller into pairing mode: Press and hold the **Share** button and the **Center PS** button simultaneously for ~5 seconds until the lightbar blinks rapidly.
2. The script will automatically scan, pair, trust, and connect your controller.
3. Once connected, it verifies `/dev/input/js0`.

### Option B: Manual Pairing via `bluetoothctl`

1. Open a terminal session on the robot and start `bluetoothctl`:
   ```bash
   bluetoothctl
   ```

2. Put your controller into pairing mode:
   - Press and hold the **Share** button and the **Center PS** button simultaneously for approximately 5 seconds until the lightbar rapidly blinks.

3. Start scanning for Bluetooth devices:
   ```text
   [bluetooth]# agent on
   [bluetooth]# default-agent
   [bluetooth]# scan on
   ```

4. Locate your controller MAC address in the scan output (named "Wireless Controller"):
   ```text
   [CHG] Device BB:8E:41:F5:5D:C7 Name: Wireless Controller  
   [CHG] Device BB:8E:41:F5:5D:C7 Alias: Wireless Controller  
   ```

5. Pair, trust, and connect to the controller:
   ```text
   [bluetooth]# pair BB:8E:41:F5:5D:C7
   [bluetooth]# trust BB:8E:41:F5:5D:C7
   [bluetooth]# connect BB:8E:41:F5:5D:C7
   [bluetooth]# scan off
   [bluetooth]# exit
   ```

6. Verify that the Linux joystick device is recognized:
   ```bash
   ls -l /dev/input/js*
   ```
   The device node `/dev/input/js0` should now be present.

---

## 2. Running Teleoperation

Once your controller is paired and connected:

### Option A: Using the Turnkey Shell Alias
```bash
teleop
```
Hold `L1` or `LB` (deadman switch) while moving the left stick (throttle) and right stick (steering).

### Option B: Using Direct ROS 2 Launch Commands
```bash
# Terminal 1: Bring up the VESC motor driver
ros2 launch f1tenth_teleop vesc.launch.py

# Terminal 2: Launch teleop node pointing to the joystick interface
ros2 launch f1tenth_teleop teleop.launch.py joy_dev:=/dev/input/js0
```

---

## Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| [[Remote Connection\|&larr; Step 1: Connecting Remotely]] | **Step 2: Controller Pairing** | [[Getting started with ARCPro software\|Step 3: First Drive &rarr;]] |