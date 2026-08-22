---
title: "Lab 2 - Exercises"
tags:
  - vnav
  - labs
---

# Lab 2 - Exercises

> [!important] Submission Requirements (Individual)
> **This lab must be completed individually.**
> - **Part 1 (Code Deliverables):** Push your entire package folder to your individual repository under the `lab2` directory. Make sure code compiles cleanly before pushing.
> - **Part 2 (Theory / Math Deliverables):** Submit typed solutions in PDF format (LaTeX or Word) under `lab2`.

> [!warning] Submission Deadline
> Your repository will be cloned at midnight **Friday, September 12, 2025**.
> If you need to submit your solution after the deadline, notify the instructor beforehand.

## Setup Workspace

To get started, create a ROS 2 workspace for the VNAV class:

```bash
mkdir -p ~/vnav_ws/src
cd ~/vnav_ws/src
ln -s ~/labs/lab2/two_drones_pkg
```

> [!info] Workspace Symlink
> Assuming you have cloned the VNAV labs repository to `~/labs`, the command above creates a **softlink** between the files in the VNAV repository and files in the ROS workspace. Editing files in `~/vnav_ws/src/two_drones_pkg` will be reflected in `~/labs/lab2/two_drones_pkg`.

### Ensure Up-to-Date Lab Code
Navigate to your clone of the Labs codebase and pull the latest updates:

```bash
cd ~/labs
git pull
```

### Building the Code
Build the package using `colcon`:

```bash
colcon build --symlink-install
```

> [!important] Sourcing the Environment
> In order to use your workspace, make ROS 2 aware of the packages by sourcing the environment in **every single terminal** where you run commands:
> ```bash
> source install/setup.bash
> ```

> [!tip] Automatic Sourcing
> You can automatically source your workspace on terminal startup by adding it to `~/.bashrc`:
> ```bash
> echo "source $HOME/vnav_ws/install/setup.bash" >> ~/.bashrc && source ~/.bashrc
> ```

---

## The Two-Drone Scenario

In this part, we work with **3D Rigid Transformations** and **`tf2`**, the basic ROS tool to keep track of multiple coordinate frames over time.

### The Static Scenario and rViz
Launch the two-drone static scenario:

```bash
ros2 launch two_drones_pkg two_drones.launch.yaml static:=True
```

![rViz.png](https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media/rViz.png)

This window is **rViz**, the ROS visualizer! Like most ROS nodes, rViz subscribes to topics and displays 3D graphics of the robotic system.

**First steps in rViz:**
1. **Add `/tf` visualization:** In the *Displays* panel, click *Add*, select the *By display type* tab, select **TF**, and confirm. You will see all coordinate frames with axes represented in red ($x$), green ($y$), and blue ($z$).
2. **Save configuration:** Hit `Ctrl + S` or select *File > Save Config* so you do not have to reconfigure every launch.

---

## Problem Formulation

We consider two aerial vehicles, **AV1** (blue) and **AV2** (red), following different trajectories: a **circle** and an **arc of parabola**, respectively.

- **World frame:** $\left(x_w, y_w, z_w\right)$
- **AV1 body frame:** centered at $O_1$ with axes $(x_1, y_1, z_1)$
- **AV2 body frame:** centered at $O_2$ with axes $(x_2, y_2, z_2)$

![two-drones-refs.png](https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media/two-drones-refs.png)

> [!note] Trajectory Equations (Positions)
> In the world frame, the origins of AV1 and AV2 are given as functions of time $t$:
> - $$ o_1^w(t) = [\cos(t), \sin(t), 0]^\top $$
> - $$ o_2^w(t) = [\sin(t), 0, \cos(2t)]^\top $$

> [!warning] Orientation Assumptions
> - **AV1:** Reference frame is oriented such that $y_1$ stays tangent to AV1's trajectory for all $t$, and $z_1$ is parallel to $z_w$ (roll = 0, pitch = 0, yaw = $t$).
> - **AV2:** Moves with pure translation; its axes remain parallel to the world axes for all times $t$.

> [!caution] Modeling Notes
> 1. Given the true dynamics of a quadrotor, these trajectories are dynamically infeasible. For this lab, we focus strictly on the kinematics of 3D rigid transformations.
> 2. The $y_1$ axis is chosen along the direction of motion for pedagogical purposes; standard ROS aerospace convention typically has $x_1$ pointing forward.

Deliverable 1: Nodes, topics, launch files (10 pts)**

With the`ros2 launch`command
 above we have spawned a number of ROS nodes at the same time. Using 
your knowledge of ROS, answer the following questions:

