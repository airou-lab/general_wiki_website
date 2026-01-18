# Initial Boot-up
## Introduction
In this tutorial, we will show how to run the robot in teleoperation mode.
This involves plugging in the batteries, connecting to the robot's network, and launching the teleoperation ROS launch file.

## Steps

1. **Plugin The Main Battery:**

![Plugin Main Battery](../photos/cpu_plug_in.png)

2. **Plugin The VESC Battery:**

![Plugin Vesc Battery](../photos/vesc_plug_in.png)

(Front wheels should “lock” when VESC is plugged in) 

3. **Connect to Robot Wi-Fi Network:**

Connect to the network named "Robot AP ***robot number***" (Example: Robot AP 3)
![Wi-Fi](../photos/wifi.png)
> NOTE:
> 
> It may take up to 30 seconds for the network to appear as a possible connection 

4. **SSH Into The Car:**
If using WSL, open the Ubuntu 18.04 Terminal
* [Here's how to download Ubuntu if you're using Windows](../misc/wslInstall.md)

![windows ubuntu terminal](../photos/ubuntu_on_windows.png)

Or if you're already using a linux OS, just open the bash terminal

In the terminal, enter the command: 

    ssh robot@10.42.0.1 

You should see something like this:
![ssh example](../photos/ssh_example.png)

5. **Connecting The Bluetooth Controller:**

Press the center button on the PS4 controller to pair
* If it does not connect, [see here](../misc/bluetoothController.md)

![Connecting Bluetooth Controller](../photos/bluetooth_controller.png)

6. **Starting Teleoperation:**

To start teleoperation and drive the car manually with the sensors active, enter:

    roslaunch mushr_base teleop.launch

After awhile (like 15-20 seconds), you should see the sensors turn on (LiDAR and realsense cameras) and be able to drive it manually.
* While holding the Deadman's Switch (L1), you can use the left joystick to go forward and backward and the right joystick to steer left or right.

## How to shut down the race car:
1. To shut down the system, press Ctl+C. Allow 10--15 seconds to completely shutdown. 

2. Then in the same terminal run:

    ```sudo shutdown -P now```
3. Unplug the main battery and VESC battery. Shutdown process is complete.  
