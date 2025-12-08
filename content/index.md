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
- [[hardware]] (start here)
- [[VESC aka FSEC]]
### Software:
- [[YDLidar X4 Pro and 435i realsense]] 
- [[Calibrating your car]]
- [[Fusing sensors with robot_localization]]
- [[Pairing]]
### Runing the example software
- [[arcpro run commands | Sensor and motor drive commands]]
- [[arcpro waypointer example run | Example waypointing run commands]]
## Repository File layout
All folders below are inside the `src` folder:
- `base` Houses all code esential for driving the robot, running the lidar, and twist command conversion
	- `YDLidar`: Lidar code
	- `f1tenth_to_arcpro`: A forked repo of [f1tenth](https://github.com/f1tenth/f1tenth_system/tree/humble-devel#) repo 
	- `twist_to_ackermann`: A forked repo of the repo's name. Used to convert message types
- `examples` Houses all example projects completed on this car
	- `arc_rl_interface`: Reinforcement learning repo [[Running the Sim and sim2real]]
	- `waypointer`: - [[arcpro waypointer example run | waypointer]] : Example waypointing in sim and irl
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