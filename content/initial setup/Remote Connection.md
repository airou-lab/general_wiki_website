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

This guide covers how to connect to an ARC Pro robot from a laptop (Windows, macOS, or Linux). ARC Pro robots support both **terminal SSH** and **graphical Windows Remote Desktop (RDP)** across campus Wi-Fi and local robot hotspots.

> [!important] Default Robot Credentials
> - **Username**: `arc`
> - **Password**: `arcpro1234`
> - **Campus Network**: `WIFI@OU`
> - **Default Robot Hotspot IP**: `192.168.4.1`

---

## Quickstart: Remoting In (In 30 Seconds)

Most students connect from their laptops using **Windows Remote Desktop** (graphical desktop) or **Terminal SSH**:

### Option 1: Graphical Desktop (Recommended)
1. **Power On**: Ensure the robot battery is connected and the Intel NUC power LED is lit. Ensure your laptop is connected to **`WIFI@OU`**.
2. **Launch Remote Desktop**:
   - **Windows**: Press `Win + R`, type `mstsc.exe`, and press Enter.
   - **macOS**: Open **Microsoft Remote Desktop**.
3. **Connect**:
   - In the **Computer** field, enter your car's campus DNS hostname or static IP:
     ```text
     arc7.cs.nor.ou.edu
     ```
     *(Replace `7` with your vehicle number, e.g. `arc9.cs.nor.ou.edu` for Car 9, or enter `10.194.16.54`).*
4. **Log In**:
   - **Username**: `arc`
   - **Password**: `arcpro1234`
5. The full Ubuntu desktop opens in a window on your screen. You are now inside the robot! Proceed to [[Pairing|Step 2: Gamepad Controller Pairing]].

### Option 2: Terminal SSH (Fast & Lightweight)
Open PowerShell, Command Prompt, or terminal and run:
```bash
ssh arc@arc7.cs.nor.ou.edu
```
*(Or directly using the IP: `ssh arc@10.194.16.54`).*

When prompted, enter password `arcpro1234`. You are now inside the robot's command line!

---

## Fleet Hostname & Connection Directory

> [!important] Campus Network vs Robot Hotspot
> - **On Campus Wi-Fi (`WIFI@OU`)**: Always connect using the official campus DNS hostname (**`arcX.cs.nor.ou.edu`**) or the vehicle's **Campus Static IP** (`10.194.16.XX`). Enterprise Wi-Fi filters multicast DNS (`.local`), so `arcproX.local` will not resolve across campus access points.
> - **On Robot Hotspot (`ARCPRO_XX`)**: When connected directly to the car's standalone Wi-Fi hotspot in the field or outdoor track, connect via `arcproX.local` or `192.168.4.1`.

| Car | Campus Hostname (Primary) | SSH Command | Remote Desktop Target | Campus Static IP |
| :--- | :--- | :--- | :--- | :--- |
| **Car 01** | `arc1.cs.nor.ou.edu` | `ssh arc@arc1.cs.nor.ou.edu` | `arc1.cs.nor.ou.edu` | `10.194.16.48` |
| **Car 02** | `arc2.cs.nor.ou.edu` | `ssh arc@arc2.cs.nor.ou.edu` | `arc2.cs.nor.ou.edu` | `10.194.16.49` |
| **Car 03** | `arc3.cs.nor.ou.edu` | `ssh arc@arc3.cs.nor.ou.edu` | `arc3.cs.nor.ou.edu` | `10.194.16.50` |
| **Car 04** | `arc4.cs.nor.ou.edu` | `ssh arc@arc4.cs.nor.ou.edu` | `arc4.cs.nor.ou.edu` | `10.194.16.51` |
| **Car 05** | `arc5.cs.nor.ou.edu` | `ssh arc@arc5.cs.nor.ou.edu` | `arc5.cs.nor.ou.edu` | `10.194.16.52` |
| **Car 06** | `arc6.cs.nor.ou.edu` | `ssh arc@arc6.cs.nor.ou.edu` | `arc6.cs.nor.ou.edu` | `10.194.16.53` |
| **Car 07** | `arc7.cs.nor.ou.edu` | `ssh arc@arc7.cs.nor.ou.edu` | `arc7.cs.nor.ou.edu` | `10.194.16.54` |
| **Car 08** | `arc8.cs.nor.ou.edu` | `ssh arc@arc8.cs.nor.ou.edu` | `arc8.cs.nor.ou.edu` | `10.194.16.55` |
| **Car 09** | `arc9.cs.nor.ou.edu` | `ssh arc@arc9.cs.nor.ou.edu` | `arc9.cs.nor.ou.edu` | `10.194.16.56` |
| **Car 10** | `arc10.cs.nor.ou.edu` | `ssh arc@arc10.cs.nor.ou.edu` | `arc10.cs.nor.ou.edu` | `10.194.16.57` |
| **Car 11** | `arc11.cs.nor.ou.edu` | `ssh arc@arc11.cs.nor.ou.edu` | `arc11.cs.nor.ou.edu` | `10.194.16.58` |

