---
title: "Lab 7 - Exercises"
tags:
  - vnav
  - labs
---

# Lab 7 - Exercises

> [!info] Related Lectures & Notes
> - [[CS4733_5733_F25_W14_Quadrotor_Dynamics.pdf_viewer|Lecture 14 - Quadrotor Dynamics]]
> - [[CS4733_5733_F25_Quadrotor_Control_Planning.pdf_viewer|Quadrotor Control & Planning]]
> - [[Geometric_controller_steps.pdf_viewer|Geometric Controller Steps]]
> - [[06-Control1-notes.pdf_viewer|06 Control 1 Notes]]
> - [[09-TrajectoryOptimization1-notes.pdf_viewer|09 Trajectory Optimization 1 Notes]]

> [!important] Lab Structure
> - **Part 1 (Transformations & Quadrotor Dynamics):** Individual analysis and derivations.
> - **Part 2 (Trajectory Tracking Controller):** Implementation and gain tuning in the TESSE UAV flight simulator.

> [!warning] Submission Guidelines
> Submit your individual writeup and team code in the `lab7` folder of your respective repositories.

### Part 1: Practice transformations

### Deliverable 1 - Transformations in Practice (10 pts)

This exercise will help you to understand how to perform 
transformation between different rotation representations using ROS. In 
addition, you will gain experience of reading through a documentation in
 order to find what you need.

A. Messages Vs tf

