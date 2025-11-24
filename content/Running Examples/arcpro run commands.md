---
Type:
  - arcProDocs
Labs:
  - AIROU
---
> [!NOTE] Looking to run the example?
> Check out [[arcpro waypointer example run]]

The following commands assume you've built either our basic arcpro repo, or our waypointing repo. Keep in mind both repos are built for Jazzy, and as such may need modifcation if not using Jazzy. 

```bash
# Full demo launch file
ros2 launch merger full.launch.py

#Bringup lidar
ros2 launch ydlidar_ros2_driver ydlidar_launch.py   
 sim:=false

#Bringup vesc:
ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false

# Launch teleop
ros2 launch launches teleop.launch.py joy_dev:=ttyUSB0

#Launch SLAM manually
ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/src/merger/config/slam_toolbox_params.yaml
# Make sure to update the slam params file accordingly if you've moved it

# Send a drive message (ensure that vesc is running beforehand)
ros2 topic pub /drive_stamped ackermann_msgs/msg/AckermannDriveStamped \  
'{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"},  
  drive: {steering_angle: 0.0, steering_angle_velocity: 0.0, speed:  0.4, acceleration: 0.0, jerk: 0.0}}' \  
-r 10

```


As per usual please ensure the package is built and sourced properly. 