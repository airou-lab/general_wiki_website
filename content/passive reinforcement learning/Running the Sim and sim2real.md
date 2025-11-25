```bash
ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false #bringup the robot

ros2 launch realsense2_camera rs_launch.py device_type:=d435i enable_color:=true enable_depth:=true pointcloud.enable:=true align_depth:=true rgb_camera.profile:=1280x720x30 depth_module.profile:=1280x720x30   #bringup the camera

python3 ros_to_tcp_bridge.py #run the bridge

python3 inference_server_RNN.py --model {MODEL_NAME_HERE}.zip #Run the model

# Or if we want to run all of them at once:
ros2 launch f1tenth_stack no_lidar_bringup_launch.py sim:=false & ros2 launch realsense2_camera rs_launch.py device_type:=d435i enable_color:=true enable_depth:=true pointcloud.enable:=true align_depth:=true rgb_camera.profile:=1280x720x30 depth_module.profile:=1280x720x30 & python3 ros_to_tcp_bridge.py & python3 inference_server_RNN.py --model {MODEL_NAME_HERE}.zip
```
