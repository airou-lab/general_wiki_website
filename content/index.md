---
Type:
  - arcProDocs
Labs:
  - AIROU
slug: index
title: ARCPro Docs Home
---
Our robotic car is designed and built to autonomously navigate unknown areas and create accurate 2D/3D maps. Also, the vehicles are capable of intra-vehicular and vehicle-to-infrastructure communication. In this tutorial, we will go through the hardware design of ARCPro first. Then the instruction to turn on the cars and hardware setup is explained step-by-step. Lastly, we instruct you to use ARCPro software to launch different sensors (e.g., LiDAR, depth camera).

> [!Warning] 
> Running ROS1?
> Please see our deprecated ROS 1 Documentation [here](https://airou-lab.github.io/docs/intro.html)

> [!Warning]
> This site is still under construction, and as such some page links may be missing or hidden
## First time Setup guide:
- [Hardware Setup](initial%20setup/hardware.md) (start here)
- [VESC aka FSEC](initial%20setup/VESC%20aka%20FSEC.md)
### Software Setup:
- [Getting Started with ARCPro Software](initial%20setup/Getting%20started%20with%20ARCPro%20software.md) (start here)
- [ARCPro Tuning Guide (Steering & Speed Calibration)](initial%20setup/Tuning%20Guide.md)
- [YDLidar X4 Pro and 435i realsense](initial%20setup/YDLidar%20X4%20Pro%20and%20435i%20realsense.md) 
- [Bluetooth Gamepad Pairing](initial%20setup/Pairing.md)
- [Fusing sensors with robot_localization](waypointer/guides/Fusing%20sensors%20with%20robot_localization.md)
### Running the example software
- [Sensor and motor drive commands](initial%20setup/arcpro%20run%20commands.md)
- [Example waypointing run commands](waypointer/arcpro%20waypointer%20example%20run.md)
## Repository File layout
All folders below are inside the `src` folder:
- `base` Houses all code esential for driving the robot, running the lidar, and twist command conversion
	- `YDLidar`: Lidar code
	- `f1tenth_to_arcpro`: A forked repo of [f1tenth](https://github.com/f1tenth/f1tenth_system/tree/humble-devel#) repo 
	- `twist_to_ackermann`: A forked repo of the repo's name. Used to convert message types
- `examples` Houses all example projects completed on this car
	- `arc_rl_interface`: Reinforcement learning repo [Running the Sim and sim2real](passive%20reinforcement%20learning/Running%20the%20Sim%20and%20sim2real.md)
	- `waypointer`: - [waypointer](waypointer/arcpro%20waypointer%20example%20run.md) : Example waypointing in sim and irl
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
- [index](initial%20setup/index.md)
- [arcpro run commands](initial%20setup/arcpro%20run%20commands.md)
- [arcpro waypointer example run](waypointer/arcpro%20waypointer%20example%20run.md)
- [Pairing](initial%20setup/Pairing.md)
- [original docs](initial%20setup/original%20docs.md)
- [Fusing sensors with robot_localization](waypointer/guides/Fusing%20sensors%20with%20robot_localization.md)
- [hardware](initial%20setup/hardware.md)
- [index](initial%20setup/index.md)
- [YDLidar X4 Pro and 435i realsense](initial%20setup/YDLidar%20X4%20Pro%20and%20435i%20realsense.md)
- [Using nav2 with slamtoolbox](waypointer/guides/Using%20nav2%20with%20slamtoolbox.md)
- [VESC aka FSEC](initial%20setup/VESC%20aka%20FSEC.md)

%% End Waypoint %%