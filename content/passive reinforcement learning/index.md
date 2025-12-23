---
Type:
  - arcProDocs
Labs:
  - AIROU
slug: index
title: ARCPro Docs Home
---
> [!Warning] Content still under development!
  > Try at your own risk! 

- Repo link:  [airou-lab/arc_rl_interface](https://github.com/airou-lab/arc_rl_interface/tree/main)
- For [[Methodology]]
# Passive Camera only RL navigation
Train and evaluate a recurrent policy (RecurrentPPO with CNN+LSTM) that learns autonomous maneuvers from RGB frames only streaming from a Unity mini‑city. No semantic masks, optical flow, handcrafted path planners, or action blending — purely passive visual navigation.
# Run model to real world bridge.
We've provided a simple script to run a trained model on the robot. Simply run the  `/arcpro_rl.sh` in the project's home directory like so 
```bash
./arcpro_rl.sh
```
Inside you will find it calls upon a certain script 
# Run the unity sim model
Running the model is a bit more complex. Currently, we use 
- Unity version 6000.3.1f1 

TODO CONTINUE MODEL RUN SETUP FROM SCRATCH!


Our submodel is linked as so: [https://github.com/airou-lab/arc_rl_interface]()
