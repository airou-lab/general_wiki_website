---
Type:
  - arcProDocs
Labs:
  - AIROU
slug: index
---

> [!Warning] 
> Running ROS1?
> Please see our deprecated repo [here](https://airou-lab.github.io/docs/intro.html)
> 
## ARCPro Overview:
Our robotic car is designed and built to autonomously navigate unknown areas and create accurate 2D/3D maps. Also, the vehicles are capable of intra-vehicular and vehicle-to-infrastructure communication. In this tutorial, we will go through the hardware design of ARCPro first. Then the instruction to turn on the cars and hardware setup is explained step-by-step. Lastly, we instruct you to use ARCPro software to launch different sensors (e.g., LiDAR, depth camera).

# First time Setup guide:
- [[hardware]] (start here)
- [[VESC aka FSEC]]
## Software setup:
- [[YDLidar X4 Pro and 435i realsense]] 
- [[Calibrating your car]]
- [[Fusing sensors with robot_localization]]
- [[Pairing]]
## Runing the example software
- [[Using nav2 with slamtoolbox]]
- [[arcpro run commands]]
- [[arcpro waypointer example run]]


## Waypointer Repo File layout
All folders below are inside the `src` folder:
- `bridge` : A custom bridge node from ackermann drive to ackermann driveStamped (may or may not be needed)
- `f1tenth_system`: Onboard drivers built for the f1tenth race cars. The primary tools we used in the repo are:
	- `f1tenth_stack`: The main file we use for main drive commands and motor control
		- `vsec.yaml` had several changes for configuration
		- `no_lidar_bringup_launch` was used since we have our custom ydlidar
	- `Ackermann_mux` for drive messages
	- `teleop_tools`
- `merger`: Houses nav2 stack configs and main launch file that calls all other sub-launch files
- `twist_to_ackermann`: Translates our twist messages from f1tenth_stack to ackermann messages for nav2 to use
- `ylidar`: Lidar launch folder
	- we edited the folder to account for our lidar version, 
	- Additionally houses the tf2 publisher 
	- Responsible for all 
# Examples
- [[arcpro waypointer example run]] : Example waypointing in sim and irl 

Based on the following [car](https://f1tenth.readthedocs.io/en/foxy_test/getting_started/intro.html) 

# Credits 

Regarding hardware and software information for the ARC system, most information and tutorials can be found on the [MuSHR website](https://mushr.io/) which is the project ARC is derived from.

For any questions or concerns, feel free to reach out to us at:

arikak@ou.edu (Software) and dvargas88@ou.edu (Hardware & MiniCity)**.

There is also a forum for MuSHR issues located in their [GitHub organization discussions](https://github.com/prl-mushr/mushr/discussions).


## Outside Resources
Regarding the software for the MuSHR/ARC system, most information and tutorials can be found on the [MuSHR](https://mushr.io/) website or [f1tenth](https://roboracer.ai/build) site.

For any questions or concerns, feel free to reach out to Arika Khor at arikak@ou.edu. There is also a forum for MuSHR issues located in their GitHub organization discussions

For the purposes of documentation, we will only go over methods and information relevant to running the base sensors in ARC system, and anything that might be of resource to a new user 

%% Begin Waypoint %%
- [[index]]
- [[arcpro run commands]]
- [[arcpro waypointer example run]]
- [[Pairing]]
- [[original docs]]
- [[Fusing sensors with robot_localization]]
- [[hardware]]
- [[index]]
- [[YDLidar X4 Pro and 435i realsense]]
- [[Using nav2 with slamtoolbox]]
- [[VESC aka FSEC]]

%% End Waypoint %%