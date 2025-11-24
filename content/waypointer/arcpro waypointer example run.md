# Run commands
## Run with map
- `colcon build + source`
- `bridge`
- `lidar`

Lidar currently cant be brought up due to race condition (i think). Check nav2.yaml for the current map being used, they should be stored in the /res folder.

## Run SLAM
We bringup in isolation, to build the lidar map we have:
- `vesc`
- `lidar`
- `joy`
```bash
ros2 bag record -o name --topics /scan /tf /tf_static /odom
```

To replay and make the slam:
```bash
ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/home/airou/PycharmProjects/arcpro_rl_base_case_waypointer/src/merger/config/slam_toolbox_params.yaml

# in another terminal

ros2 bag play name --clock
```

when finished run
```bash

ros2 run nav2_map_server map_saver_cli -f ~/my_new_map
```

See [[Slam Toolbox]] about some issues I ran into when attempting to run (due to odom configs)

# Slam settings adjusted:
- Relative path settings: `src/merger/config/slam_toolbox_params.yaml`

We use [[ceres_scan_matcher]] to match scans to map with slamtoolbox to create our initial map. We adjusted the settings to distrust the odometry as there was much issue with turning and keeping the same estimated pose (the graph would fracture like in [[Slam Toolbox]]).. We also vastly increased the occupied space weight so localizing within the /scan topic weight was increased. Loop closure was decreased slightly, but the minimum travel distance and orientation was vastly decresed to match the faulty  odom topic. Given we were brute forcing the laser scan localization, we set these distances to be very short, and throttle scans to be quite low (at 2)

The package [[robot_localization]] was used to create our fused odom topic, which used the realsense IMU and motor encoders on our robot. We tried using pure IMU though it resulted in horrible x-y axis localization. 

```yaml
 do_loop_closing: true  
    loop_search_maximum_distance: 10.0  # (meters) How far to search for a loop closure.  
    minimum_travel_distance: 0.008        # (meters) Min distance robot must travel to add a new node.  
    minimum_travel_heading: 0.09  
  
 #me used this last time  
#    minimum_travel_distance: 0.05       # Was 0.1. Update every 5cm.  
#    minimum_travel_heading: 0.034       # Was 0.087 (5 deg). Update every 2 degrees.
    throttle_scans: 2                   # Process every 1 scan. Increase if CPU is too high.  
  
    solver_plugin: "solver_plugins::CeresSolver"  
  
    ceres_solver_options:  
      use_nonmonotonic_steps: true  
      max_num_iterations: 50  
      num_threads: 1
```