---
Type:
  - arcProDocs
Labs:
  - AIROU
---
For building the files, see the [[setup/building your bot/index|STL folder]]
# Hardware build and specs guide
## Onboard Hardware  Specs
ARCPro Main Components: 
- Intel NUC Processor
- 2D LiDAR ([YDLIDAR X4PRO](https://www.ydlidar.com/product/ydlidar-x4-pro) )
- [Intel D435i RGB-D Camera](https://realsenseai.com/products/depth-camera-d435i/) 
- Servo Motor
- Controller VESC
	- [FLIPSKY Electric Speed Controller for Skateboard Mini FSESC4.20 50A Base on ESC® 4.12 with Aluminum Anodized Heat Sink 12s esc](https://www.amazon.com/Flipsky-Electric-Controller-Skateboard-FSESC4-20/dp/B08725X8CT)
## Initial Boot-up: 
- Plug VESC battery  to VESC  (Front wheels should “lock” when VESC is plugged in and you may hear a sound) 
- Plug NUC battery to power convertor.
- Plugin NUC.
- Turn on the intel NUC by pushing the power button on the front. The NUC will turn on and you will see the lidar on the top starts spinning!
- The connector to connect the VESC battery
- The connector for connecting NUC battery
- After you connect the batteries:
## Connecting to the NUC:
- **Remotely (Wi-Fi Hotspot or Direct Ethernet)**: See the complete guide at **[[Remote Connection|Connecting Remotely to Your Robot (Hotspot, SSH & Windows RDP)]]**.
  - **Wi-Fi Hotspot**: Connect to `ARCPRO_XX` (Password: `arcpro1234`) and connect to `192.168.4.1` via SSH or Windows Remote Desktop.
  - **Direct Ethernet**: Plug an Ethernet cable into the NUC and connect to `192.168.2.1`.
- **Directly (Physical Monitor)**: You may connect a monitor (HDMI), keyboard, and mouse directly to the NUC in the lab.
## How to shut down the race car: 
1. To shut down the system, press the power button in NUC. Please do not hold it! Otherwise, it damages the NUC over the time 
2.  Unplug the NUC cable
3. Unplug the NUC batter
4. Unplug the VESC battery 


Next steps:
[[VESC aka FSEC]]