In ROS, there are two commonly used datatypes for quaternions. One is[`geometry_msgs::msg::Quaternion`](https://docs.ros2.org/latest/api/geometry_msgs/msg/Quaternion.html)and the other is[`tf2::Quaternion`](https://docs.ros2.org/foxy/api/tf2/classtf2_1_1Quaternion.html). Based on the documentation for[tf2](https://docs.ros2.org/foxy/api/tf2/namespacetf2.html)and[the tf2 tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Tf2-Main.html), answer the following questions:

1. Assume we have an incoming`geometry_msgs::msg::Quaternion quat_msg`that holds the pose of our robot. We need to save it in an already defined`tf2::Quaternion quat_tf`for further calculations. Write one line of C++ code to accomplish this task.
2. Assume we have just estimated our robot’s newest rotation and it’s saved in a variable called`quat_tf`of type`tf2::Quaternion`. Write one line of C++ code to convert it to a`geometry_msgs::msg::Quaternion`type. Use`quat_msg`as the name of the new variable.
3. If you just want to know the scalar value of a`tf2::Quaternion`, what member function will you use?

B. Conversion

The following questions will prepare you for converting between different rotation representations in C++ and ROS.

1. Assume you have a`tf2::Quaternion quat_t`. How to extract the yaw component of the rotation with just one function call?
2. Assume you have a`geometry_msgs::msg::Quaternion quat_msg`. How to you convert it to an Eigen 3-by-3 matrix? Refer to[this](https://docs.ros2.org/foxy/api/tf2_eigen/tf2__eigen_8h.html)and[this](http://eigen.tuxfamily.org/dox-3.2/classEigen_1_1Quaternion.html)for possible functions. You probably need two function calls for this.

### Deliverable 2 - Modelling and control of UAVs (20 pts)

A. Structure of quadrotors

![drone_spinning.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/drone_spinning.png)

The figure above depicts two quadrotors*(a)*and*(b)*. Quadrotor*(a)*is a fully functional UAV, while for Quadrotor*(b)*someone changed propellers 3 and 4 and reversed their respective rotation directions.

Show mathematically that quadrotor*(b)*is not able to track a trajectory defined in positionand yaw orientation.

- Hint: write down thematrix (see lecture notes eq. (6.9)) for the two cases*(a)*and*(b)*and compare the rank of the two matrices

B. Control of quadrotors

Assume that empirical data suggest you can approximate the drag force (in the body frame) of a quadrotor body as:

$F^b = \begin{bmatrix} 0.1 & 0 & 0 \\ 0 & 0.1 & 0 \\ 0 & 0 & 0.2\end{bmatrix} (v^b)^2$

With  $(v^b)^2= [-v^b_x \mid v^b_x \mid ,\, -v^b_y \mid v^b_y \mid ,\, -v^b_z \mid v^b_z \mid]^T$ , and  $v_x, v_y, v_z$ ,being the quadrotor velocities along the axes of the body frame.

With the controller discussed in class (see referenced paper[1](https://vnav.mit.edu/labs/lab3/exercises.html#fn:1)), describe how you could use the information above to improve the tracking performance.

- Hint: the drag force introduced above is an additional 
term in the system’s dynamics, which the controller could compensate for
 explicitly…

### **Part 2: Trajectory tracking for UAVs**

In this section, we are going to implement the geometric controller discussed in class on a simulated drone.

#### **Getting the code base**

Consistently with the folder structure introduced in previous 
assignments, we will navigate to our existing clone of the VNAV Labs 
repository and pull the latest updates:

```bash
# change the folder name according to your setup
cd ~/vnav/starter-code
git pull
```

Next, put the team submission repo that you just created into you colcon workspace.

```bash
cd ~/vnav_ws/src/
git clone <your team repo url>
```

Note that if the repo doesn’t have any commits yet, you won’t be able to clone it; instead, make a new directory in`~/vnav_ws/src`.

In`~/labs/lab7`we now have the`tesse_ros_bridge`and the`controller_pkg`folders,
 which are both ROS packages. Let us copy these folders to the team repo
 inside VNAV workspace and build the workspace as follows:

```bash
cp -r ~/labs/lab7/ ~/vnav_ws/src/<team repo name>
```

In your`~/vnav_ws/src/<team repo name>/lab7`folder, you should see two folders:`controller_pkg`and`tesse-ros-bridge`. Then, we need install some Python dependencies:

```bash
cd ~/vnav_ws/src/<team repo>/lab7/tesse-interface

pip install . sudo apt install ros-jazzy-tf-transformations
pip install numpy==1.26.4
pip install -U transforms3d
pip install rospy2
sudo apt install ros-jazzy-ackermann-msgssudo apt updatesudo apt install ros-jazzy-rviz-imu-plugin
```

At this point, you can either keep your lab 2 code or remove all the 
folders related to the previous labs. Either way, you need to compile 
the new code.

```bash
colcon build
source install/setup.bash
```

After doing so, please proceed[here](https://drive.google.com/file/d/1P2SZ20yg6nEt-UHDq6aHqPPYaOvkqrrx/view?usp=sharing)to
 download the binary executable for the simulator we are going to use 
for lab 7 (if you already downloaded this for Lab 1, you do not need to 
re-download it). Unzip the file, put the folder in`~/vnav-builds`, and run the following commands:

```bash
cd ~/vnav-builds/lab7/
chmod +x lab7.x86_64
```

This will make sure you can run the executable in the command line.

### Launching the TESSE simulator with ROS bridge

In a terminal window, run this command to start the simulator:

```bash
cd ~/vnav-builds/lab7/
./lab7.x86_64
```

Once the simulator starts, you should see the unity simulator (fig. below).

![sim.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/sim.png)

In the simulator, you can:

- press`W`to turn on all propellers;
- press`R`to respawn the quadrotor at the initial location.

Note that**you can resize the window**to help with debugging later on.

Once the workspace has been compiled successfully, with your workspace sourced execute:

```bash
# make sure to source install/setup.bash!
ros2 launch tesse_ros_bridge tesse_quadrotor_bridge.launch.yaml
```

This launches two ROS nodes:`tesse_ros_brige`and`quadrotor_control_interface`.
 The former receives state messages from our simulator and publishes 
them in a few ROS topics, and the latter listens to our controller node 
and sends the propeller commands to our simulator. To visualize the 
state of our quadrotor, we will use`rviz2`. Run the following command to load our`rviz`preset:

```bash
cd ~/vnav_ws/src/controller_pkg
rviz2 -d rviz/lab7.rviz
```

You should see a screen similar to this:

![rviz_starting.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/rviz_starting.png)

A few highlights:

- the purple upward arrow corresponds to the IMU message;
- the`base_link_gt`axes correspond to the body frame of the quadrotor;
- the`world`axes correspond to the world frame in ROS.

### Implement the controller

From the previous section, you must have noticed that the drone is 
stationary. Unsurprisingly, this happens because the UAV is not 
receiving any control inputs. In this section, you will be precisely 
asked to take care of it!

Given four propeller speeds, the simulator propagates forward the UAV
 dynamics and outputs the current state of the robot. It is your job now
 to provide the propeller speeds based on the current state of the robot
 (from the simulator) and a desired one (from a trajectory generator). 
This problem is extensively described in the geometric controller paper[1](https://vnav.mit.edu/labs/lab3/exercises.html#fn:1),
 where the authors introduce an almost-globally convergent geometric 
controller for a quadrotor, also outlined in class. We will ask you to 
read the paper thoroughly and implement this controller in ROS.

For the purposes of this lab, the trajectory generator is given by 
the traj_publisher node, which outputs a time-varying desired state 
along a hard-coded circular trajectory. The navigation stack (almost) 
implemented in our codebase has the architecture shown below:

![navigation_stack.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/navigation_stack.png)

where the ROS nodes are highlighted as vertices in the graph and the ROS topic names are reported on the edges.

In particular:

- `/desired_state`is of type[trajectory_msgs/msg/MultiDOFJointTrajectoryPoint](https://docs.ros2.org/foxy/api/trajectory_msgs/msg/MultiDOFJointTrajectoryPoint.html)and has the following fields:
  - `transforms`- type[geometry_msgs/msg/Transform](https://docs.ros2.org/latest/api/geometry_msgs/msg/Transform.html):
    - `translation`: a 3D vector with the desired position of the c.o.m. in the world frame
    - `rotation`: a quaternion rapresenting a rotation (in our case will be only a yaw component)

  - `velocities`- type[geometry_msgs/msg/Twist](https://docs.ros2.org/latest/api/geometry_msgs/msg/Twist.html):
    - `linear`: a 3D vector with the desired velocity of c.o.m. in world frame
    - `angular`: we will ignore this field as it is not used by the controller

  - `accelerations`- type[geometry_msgs/msg/Twist](https://docs.ros2.org/latest/api/geometry_msgs/msg/Twist.html):
    - `linear`: a 3d vector with the desired acceleration of c.o.m. in world frame
    - `angular`: we will ignore this field as it is not used by the controller

- `/current_state`is of type[nav_msgs/msg/Odometry](https://docs.ros2.org/foxy/api/nav_msgs/msg/Odometry.html)with the relevant fields:
  - `pose.pose`- type[geometry_msgs/msg/Pose](https://docs.ros2.org/latest/api/geometry_msgs/msg/Pose.html):
    - `position`: a 3d vector with the current position of the c.o.m. in the world frame
    - `orientation`: a quaternion representing the current orientation of the UAV

  - `twist.twist`- type[geometry_msgs/msg/Twist](https://docs.ros2.org/latest/api/geometry_msgs/msg/Twist.html):
    - `linear`: a 3d vector with the current velocity of c.o.m. in the world frame
    - `angular`: a 3d vector with the current angular velocity in the world frame

- `/rotor_speed_cmds`is of type[mav_msgs/msg/Actuators](https://github.com/ethz-asl/mav_comm/blob/ros2/mav_msgs/msg/Actuators.msg)and it contains the relevant field:
  - `angular_velocities`- type`float64[]`, containing the desired speeds of the propellers.

### Simulator conventions

In the picture below, we illustrate the conventions used in unity 
simulator for the propeller speeds and their positions in the body 
frame. Please**look carefully**as this will help you build the correct wrench-to-controls matrix (`F2W`) in the coding assignment

![sim_convention.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/sim_convention.png)

#### **Note that**

- as in most research papers, we assume that, for $\omega_i > 0$ ,
 all the propellers produce an upward force (lift). This is consistent 
with the first row of the matrix in eq. (6.9) on the lecture notes. 
While this might be confusing at first, note that on real quadrotors the
 motors are configured to rotate in different directions: two 
counter-clockwise (CCW), and two clockwise (CW). This configuration is 
necessary so that our quadrotor will be stable in its yaw direction. 
There are also two sets of propellers: one set for CCW motors, and 
another set for CW motors (both will produce upward force if mounted 
appropriately). See this[video](https://www.youtube.com/watch?v=bHgeT66AXJ0)[![play_overlay.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/play_overlay.png)](https:/www.youtube.com/watch?v=bhget66axj0)for an example.
- in the figure, we show the positive spinning directions for the 
propellers (blue) and the resulting direction of the yaw torques 
generated by aerodynamic drag. For example: propeller 1’s angular 
velocity  $\omega_1$ is
 considered positive when propeller 1 spins clockwise (as seen from 
top), which in turn produces a counter-clockwise drag torque  $\tau_{\text{drag}_1}$ .
 The sign of the drag torque is determined by applying right-hand rule: 
positive for counter-clockwise, and negative for clockwise.
- the spinning directions are different from the paper. The expression  $\tau_{\text{drag}}^i = (-1)^i c_d\,\omega_i | \omega_i |$ implies that the drag on propeller 1 produces a negative (clockwise) yaw torque instead, for. However, the above convention is acceptable: propellers are*mounted*differently in the simulated quadrotor!
- the propeller speeds need to be provided in**radians per second (rad/s)**,
 NOT in rpm. Initially, it will be tempting to go for the latter, as it 
will make the drone move more easily (control inputs get bigger), 
however, it will hurt you in the long run.

Before proceeding, keep in mind that there are a number of caveats 
that will make the math in your code slightly different from the one 
found in the paper. The main differences can be summarized as follows:

**Reference frames**. The paper and your code use 
different conventions for coordinate frames. Please refer to the figure 
and pay attention to the two main facts summarized below.

![Frames-Paper-vs-ROS.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/frames-paper-vs-ros.png)

1. In the paper, the z-axes - both in the world and body frames - are downwards, while ROS has them pointing upwards. This affects the signs of  $b_{3_d}$ in equation (12), as well as gravity and aerodynamic forces in equations (12), (15), (16). (equation numbers refer to the paper[1](https://vnav.mit.edu/labs/lab3/exercises.html#fn:1)).
2. In the paper, the x-body axis is along a propeller arm,
 while we prefer having it at 45° between two propellers. This will 
require some thought on your end when converting the total desired force
 + torques (*wrench*) into the desired propeller speeds. In other
 words, you have to change equation (1) from the paper. For this step, 
refer to equation (6.9) in the lecture notes!

**Aerodynamic coefficients**. In the paper, equation (1), the quantity   $c_{\tau f}$ relates directly the yaw torque with the lift produced by a propeller. In contrast, we prefer using the *lift* and *drag* coefficients  $c_f$  and  $c_d$  , which have a clearer physical interpretation. Consider the relation  $c_{\tau f}=c_d/c_f$   between these coefficients.

### Deliverable 3 - Geometric controller for the UAV (50 pts)

After reading the reference[1](https://vnav.mit.edu/labs/lab3/exercises.html#fn:1)-*thoroughly*- get together with your teammates and open the source file`controller_node.cpp`.
 In this file, you will find detailed instructions to fill in the 
missing parts and make your quadrotor fly! To have full credits for this
 part of the lab, your team needs to complete the following:

- Implement all missing parts in`controller_node.cpp`and ensure everything compiles.
- Tune parameters so that the quadrotor achieves stable circular trajectory.
- A video showing the quadrotor completing one round of the circular trajectory in`rviz`(can
 either be a screen capture, or a video shot using your phone). Please 
upload the video onto either Google drive or Dropbox, generate a 
publicly viewable link, and put the link in a text file called`rviz_drone_flight.txt`in your repo.

#### How to test

Once you are ready to compile your code, run:

```bash
colcon build
```

from the folder`~/vnav_ws`.

To try out your code, launch the simulator. Additionally, run your controller by typing, in a separate terminal:

```bash
ros2 launch controller_pkg traj_tracking.launch
```

Depending on your focus - and degree of luck - it will take multiple 
attempts to have a stable and smooth controller and multiple iterations 
of parameter tuning. That’s normal!

As a suggestion, you could start by testing a stationary waypoint, 
before moving to the circular trajectory. This is possible by switching 
the`STATIC_POSE `flag to`1`in`controller_pkg/src/traj_publisher.cpp`. Also, you should use`rviz`to visually compare the desired and the current poses.

#### Tuning tips

First of all, look closely at the equations and see what are the gain
 parameters directly affecting. Which one affects the yaw? Which one 
affects the speed? Which one affects the position? Doing so will give 
you a rough idea on what to do for tuning.

To provide a more graphical/qualitative understanding, here are some typical situations that you might encounter:

**`komega`is too high**:

![tuning_highkomega.gif](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/tuning_highkomega.gif)

**`kr` is too low**:

![tuning_lowkr.gif](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/tuning_lowkr.gif)

**`kv` is too low**:

![tuning_lowkv.gif](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/tuning_lowkv.gif)

**NOTE**: The specific gain parameters may differ across different computers.

#### What to expect

If your controller is working reasonably well we expect to see something like this:

![result.gif](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/result.gif)

**Note**: it is totally fine if the drone does a rapid maneuver to start tracking the circle as soon as you run the controller node.

## References

1. Lee, Taeyoung, Melvin Leoky, N. Harris McClamroch. “Geometric 
tracking control of a quadrotor UAV on SE (3).” Decision and Control 
(CDC), 49th IEEE Conference on. IEEE, 2010[Link](http://math.ucsd.edu/~mleok/pdf/LeLeMc2010_quadrotor.pdf)

---

**Previous**: [[Lab 6 - Exercises|⬅ Lab 6: Object Detection]] | **Next**: [[Final Project + exam/index|Final Project & Exam ➔]]