1. List the nodes running in the two-drone static scenario.
  - Hint: you can directly inspect the launch file, use the`ros2 node list`command, or get some help from`rqt_graph`. You will notice that rViz is initially not shown in it but you can uncheck the*Debug*option for a full picture.

2. How could you run the two-drone static scenario without using the`ros2 launch`command? List the commands that you would have to execute (in separate terminals) to achieve the same result.
  - Hint:`ros2 run [...]`, try things out before finalizing your answer!

3. List the topics that each node publishes / subscribes to. What nodes
 are responsible for publishing the av1, av2, frames? Which topic causes
 rViz to plot the drone meshes?
  - Hint: uncheck items on the left pane in rViz until the 
meshes disappear, then check what node is publishing the corresponding 
topic

4. What changes if we omit`static:=True`? Why?
  - Hint: check out and briefly explain the if and unless keywords in the launch file

### **Let's make things move! Publishing the transforms using tf**

After exploring the static scenario, it’s time to implement the motions described in theproblem formulationsection and visualize them in rViz. With the editor of your choice, open`frames_publisher_node.cpp`in the`src`folder of`two_drones_pkg`. In this file, we provide a basic structure of a ROS node.

### Some Context

Please take your time to familiarize with this code before modifying 
it. Although not mandatory, the pattern found in it is a very common way
 to implement ROS nodes:

- The node’s source code is encapsulated into a class,`FramesPublisherNode`(line 11), which inherits from`rclcpp::Node`.
- In the constructor of the class (lines 20 to 32), one performs 
operations that need to be executed only once upon startup (e.g. 
typically, initializing subscribers and publishers),
- Using a Timer (lines 14 and 27), the`onPublish()`method is called periodically - at a 50Hz - and all the operations within it are performed ad libitum,
  - the node is registered with`rclcpp::init(...)`
  - an instance of the node class is created
  - a blocking call to`rclcpp::spin()`is issued, which starts ROS’s main loop.In the body of`main()`(towards the end of the file):
  - the node is registered with`rclcpp::init(...)`
  - an instance of the node class is created
  - a blocking call to`rclcpp::spin()`is issued, which starts ROS’s main loop.

### **Deliverable 2 - Publishing transforms (20 pts)**

In`frames_publisher_node.cpp`, follow the instructions in the comments and fill in the missing code. Your objective is to populate the provided`world_T_av1`and`world_T_av2`variables to match the motions described in the problem formulation. These objects are instances of the`geometry_msgs::msg::TransformStamped`class, which is a ROS message type representing a homogeneous transformation matrix (at a specific instance in time).

**Keep in mind.**

> [!warning] Orientation Notice
> Ensure that the orientation of the AV1 frame matches the assumptions in the problem formulation (tangent to trajectory), as this is crucial for the result!

#### **How to test**

Once you are ready to compile your code, run:

```bash
colcon build
```

from the workspace folder`~/vnav_ws`.

To try out your code, launch the two-drone scenario in non-static mode, i.e. run:

```bash
ros2 launch two_drones_pkg two_drones.launch.yaml
```

**Note: 
Please make sure you source install/setup.bash inside your catkin space 
every time you compile the package by running calcon build**

> [!success] What to Expect
> You should see both drones moving in rViz along their respective circular and parabolic paths!
>
> ![two_drones_rviz.gif](https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media/two_drones_rviz.gif)

```bash

```

### **Changing the rViz fixed reference frame.**

As mentioned, we are interested in the motion of AV2 relative to 
AV1’s reference frame. In the Displays panel (left, by default), under 
the Global Options section, rViz offers the possibility to change the 
Fixed Frame to any frame published in tf. Try it out yourself and change
 “world” into “av1” by typing in the corresponding field. From this 
perspective, AV1 appears static, the world frame spins around its  $z$  axis and AV2 seems to be following a closed-curve trajectory.

### **Deliverable 3 - Looking up a transform (20 pts)**

In`plots_publisher_node.cpp`,
 follow the instructions in the comments and fill in the missing code. 
Your objective is to populate the provided object, transform, with the 
relative transform between two given frames with names`ref_frame`and`dest_frame`.

Compile your code and try it out as previously explained.

> [!success] What to Expect: Relative Trajectory
> You should see three trajectories in rViz:
> 1. **AV1 (blue, solid):** Circle on the $x$-$y$ plane in world frame.
> 2. **AV2 (red, solid):** Parabola on the $z$-$x$ plane in world frame.
> 3. **AV2 in AV1 frame (red, dashed):** An ellipse lying on a slanted plane!
>
> > [!tip] Troubleshooting
> > If the observed relative trajectory looks unexpected, try swapping `ref_frame` and `dest_frame` when looking up the transform.

