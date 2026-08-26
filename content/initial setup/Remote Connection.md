---
title: "Connecting Remotely to Your Robot"
tags:
  - arcProDocs
  - setup
  - remote
  - connection
---

# Connecting Remotely to Your ARC Pro Robot

This guide covers how to connect to an ARC Pro robot from a laptop (Windows, macOS, or Linux). ARC Pro robots support both **terminal SSH** and **graphical Windows Remote Desktop (RDP)**.

> [!important] Default Robot Credentials
> - **Username**: `arc` (or your configured administrative user)
> - **Default Robot Hotspot IP**: `192.168.4.1`

---

## Connection Methods Overview

| Method | Best For | Connection Target | Configuration Needed |
| :--- | :--- | :--- | :--- |
| **[[#Option 1: Direct Wi-Fi Hotspot (Wireless)]]** | In-lab wireless testing & driving | `192.168.4.1` | Connect laptop to `ARCPRO_XX` Wi-Fi |
| **[[#Option 2: Remote Access via Tailscale / Mesh VPN]]** | Off-campus / Remote access across networks | Robot Tailscale hostname or IP | Requires Tailscale installed on client & robot |

---

## Option 1: Direct Wi-Fi Hotspot (Wireless)

Every ARC Pro robot automatically broadcasts its own dedicated high-speed Wi-Fi hotspot for direct, zero-configuration local wireless control.

### Step 1: Connect Your Laptop to the Robot's Wi-Fi
1. Open Wi-Fi settings on your laptop.
2. Select your robot's SSID:
   - **SSID Format**: `ARCPRO_02`, `ARCPRO_05`, `ARCPRO_06`, `ARCPRO_07`, `ARCPRO_08`, `ARCPRO_09`, `ARCPRO_11` (or your configured hotspot name)
3. Enter the Wi-Fi Password:
   ```text
   arcpro1234
   ```
4. Your laptop will automatically receive an IP address on the `192.168.4.x` subnet.

---

### Step 2A: Connect via Terminal (SSH)
Open your terminal (macOS/Linux) or PowerShell / Command Prompt (Windows) and run:

```bash
ssh arc@192.168.4.1
```

*(You can also use `ssh arc@arcpro2.local` if your OS supports mDNS).*

---

### Step 2B: Connect via Windows Remote Desktop (GUI Desktop)
To access the full Ubuntu graphical desktop (including **Zen Browser**, visual tools, and GUI terminals):

1. On Windows, open **Remote Desktop Connection** (`mstsc.exe`).
   - *(On macOS, install and open Microsoft Remote Desktop from the App Store).*
2. In the **Computer** field, enter:
   ```text
   192.168.4.1
   ```
3. Click **Connect**.
4. When prompted by XRDP:
   - **Session**: `Xorg`
   - **Username**: `arc`
   - **Password**: *(your robot user password)*
5. The full Ubuntu desktop environment opens directly on your laptop screen!

> [!tip] Default Web Browser
> The desktop is pre-configured with **Zen Browser** as the default browser for reviewing course docs, documentation, and web visualizers.

---

## Option 2: Remote Access via Tailscale / Mesh VPN

For remote access over campus networks, off-campus locations, or across different Wi-Fi subnets without port forwarding or firewall hassles, ARC Pro robots can be accessed using **Tailscale** (a zero-config WireGuard-based mesh VPN).

### General Setup for Replicating the System

If you are setting up or replicating this robotics platform on your own machine or fleet:

1. **Install Tailscale on the Robot**:
   ```bash
   curl -fsSL https://tailscale.com/install.sh | sh
   sudo tailscale up
   ```
2. **Install Tailscale on Your Laptop/Client**:
   - Download and install Tailscale from [tailscale.com/download](https://tailscale.com/download) for your OS (Windows, macOS, Linux, iOS, Android).
   - Sign in to the same Tailscale account.
3. **Obtain Robot Tailscale IP / Hostname**:
   - Run `tailscale ip -4` or `tailscale status` on the robot, or check your Tailscale admin console.
   - Tailscale assigns a stable 100.x.y.z IP address and a MagicDNS name (e.g., `robot-name.your-tailnet.ts.net`).

### Connecting via Tailscale

Once both your laptop and robot are connected to your Tailscale network:

- **SSH Terminal Access**:
  ```bash
  ssh <username>@<tailscale-ip-or-magicdns>
  ```
- **Remote Desktop (RDP / XRDP)**:
  Enter the robot's Tailscale IP or MagicDNS domain into Remote Desktop Connection (`mstsc.exe` or macOS Microsoft Remote Desktop).

> [!note] AIROU Lab Fleet Example
> For students and lab members using the pre-configured lab fleet:
> - **Tailscale Address Format**: `arcproX.husky-bangus.ts.net` (where `X` is your robot number, e.g., `arcpro2.husky-bangus.ts.net`)
> - **SSH**: `ssh arc@arcproX.husky-bangus.ts.net`
> - **RDP Target**: `arcproX.husky-bangus.ts.net`

---

## Quick Out-of-the-Box Verification Scripts

Once connected as the `arc` user, you can run convenience scripts located directly in `~`:

```bash
# 1. Test Drivetrain (Drives forward at 0.4 m/s for verification)
./straight.sh

# 2. Test Odometry / Drive Command Publishing
./mockodom.sh

# 3. Clean up and terminate all running ROS processes
./killall.sh
```

---

## Next Steps
- **Vehicle Calibration**: [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- **Sensors**: [[YDLidar X4 Pro and 435i realsense|Testing YDLidar & RealSense Cameras]]
- **Course Labs**: [[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]
