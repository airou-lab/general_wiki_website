---
title: "Connecting Remotely to Your Robot"
tags:
  - arcProDocs
  - setup
  - remote
  - connection
---

# Connecting Remotely to Your ARC Pro Robot

This guide covers how to connect to an ARC Pro robot from a laptop (Windows, macOS, or Linux). ARC Pro robots support both **terminal SSH** and **graphical Windows Remote Desktop (RDP)** across campus Wi-Fi, direct Ethernet, local robot hotspots, and Tailscale VPN.

> [!important] Default Robot Credentials
> - **Username**: `arc`
> - **Password**: `arcpro1234`
> - **Direct Plug-and-Play Ethernet IP**: `192.168.2.1`
> - **Default Robot Hotspot IP**: `192.168.4.1`

---

## Connection Methods Overview

| Method | Best For | Target Address | Requirements |
| :--- | :--- | :--- | :--- |
| **[[#Option 1: Campus Wi-Fi & Live Fleet Board (Recommended)]]** | In-lab classwork with full internet | Live Campus IP (e.g. `10.204.x.x`) via Fleet Board | Connect laptop to `WIFI@OU` |
| **[[#Option 2: Direct Plug-and-Play Ethernet Cable]]** | Instant zero-setup wired link | `192.168.2.1` | RJ45 Ethernet cable plugged into robot |
| **[[#Option 3: Direct Wi-Fi Hotspot (Wireless)]]** | Field testing & isolated driving | `192.168.4.1` | Connect laptop to `ARCPRO_XX` Wi-Fi |
| **[[#Option 4: Remote Access via Tailscale Mesh VPN]]** | Off-campus / remote lab work | `arcproX.husky-bangus.ts.net` | Tailscale client installed on laptop |

---

## Option 1: Campus Wi-Fi & Live Fleet Board (Recommended for Students)

When working in the robotics lab, both your laptop and the robots connect directly to campus Wi-Fi (**`WIFI@OU`**). This provides full high-speed internet access to both your laptop and the robot simultaneously.

### Step 1: Open the Live Fleet Status Board
1. Connect your laptop to **`WIFI@OU`**.
2. Open your web browser and navigate to the lab status board:
   - **Lab Board**: `http://fleet.yourdomain.fyi` *(or `http://10.204.190.207:8080`)*
3. The board displays real-time status, live campus IP addresses, and ping latency for all fleet robots.

### Step 2: Connect via Terminal (SSH)
Find your assigned car on the dashboard and click **Copy SSH**, or run in your terminal:

```bash
ssh arc@<car-campus-ip>
# Example: ssh arc@10.204.88.141
```

When prompted, enter the password: `arcpro1234`.

### Step 3: Connect via Windows Remote Desktop (GUI Desktop)
To access the full Ubuntu graphical desktop (including **Zen Browser**, visualizer tools, and GUI terminals):

1. On Windows, open **Remote Desktop Connection** (`mstsc.exe`).
   *(On macOS, open Microsoft Remote Desktop).*
2. In the **Computer** field, enter your car's campus IP:
   ```text
   <car-campus-ip>
   ```
3. Click **Connect**.
4. When prompted by XRDP:
   - **Session**: `Xorg`
   - **Username**: `arc`
   - **Password**: `arcpro1234`

---

## Option 2: Direct Plug-and-Play Ethernet Cable

Every ARC Pro robot includes an auto-DHCP shared network server on its Ethernet port (`enp89s0`).

1. Connect an Ethernet cable directly between your laptop and the robot's Ethernet port.
2. Your laptop automatically receives an IP address on the `192.168.2.x` subnet.
3. Connect immediately to static IP **`192.168.2.1`**:
   - **SSH**: `ssh arc@192.168.2.1`
   - **Remote Desktop**: Connect to `192.168.2.1` in your RDP client.

> [!tip] Simultaneous Internet Access
> When using direct Ethernet, your laptop can remain connected to `WIFI@OU` for internet while maintaining a dedicated high-bandwidth wired link to the robot.

---

## Option 3: Direct Wi-Fi Hotspot (Wireless Standalone)

For field testing, outdoor racing, or standalone use where campus Wi-Fi is unavailable:

### Step 1: Connect to Robot Wi-Fi
1. Open Wi-Fi settings on your laptop.
2. Select your robot's SSID:
   - **SSID Format**: `ARCPRO_02`, `ARCPRO_05`, `ARCPRO_06`, `ARCPRO_07`, `ARCPRO_08`, `ARCPRO_09`, `ARCPRO_11`
3. Enter the Wi-Fi Password:
   ```text
   arcpro1234
   ```
4. Your laptop receives an IP address on the `192.168.4.x` subnet.

### Step 2: Remote In
- **SSH**: `ssh arc@192.168.4.1`
- **Remote Desktop**: Connect to `192.168.4.1` in your RDP client.

---

## Option 4: Remote Access via Tailscale Mesh VPN

For remote access over external networks or across campus subnets:

### Connecting via Tailscale
Once both your laptop and robot are logged into the Tailscale network:

- **SSH Terminal Access**:
  ```bash
  ssh arc@arcproX.husky-bangus.ts.net
  # Example: ssh arc@arcpro7.husky-bangus.ts.net
  ```
- **Remote Desktop (RDP)**:
  Enter `arcproX.husky-bangus.ts.net` into Remote Desktop Connection.

---

## Out-of-the-Box Robot Verification Scripts

Once connected as the `arc` user, you can run convenience scripts located directly in `~`:

```bash
# 1. Test Drivetrain (Drives forward at 0.4 m/s for verification; Ctrl+C cleanly stops)
./straight.sh

# 2. Test Odometry / Drive Command Publishing
./mockodom.sh

# 3. Clean up and terminate all running ROS processes and shared memory
./killall.sh
```

---

## Next Steps
- **Vehicle Calibration**: [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- **Sensors**: [[YDLidar X4 Pro and 435i realsense|Testing YDLidar & RealSense Cameras]]
- **Course Labs**: [[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]