## **Part 2: Math questions**

So far, we have used ROS and tf to get a visual understanding of the 
motion of AV2 relative to AV1’s body frame. In this section, you are 
asked to use your knowledge about homogeneous transformations and study 
the relative trajectory explicitly.

The visualization we have built should provide you with great 
guidance while working out the following questions. Since this exercise 
is designed for you to familiarize with the math of 3D transformations, 
we require that you explicitly write down all the homogeneous 
transformation matrices used in the process and precisely outline the 
logic and algebraic steps taken.

### **Deliverable 4 - Mathematical derivations (10 points)**

1. In theproblem formulation, we mentioned that AV2’s trajectory is an arc of parabola in the $x$ - $z$ plane of the world frame. Can you prove this statement?
  - Hint: Parabola has a general form of  $f\left(x\right)=ax^2+bx+c$  and note that  $c o s ( 2 t )$ can be written as…

2. Compute  $o^{1}_2(t)$ , i.e., the position of AV2 relative to AV1’s body frame as a function of $t$ .
  - Hint: write down the homogeneous transformations and compose them accordingly…

3. Show that  $o^{1}_2(t)$ describes a planar curve and find the equation of its plane  $\prod_{ }^{ }$ .
  - Hint: find a linear relation between  $z^{1}_2$ and  $y_2^{1}$

4. [optional] Rewrite the above trajectory explicitly using a 2D frame of reference  $(x_p,y_p)$ on the plane found before. Try to ensure that the curve is centered at the origin of this 2D frame and that $x_{p}$ , $y_{p}$ are axes of symmetry for the curve.
  - Hints: i) center the new 2D frame in  $p^{1}= ( − 1 , − 1 / 2 , 0 )$ , these coordinates are in AV1’s frame
  - ii) start with a 3D reference frame centered in p with axes  $(x_p,y_p,z_p)$ , compute  $o_2^{p}(t)$  iii) make sure that the $z$ component vanishes after the change of coordinates

5. [optional 2 extra point] Using the expression of  $o_2^{p}(t)$ , prove that the trajectory of AV2 relative to AV1 is an ellipse and compute the lengths of its semi-axes.
  - Hint: what is the general form of the equation of an axis-aligned ellipse centered in the origin?

**Deliverable 5 - Rotation presentations I (10 pts)**

A drone is initially facing **north** (aligned with the positive Y-axis). You want to rotate it **90° clockwise around the Z-axis** (so it ends up facing east, along the positive X-axis).

1. Write the unit quaternion that represents this rotation.
2. Apply the quaternion to the initial orientation vector  $v = ( 0 , 1 , 0 ) \mathbf{v} = (0, 1, 0)$
3. Show that the rotated vector is  $( 1 , 0 , 0 )$

**Deliverable 6 - Rotation presentations II (10 pts)**

Let R is:

$$
 R = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} 
$$ 1. Verify that  $R R$  is a proper rotation matrix (i.e.,  $R^{^\top} R = I R^\top R = I$  and  $det ( R ) = + 1 \det(R)=+1$ .

2. Find the axis–angle representation of  $R R$  (identify the rotation axis  $u \mathbf{u}$ u and rotation angle  $θ \theta$ ).

3. Apply  $R R$  to the vector  $v = ( 1 , 0 , 0 )^{^\top} \mathbf{v}=(1,0,0)^\top$ ; show the result.

4. Compute the equivalent unit quaternion  $q = ( w , x , y , z ) q=(w,x,y,z)$  for  $R R$ .

**Deliverable 7 - Intrinsic vs Extrinsic rotations (20 pts)**

Consider the following sequence of rotations:

$R_1$   90° around  $xR_2$  180° around  $yR_3$  -30° around  $x$

*A)*Extrinsic

The sequence of rotations is applied with respect to a fixed frame of reference (the world frame), as follows:

![guitar-01.png](https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media/guitar-01.png)

*Note*: the body axes are unlabeled, but represented in red ( $x_b$ ), green ( $y_b$ ), green ( $z_b$ ),

*B)*Intrinsic

The sequence of rotations is applied in*reverse order*with respect to a frame of reference attached to the object (the body frame), as follows:

![guitar-02.png](https://airou-lab.github.io/general_wiki_website/SP2026-VNAV-CourseContent/Uploaded%20Media/guitar-02.png)

**Note that the final orientation of the object is the same in both cases!**

This property is quite general: it holds regardless of the specific 
axes and angles of the rotations and for any number of rotations in the 
sequence.

Could you prove this formally?