---

## Method 1: Graphical Desktop via Windows Remote Desktop (RDP)

Windows Remote Desktop provides the full Ubuntu desktop GUI, pre-installed with **Zen Browser**, ROS visualizers (RViz), and terminal tools.

### Step 1: Open Remote Desktop
- **Windows**: Press `Win + R`, type `mstsc.exe`, and press Enter.
- **macOS**: Install and open **Microsoft Remote Desktop** from the Mac App Store.
- **Linux**: Use Remmina (`sudo apt install remmina remmina-plugin-rdp`).

### Step 2: Enter Connection Details
1. In the **Computer** field, enter your car's campus DNS hostname:
   ```text
   arc7.cs.nor.ou.edu
   ```
   *(Or enter the campus static IP, e.g. `10.194.16.54`).*
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
# Connect using the campus DNS hostname:
ssh arc@arc7.cs.nor.ou.edu

# Or connect directly via the campus static IP:
ssh arc@10.194.16.54
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
   ssh arc@arc7.cs.nor.ou.edu
   ```
4. Click **Connect**. VS Code will open a remote workspace with file tree, terminal, and debugging tools running on the car.

---

---

## Method 3: Direct Wi-Fi Hotspot (Standalone / Field Mode)

For outdoor driving or standalone field testing where campus Wi-Fi is unavailable:

1. Open Wi-Fi settings on your laptop and select the car's network:
   - **SSID**: `ARCPRO_XX` (e.g. `ARCPRO_07`)
   - **Password**: `arcpro1234`
2. Connect directly:
   - **SSH**: `ssh arc@arcproX.local` *(or `ssh arc@192.168.4.1`)*
   - **Remote Desktop**: Connect to `arcproX.local` *(or `192.168.4.1`)* in your RDP client.

---

## Remote Connection Troubleshooting

### Issue 1: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`
- **Symptom**: When connecting via SSH, OpenSSH prints a warning banner and aborts with `Host key verification failed`.
- **Cause**: The robot was reflashed or updated, generating a new ED25519 host key. Your laptop has the older key cached in `~/.ssh/known_hosts`.
- **Fix**: Clear the cached host key on your personal laptop (run in PowerShell, Command Prompt, or Terminal):
  ```bash
  ssh-keygen -R arc7.cs.nor.ou.edu
  ssh-keygen -R 10.194.16.54
  ```
  *(Replace `7` / `10.194.16.54` with your vehicle number and IP).*

### Issue 2: `Could not resolve hostname` or `NXDOMAIN`
- **Symptom**: Running `ssh arc@arc7.cs.nor.ou.edu` returns `Name or service not known` or `Temporary failure in name resolution`.
- **Cause**: 
  1. Your laptop is configured with third-party public DNS (such as Google `8.8.8.8`, Cloudflare `1.1.1.1`, or NextDNS) or a personal VPN (NordVPN, Mullvad, etc.). Public DNS resolvers do not know internal university `.ou.edu` records.
  2. You are connected to `OU-Guest` rather than `WIFI@OU`.
- **Fix**:
  1. Connect directly using the robot's **Campus Static IP** (bypasses DNS entirely):
     ```bash
     ssh arc@10.194.16.54
     ```
  2. Ensure your laptop is connected to **`WIFI@OU`**, and disconnect any personal third-party VPN clients.

### Issue 3: Connection Timed Out
- **Symptom**: `ssh` or Windows Remote Desktop hangs and prints `connect to host ... port 22: Connection timed out`.
- **Cause**:
  1. The vehicle is powered off or its battery has depleted. Verify the Intel NUC power LED is lit blue.
  2. Your laptop is connected to an isolated guest network (`OU-Guest`), which firewalls off campus robot subnets. Connect to `WIFI@OU`.

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

## Navigation

| Previous Step | Current Step | Next Step |
| :--- | :--- | :--- |
| *(Start of Onboarding)* | **Step 1: Connecting Remotely** | [[Pairing\|Step 2: Controller Pairing &rarr;]] |

