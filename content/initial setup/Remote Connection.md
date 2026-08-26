---
title: "Connecting Remotely to Your Robot"
tags:
  - arcProDocs
  - setup
  - remote
  - connection
---

# Connecting Remotely to Your ARC Pro Robot

This guide covers how students can connect to their ARC Pro robot from a laptop (Windows, macOS, or Linux). ARC Pro robots support both **terminal SSH** and **graphical Windows Remote Desktop (RDP)** without requiring Tailscale or complex campus network configurations.

> [!important] Default Student Credentials
> - **Username**: `arc`
> - **Default Robot Hotspot IP**: `192.168.4.1`
> - **Default Direct Ethernet IP**: `192.168.2.1`

---

## Connection Methods Overview

| Method | Best For | Connection Target | Configuration Needed |
| :--- | :--- | :--- | :--- |
| **[[#Option 1: Direct Wi-Fi Hotspot (Wireless)]]** | In-lab wireless testing & driving | `192.168.4.1` | Connect laptop to `ARCPRO_XX` Wi-Fi |
| **[[#Option 2: Plug-and-Play Direct Ethernet]]** | Cable connection / high bandwidth | `192.168.2.1` | Plug Ethernet cable into NUC |
| **[[#Option 3: Campus Network & Tailscale]]** | Off-campus / Remote access | `arcproX.husky-bangus.ts.net` | Requires Tailscale |

---

## Option 1: Direct Wi-Fi Hotspot (Wireless)

Every ARC Pro robot automatically broadcasts its own dedicated high-speed Wi-Fi hotspot in the lab.

### Step 1: Connect Your Laptop to the Robot's Wi-Fi
1. Open Wi-Fi settings on your laptop.
2. Select your robot's SSID:
   - **SSID Format**: `ARCPRO_02`, `ARCPRO_05`, `ARCPRO_06`, `ARCPRO_07`, `ARCPRO_08`, `ARCPRO_09`, `ARCPRO_11`
3. Enter the Wi-Fi Password:
   ```text
   arcpro1234
   ```
4. Your laptop will automatically receive an IP address (e.g., `192.168.4.100`).

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

## Option 2: Plug-and-Play Direct Ethernet (Cable)

If you prefer a physical cable connection for maximum speed and zero wireless latency:

1. Connect a standard Ethernet cable (RJ-45) from your laptop to the Intel NUC's Ethernet port (`enp89s0`).
2. The robot's built-in DHCP server will automatically assign your laptop an IP on the `192.168.2.x` subnet.
3. Connect using:
   - **SSH**: `ssh arc@192.168.2.1`
   - **Remote Desktop (RDP)**: `192.168.2.1`

> [!info] Internet Passthrough
> The robot automatically bridges internet from its campus Wi-Fi (`WIFI@OU`) to your laptop over the direct Ethernet and Hotspot connections.

---

## Option 3: Campus Network & Tailscale (Advanced)

For instructors or remote access outside the lab:
- **Tailscale Address**: `arcproX.husky-bangus.ts.net`
- **Port 22**: SSH Terminal
- **Port 3389**: Windows Remote Desktop (RDP)

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
- 🏎️ **Vehicle Calibration**: [[Tuning Guide|ARCPro Tuning Guide (Steering & Speed Calibration)]]
- 📡 **Sensors**: [[YDLidar X4 Pro and 435i realsense|Testing YDLidar & RealSense Cameras]]
- 📚 **Course Labs**: [[SP2026-VNAV-CourseContent/labs/index|VNAV Lab Exercises]]
