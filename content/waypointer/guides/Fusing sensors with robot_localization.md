---
Type:
  - arcProDocs
Labs:
  - AIROU
---
For sensor fusion with the realsense's IMU, we used the [robot_localization](https://docs.ros.org/en/melodic/api/robot_localization/html/index.html) package along with the nav2 stack. The config file can be found in `src/merger/config/ekf.yaml` and uses the realsense and odom topic for the motor controllers as seen below. If there are additional sensors (such as using the lidar as a odom source) you can read the robot_localization docs as linked before to add a new source. 

```yaml
  odom0: /odom  
  odom0_config: [ false, false, false,  
                  false, false, false,  
                  true, true, false,  
                  false, false, true,  
                  false, false, false ]  
# realsense imu..  
imu0: /camera/camera/imu/sample  
imu0_config: [ false, false, false,  # ignore position  
               true, true, true,     # use orientation  
               true, true, true ]     # use angular velocity
```