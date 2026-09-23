---
title: "Connecting Remotely to Your Robot"
tags:
  - arcProDocs
  - setup
  - remote
  - connection
---

# Connecting Remotely to Your ARC Pro Robot

> [!info] ARC Pro Student Onboarding: Step 1 of 5
> This is **Step 1** in the student setup sequence. After connecting, proceed to [[Pairing|Step 2: Gamepad Controller Pairing]].

This guide covers how to connect to an ARC Pro robot from a laptop (Windows, macOS, or Linux). ARC Pro robots support both **terminal SSH** and **graphical Windows Remote Desktop (RDP)** across campus Wi-Fi, direct Ethernet, and local robot hotspots.

> [!important] Default Robot Credentials
> - **Username**: `arc`
> - **Password**: `arcpro1234`
> - **Campus Network**: `WIFI@OU`
> - **Direct Plug-and-Play Ethernet IP**: `192.168.2.1`
> - **Default Robot Hotspot IP**: `192.168.4.1`

---

## Fleet Hostname & Connection Directory

You do not need to type or memorize numeric IP addresses. ARC Pro robots broadcast their hostname across the network. You can connect directly using the robot's name (`arcproX.local` or `arcproX`). The campus static IP is provided as an optional fallback.

| Car | Hostname (Primary Target) | SSH Command | Remote Desktop Target | Campus Static IP (Fallback) |
| :--- | :--- | :--- | :--- | :--- |
| **Car 02** | `arcpro2.local` *(or `arcpro2`)* | `ssh arc@arcpro2.local` | `arcpro2.local` | `10.204.163.194` |
| **Car 05** | `arcpro5.local` *(or `arcpro5`)* | `ssh arc@arcpro5.local` | `arcpro5.local` | `10.204.162.140` |
| **Car 06** | `arcpro6.local` *(or `arcpro6`)* | `ssh arc@arcpro6.local` | `arcpro6.local` | `10.204.75.103` |
| **Car 07** | `arcpro7.local` *(or `arcpro7`)* | `ssh arc@arcpro7.local` | `arcpro7.local` | `10.204.88.141` |
| **Car 08** | `arcpro8.local` *(or `arcpro8`)* | `ssh arc@arcpro8.local` | `arcpro8.local` | `10.204.79.237` |
| **Car 09** | `arcpro9.local` *(or `arcpro9`)* | `ssh arc@arcpro9.local` | `arcpro9.local` | `10.204.77.17` |
| **Car 11** | `arcpro11.local` *(or `arcpro11`)* | `ssh arc@arcpro11.local` | `arcpro11.local` | `10.204.18.35` |
| **Bench** | `airou.local` *(or `airou`)* | `ssh arc@airou.local` | `airou.local` | `10.204.11.145` |

*(You can also check real-time online status and latency at the lab dashboard: `http://10.204.190.207:8080`)*

---

## Method 1: Graphical Desktop via Windows Remote Desktop (RDP)

Windows Remote Desktop provides the full Ubuntu desktop GUI, pre-installed with **Zen Browser**, ROS visualizers (RViz), and terminal tools.

### Step 1: Open Remote Desktop
- **Windows**: Press `Win + R`, type `mstsc.exe`, and press Enter.
- **macOS**: Install and open **Microsoft Remote Desktop** from the Mac App Store.
- **Linux**: Use Remmina (`sudo apt install remmina remmina-plugin-rdp`).

### Step 2: Enter Connection Details
1. In the **Computer** field, enter your car's hostname (e.g. `arcpro7.local` or `arcpro7`).
   *(If your network does not resolve mDNS names, you can alternatively enter your car's campus static IP, e.g. `10.204.88.141`).*
2. Click **Connect**.

### Step 3: Accept Certificate Warning
If prompted with a certificate verification warning ("The identity of the remote computer cannot be verified"), check the box for **"Don't ask me again for connections to this computer"** and click **Yes / Connect**.

### Step 4: Login at the XRDP Prompt
When the green/blue XRDP login screen appears:
- **Session**: `Xorg`
- **Username**: `arc`
- **Password**: `arcpro1234`
- Click **OK**.

The full graphical desktop environment will open on your screen.

---

## Method 2: Command Line Terminal (SSH)

### Standard Terminal Connection
Open PowerShell, Command Prompt, or terminal (macOS/Linux) and connect:

```bash
# Connect directly using the robot hostname:
ssh arc@arcpro7.local

# Or if your OS resolves short names:
ssh arc@arcpro7

# (Fallback if hostname resolution is unavailable on campus Wi-Fi)
ssh arc@10.204.88.141
```

When prompted:
1. If connecting for the first time, type `yes` to accept the SSH host fingerprint.
2. Enter the password: `arcpro1234`.

### VS Code Remote - SSH Setup
To edit code directly on the robot inside VS Code on your laptop:
1. Install the **Remote - SSH** extension in VS Code.
2. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and select **Remote-SSH: Add New SSH Host...**.
3. Enter:
   ```text
   ssh arc@arcpro7.local
   ```
4. Click **Connect**. VS Code will open a remote workspace with file tree, terminal, and debugging tools running on the car.

---

## Method 3: Direct Plug-and-Play Ethernet Cable

For zero-network environments or direct wired debugging:

1. Connect an Ethernet cable directly between your laptop and the robot's Ethernet port (`enp89s0`).
2. The robot acts as an auto-DHCP server and assigns your laptop an IP in the `192.168.2.x` range.
3. Connect directly:
   - **SSH**: `ssh arc@arcproX.local` *(or `ssh arc@192.168.2.1`)*
   - **Remote Desktop**: Connect to `arcproX.local` *(or `192.168.2.1`)* in your RDP client.

> [!tip] Simultaneous Internet
> When connected via direct Ethernet, your laptop remains connected to Wi-Fi for internet while maintaining a dedicated high-speed wired link to the robot.

---

## Method 4: Direct Wi-Fi Hotspot (Standalone / Field Mode)

For outdoor driving or standalone field testing where campus Wi-Fi is unavailable:

1. Open Wi-Fi settings on your laptop and select the car's network:
   - **SSID**: `ARCPRO_XX` (e.g. `ARCPRO_07`)
   - **Password**: `arcpro1234`
2. Connect directly:
   - **SSH**: `ssh arc@arcproX.local` *(or `ssh arc@192.168.4.1`)*
   - **Remote Desktop**: Connect to `arcproX.local` *(or `192.168.4.1`)* in your RDP client.

---

## Turnkey Robot Verification & Driving Commands

Once connected as the `arc` user, you can run convenience commands directly from any terminal:

```bash
# 1. Teleoperation & Driving
move_forward   # Drivetrain forward test at 0.4 m/s (auto-stops on Ctrl+C)
teleop         # Gamepad teleop (Hold L1/LB + left stick throttle, right stick steer)
teleop_key     # Interactive keyboard teleop in terminal

# 2. Sensors, SLAM & Telemetry
lidar          # Standalone YDLidar X4 Pro (/scan)
camera         # Standalone Intel RealSense D435i
slam           # Real-time SLAM Toolbox 2D mapping (/scan + VESC odom -> /map)
telemetry      # Foxglove Bridge (:8765), LiDAR, and RealSense camera streaming

# 3. Clean up and terminate all running ROS processes and shared memory
killall        # (or: killall_nodes)
```

---

---

## Navigation
| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| *(Start of Onboarding)* | **Step 1: Connecting Remotely** | **[[Pairing|Step 2: Controller Pairing &rarr;]]** |
