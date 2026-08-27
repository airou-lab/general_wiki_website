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
> - **Campus Network**: `WIFI@OU`
> - **Direct Plug-and-Play Ethernet IP**: `192.168.2.1`
> - **Default Robot Hotspot IP**: `192.168.4.1`

---

## Fleet Static IP Directory (Campus Wi-Fi)

All fleet robots authenticate to **`WIFI@OU`** with dedicated static IP assignments. Both your laptop and the robot connect to `WIFI@OU`, providing full high-speed internet access simultaneously.

| Car | Hostname | Campus Static IP | SSH Command | Remote Desktop Target |
| :--- | :--- | :--- | :--- | :--- |
| **Car 02** | `arcpro2` | `10.204.163.194` | `ssh arc@10.204.163.194` | `10.204.163.194` |
| **Car 05** | `arcpro5` | `10.204.162.140` | `ssh arc@10.204.162.140` | `10.204.162.140` |
| **Car 06** | `arcpro6` | `10.204.75.103` | `ssh arc@10.204.75.103` | `10.204.75.103` |
| **Car 07** | `arcpro7` | `10.204.88.141` | `ssh arc@10.204.88.141` | `10.204.88.141` |
| **Car 08** | `arcpro8` | `10.204.79.237` | `ssh arc@10.204.79.237` | `10.204.79.237` |
| **Car 09** | `arcpro9` | `10.204.77.17` | `ssh arc@10.204.77.17` | `10.204.77.17` |
| **Car 11** | `arcpro11` | `10.204.18.35` | `ssh arc@10.204.18.35` | `10.204.18.35` |
| **Bench** | `airou` | `10.204.11.145` | `ssh arc@10.204.11.145` | `10.204.11.145` |

*(You can also check real-time online status and latency at the lab dashboard: `http://10.204.190.207:8080`)*

---

## Method 1: Graphical Desktop via Windows Remote Desktop (RDP)

Windows Remote Desktop provides the full Ubuntu desktop GUI, pre-installed with **Zen Browser**, ROS visualizers (RViz), and terminal tools.

### Step 1: Open Remote Desktop
- **Windows**: Press `Win + R`, type `mstsc.exe`, and press Enter.
- **macOS**: Install and open **Microsoft Remote Desktop** from the Mac App Store.
- **Linux**: Use Remmina (`sudo apt install remmina remmina-plugin-rdp`).

### Step 2: Enter Connection Details
1. In the **Computer** field, enter your car's campus IP (e.g. `10.204.88.141` for Car 07).
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
# Replace with your car's static IP
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
   ssh arc@10.204.88.141
   ```
4. Click **Connect**. VS Code will open a remote workspace with file tree, terminal, and debugging tools running on the car.

---

## Method 3: Direct Plug-and-Play Ethernet Cable

For zero-network environments or direct wired debugging:

1. Connect an Ethernet cable directly between your laptop and the robot's Ethernet port (`enp89s0`).
2. The robot acts as an auto-DHCP server and assigns your laptop an IP in the `192.168.2.x` range.
3. Connect directly to static IP **`192.168.2.1`**:
   - **SSH**: `ssh arc@192.168.2.1`
   - **Remote Desktop**: Connect to `192.168.2.1` in your RDP client.

> [!tip] Simultaneous Internet
> When connected via direct Ethernet, your laptop remains connected to Wi-Fi for internet while maintaining a dedicated high-speed wired link to the robot.

---

## Method 4: Direct Wi-Fi Hotspot (Standalone / Field Mode)

For outdoor driving or standalone field testing where campus Wi-Fi is unavailable:

1. Open Wi-Fi settings on your laptop and select the car's network:
   - **SSID**: `ARCPRO_XX` (e.g. `ARCPRO_07`)
   - **Password**: `arcpro1234`
2. Connect to static IP **`192.168.4.1`**:
   - **SSH**: `ssh arc@192.168.4.1`
   - **Remote Desktop**: Connect to `192.168.4.1` in your RDP client.

---

## Method 5: Remote Access via Tailscale Mesh VPN

For remote access from off-campus locations:

1. Ensure Tailscale is active on your laptop and logged into the lab network.
2. Connect using the MagicDNS hostname:
   - **SSH**: `ssh arc@arcproX.husky-bangus.ts.net`
   - **RDP Target**: `arcproX.husky-bangus.ts.net`

---

## Turnkey Robot Verification Scripts

Once connected as the `arc` user, you can run convenience test scripts located in your home directory:

```bash
# 1. Test Drivetrain (Drives forward at 0.4 m/s for verification; Ctrl+C stops cleanly)
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
