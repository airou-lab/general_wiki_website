---
Type:
  - arcProDocs
Labs:
  - AIROU
---
> [!NOTE] Running from our repo directly?
    > If you cloned our repo and followed the build steps, skip to [[arcpro run commands]]

> [!Warning] Port issues
    > Note that some ports in these docs may have been manually defined, and as such should be accounted for with lsbusb


# Realsense
```bash
sudo apt update  
sudo apt install -y v4l-utils \ ros-jazzy-librealsense2=2.56.4-1noble.20250722.140707 \  ros-jazzy-realsense2-camera=4.56.4-1noble.20250814.083109 \  ros-jazzy-realsense2-camera-msgs=4.56.4-1noble.20250806.110923
# Ensure permissions for the camera
sudo udevadm control --reload-rules && sudo udevadm trigger  
sudo usermod -aG video $USER    
```

Then the realsense should be runnable via:
```bash
ros2 launch realsense2_camera rs_launch.py
```


# YdLidar X4 Pro

## Build the SDK
```bash
git clone git@github.com:YDLIDAR/ydlidar_ros2_driver.git 
```
Then go through these docs [here ](https://github.com/YDLIDAR/YDLidar-SDK/blob/master/doc/howto/how_to_build_and_install.md) and run dependent on OS or follow below. It should bringup rivz automatically and run the expected laser scan.
```bash
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK
mkdir build
cd build
cmake ..
make
sudo make install
cpack #put into package
./tri_test #test 
```
## Build the Ros repo
Run below, will grab the SDK and the ros2 code. 
```bash

git clone git@github.com:YDLIDAR/YDLidar-SDK.git
```

