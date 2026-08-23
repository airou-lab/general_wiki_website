---
title: "Lab 4 - Exercises"
tags:
  - vnav
  - labs
---

# Lab 4 - Exercises

> [!info] Related Lectures & Notes
> - [[CS4733_5733_F25_W4_5_2view_GeometryII.pdf_viewer|Lectures 4-5 - 2-View Geometry II]]
> - [[CS4733_5733_F25_W6_7_Ransac_correspondance.pdf_viewer|Lectures 6-7 - RANSAC Correspondence]]
> - [[Eight_Point_Algorithm_Explanation.pdf_viewer|Eight-Point Algorithm Explanation]]
> - [[14-2viewGeometry-notes.pdf_viewer|14 2-View Geometry Notes]]
> - [[15-RANSAC-notes (2).pdf_viewer|15 RANSAC Notes]]

> [!important] Submission Guidelines
> - **Individual Part:** Upload solutions in the `lab4` folder of your individual repository.
> - **Team Part:** Upload solutions in the `lab4` folder of your team repository.
> - **Deliverable 5:** Create a dedicated folder `lab4_deliverable5` and push code and results there.

> [!warning] Submission Deadline
> Staff will clone all repositories on **October 14th, 11:59 PM**.

**Part 1: Individual section**

## Deliverable 1 - Designing a Minimal Solver [15 pts]

Please read the following paper.

[1] Nistér, David. “An efficient solution to the five-point relative 
pose problem.” 2003 IEEE Computer Society Conference on Computer Vision 
and Pattern Recognition, 2003. Vol. 2. 2003.[Link here](https://www-users.cse.umn.edu/~hspark/CSci5980/nister.pdf)

Nister’s method [1] is a minimal solver since it uses 5 point 
correspondences to compute the 5 degrees of freedom that define the 
relative pose (up to scale) between the two cameras (recall: each point 
induces a scalar equation). In the presence of external information 
(e.g., data from other sensors), we may be able use less point 
correspondences to compute the relative pose.

1. Explain 2-point, 5-point and 8-point algorithms and explain their steps to get the relative pose estimate (up to scale)

2. Outline the main computational steps required to get the 
relative pose estimate (up to scale) in Nister’s 5-point algorithm.

3. Does the 5-point algorithm exhibit any degeneracy? (degeneracy = 
special arrangements of the 3D points or the camera poses under which 
the algorithm fails)

4. When used within RANSAC, what is the expected number of iterations
 the 5-point algorithm requires to find an outlier-free set?

- 
  - Hint: take same assumptions of the lecture notes

5. **Can you do better than Nister?**Consider a drone 
flying in an unknown environment and equipped with a camera and an 
Inertial Measurement Unit (IMU). We want to use the feature 
correspondences extracted in the images captured at two consecutive time
 instants $t_{1}$ and $t_{2}$ to estimate the relative pose (up to scale) between the pose at time $t_{1}$ and the pose at time $t_{2}$ .
 Besides the camera, we can use the IMU (and in particular the 
gyroscopes in the IMU) to estimate the relative rotation between the 
pose of the camera at time $t_{1}$ and $t_{2}$ .

Assume the relative camera rotation between time $t_{1}$ and $t_{2}$ and
 is known from the IMU. Design a minimal solver that computes the 
remaining degrees of freedom of the relative pose (2-point algorithm)

- 
  - Hint: we only want to compute the pose up to scale

## **Part 2 and 3 (Team deliverables):**

**Part 2:** we will estimate the motion of a (simulated)
 flying drone in real time and compare the performances of different 
algorithms. For the datasets, we will use pre-recorded`data` of a simulated drone flying in an indoor environment.

**Part 3:** You need to drive the car in minicity and 
estimate the motion of the car using 2D-2D correspondence (required) and
 3D-3D correspondence (optional)

For the algorithms, we will be using the implementations provided in the[OpenGV](https://laurentkneip.github.io/opengv/page_how_to_use.html)library (note: Open**G**V).

Additionally, for motion estimation:

- We will only focus on two-view (vs multi-camera) pose estimation. In
 OpenGV, we refer to two-view problems as “Central” (vs “Non-Central”) 
relative pose problems.
- We will focus only on the calibrated case, where the intrinsic 
matrix K is given, and we assume that the images are rectified 
(distortion removed) using the parameters that you estimated previously.

## Getting started: code base and datasets

- **Prerequisites**: Lab 5 will use the feature matching 
algorithms developed in Lab 3 (in particular, we use SIFT matching), so 
make sure you have a working version of Lab 3 already in your workspace.
- **Prepare the code base**: download lab4 code from OUVNAV_labs. Copy the entire `lab4` folder to the `src` folder of your vnav workspace (e.g., `~/vnav_ws/src`).
- We also need to install OpenGV. In your colcon workspace, clone`https://github.com/MIT-SPARK/opengv.git`. Run`colcon build`and make sure that OpenGV and the stencil code build successfully.
- You also need to install CV_bridge. This requires cloning the 
following repository and selecting branch compatible with ROS 2 Jazzy 
(4.1.0), clone it in your workspace,

```bash
git clone https://github.com/ros-perception/vision_opencv.gitcd vision_opencvgit fetch --all --tags   // you can browse all branchesgit checkout 4.1.0
```

Now you have setup dependencies. Then pull the course repository

```bash
git pull
```

Copy lab4 in your workspace:

`cp -r ~/lab4 ~/vnav_ws/src`

Note, you should have folder lab4 inside src folder

**Download the datasets**: We will use dataset `vnav-lab6-office`and you can download it[here](https://drive.google.com/file/d/1TohOnfjR_FKf_y9wYTEkmv-XCuFPFRPt/view?usp=sharing).

After downloading the dataset you will need to unzip it.

The rosbag files include the following topics of the drone:

- Ground-truth pose estimate of the drone’s body frame:`/tesse/odom`
- RGB image from the left-front camera of the drone:`/tesse/left_cam/rgb/image_raw`
- Depth image:`/tesse/depth_cam/mono/image_raw`

You can play these datasets by running:

```bash
ros2 bag play <path to bag>
```

while in parallel open RVIZ by:

```bash
rviz2 -d <path_to_lab_4> /config/default.rviz
```

You should see on the left the RGB Image and the Depth image.

Let’s perform motion estimation!

We will use two methods to estimate the motion of the drone:

- Motion estimation from 2D-2D correspondences (Deliverable 3)
- Motion estimation from 3D-3D correspondences (Deliverable 4)

You also drive the car and estimate its motion using 2D-2D correspondence (i.e., images) for Deliverable 5.

In Deliverable 3, we will perform motion estimation**only**using
 2D RGB images taken from the drone’s camera, while in Deliverable 4, we
 will additionally use the depth measurements to get the sense of 3D.

**NOTE:**

- All your main implementations of the motion estimation algorithms should be in the`pose_estimation.cpp`file.
 In the file, we have also provided many comments to help your 
implementation, so please go through the comments in details.
- For this lab, we provide a number of useful utility functions in`lab4_utils.h`. You do not need to use these functions to complete the assignment, but they might help save you some time and frustration.

### **Deliverable 2 - Initial Setup [5 pts]**

Before we go to motion estimation, an important task is to calibrate 
the camera of the drone, i.e., to obtain the camera intrinsics and 
distortion coefficients. Normally you would need to calibrate the camera
 yourself offline to obtain the parameters.

However, in this lab the camera that the drone is equipped with has 
been calibrated already, and calibration information is provided to you!
 (If you are curious about how to calibrate a camera, feel free to check
 this[OpenCV tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html))

As part of the starter code, we provide a function`calibrateKeypoints`to
 calibrate and undistort the keypoints. Make sure you use this function 
to calibrate the keypoints before passing them to RANSAC.

### **Deliverable 3: 2D-2D Correspondences [40 pts]**

Given a set of keypoint correspondences in a pair of images (2D - 2D 
image correspondences), as computed in the previous lab 3, we can use 
2-view (geometric verification) algorithms to estimate the relative pose
 (up to scale) from one viewpoint to another.

To do so, we will be using three different algorithms and comparing their performance.

We will first start with the 5-point algorithm of Nister. Then we 
will test the 8-point method we have seen in class. Finally, we will 
test the 2-point method you developed in Deliverable 1. For all 
techniques, we use the feature matching code we developed in Lab 3. In 
particular, we use SIFT for feature matching in the remaining of this 
problem set.

We provide you with a skeleton code in`lab4`folder where we have set-up ROS callbacks to receive the necessary information.

We ask you to complete the code inside the following functions:

1.`cameraCallback`: this is the main function for this lab.

Inside, you will have to use three different algorithms to estimate the relative pose from frame to frame:

- OpenGV’s the 5-point algorithm with RANSAC[(see OpenGV API)](https://laurentkneip.github.io/opengv/classopengv_1_1sac__problems_1_1relative__pose_1_1CentralRelativePoseSacProblem.html)
- OpenGV’s[8-point algorithm by Longuet-Higgins with RANSAC](https://laurentkneip.github.io/opengv/classopengv_1_1sac__problems_1_1relative__pose_1_1CentralRelativePoseSacProblem.html)
- OpenGV’s[2-point algorithm with RANSAC](https://laurentkneip.github.io/opengv/classopengv_1_1sac__problems_1_1relative__pose_1_1TranslationOnlySacProblem.html).
 This algorithm requires you to provide the relative rotation between 
pairs of frames. This is usually done by integrating the IMU’s gyroscope
 measurements. Nevertheless, for this lab, we will ask you to compute 
the relative rotation using the ground-truth pose of the drone between 
both frames.

For each part, follow the comments written in the source code for further details.

**We strongly recommend you to take a look at how to use OpenGV functions[here](https://laurentkneip.github.io/opengv/page_how_to_use.html).**

**OPTIONAL (5 bonus pts): if you are curious about how important is to reject outliers via RANSAC, try to use the 5-point method [without RANSAC (see OpenGV API)](https://laurentkneip.github.io/opengv/namespaceopengv_1_1relative__pose.html#af269f7393720263895fb9b746e4cec4a), and add the results to the performance evaluation below.**

2.`evaluateRPE`: evaluating the relative pose estimates

After implementing the relative pose estimation methods, you are 
required to evaluate their accuracy and plot their errors over time. 
Since you also have the ground-truth pose of the drone, it is possible 
to compute the Relative Pose Error (RPE) between your estimated relative
 pose from frame to frame and the actual ground-truth movement. Follow 
the equations below and compute the translation and rotation relative 
errors on the rosbag we provided.

***The relative pose error is a metric for investigating the local consistency of a trajectory***

RPE compares the relative poses along the estimated and the reference trajectory. Given the ground truth pose $T_{r e f , t}^{W}$ at time $t$ (with respect to the world frame $W$ ), we can compute the ground truth relative pose between time $t − 1$ and $t$ as:

$T_{r e f , t}^{r e f , t − 1} = ( T_{r e f , t − 1}^{W} )^{− 1} T_{r e f , t}^{W} \in SE ( 3 )T_{r e f , t}^{r e f , t − 1} = ( T_{r e f , t − 1}^{W} )^{− 1} T_{r e f , t}^{W} \in SE ( 3 )$

Similarly, the 2-view geometry algorithms we test in this lab will 
provide an estimate for the relative pose between the frame at time $t − 1$ and $t$ :

$T_{e s t , t}^{e s t , t − 1} \in SE ( 3 )T_{e s t , t}^{e s t , t − 1} \in SE ( 3 )$

Therefore, we can compute the mismatch between the ground truth and 
the estimated relative poses using one of the distances we discussed 
during lecture.

***When using 2D-2D correspondences, the translation is only
 computed up to scale (and is conventionally returned as a vector with 
unit norm). so we recommend scaling the corresponding ground truth 
translation to have unit norm before computing the errors we describe 
below.***

**Relative translation error:**This is simply the Euclidean distance between the ground truth and the estimated relative translation:

$R P E_{t − 1 , t}^{t r a n} = \| trans ( T_{r e f , t}^{r e f , t − 1} ) − trans ( T_{e s t , t}^{e s t , t − 1} ) \|_{2}R P E_{t − 1 , t}^{t r a n} = \| trans ( T_{r e f , t}^{r e f , t − 1} ) − trans ( T_{e s t , t}^{e s t , t − 1} ) \|_{2}$

where $trans ( \cdot )$ denotes the translation part of a pose.

**Relative rotation error:**This is the chordal distance between the ground truth and the estimated relative rotation:

$R P E_{i , j}^{r o t} = \| rot ( T_{r e f , t}^{r e f , t − 1} ) − rot ( T_{e s t , t}^{e s t , t − 1} ) \|_{F}R P E_{i , j}^{r o t} = \| rot ( T_{r e f , t}^{r e f , t − 1} ) − rot ( T_{e s t , t}^{e s t , t − 1} ) \|_{F}$

where $rot ( \cdot )$ denotes the rotation part of a pose. F is Ferobenius norm: [Frobenius Norm - an overview | ScienceDirect Topics](https://www.sciencedirect.com/topics/engineering/frobenius-norm)

You will need to implement these error metrics, compute them for**consecutive frames in the rosbag**, and plot them as discussed above.

As a deliverable,**provide 2 plots showing the rotation error and the translation error over time**for
 each of the tested techniques (2 plots with 3 lines for the algorithms 
using RANSAC). You can write the data to a file and do the plotting with
 Python if you prefer (upload as well the python script if necessary).

3. Publish your relative pose estimate

In order to visualize your relative pose estimate between time $t − 1$ and $t$ , we post multiply your estimated relative pose between time $t − 1$ and $t$ by the ground truth pose at time $t − 1$ . This will give you a pose estimate at time $t$ that you can visualize in Rviz.**To
 do so, we use the ground-truth pose of the previous frame (obtained 
from ROS messages), “plus” the relative pose between current frame and 
previous frame (obtained from your algorithms, and then scale the 
translation using ground-truth), to compute the estimated (absolute) 
pose of the current frame, and then publish it.**

To run your code, use:

```bash
ros2 launch lab_6 video_tracking.launch.yaml
```

but be sure to modify the dataset path and parameters to run the correct method! For example, the`pose_estimator`parameter determines which algorithm to be used for the motion estimation.

**Note that we are cheating in this visualization since we use 
the ground truth from the previous time stamp. In practice, we cannot 
concatenate multiple estimates from 2-view geometry since they are up to
 scale (so for visualization, we use groundtruth to recover the scale).**

In the next deliverable we will see that 3D-3D correspondences allow us to reconstruct the correct scale for the translation.

### Deliverable 4: 3D-3D Correspondences [20 pts]

The rosbag we provide you also contains depth values registered with 
the RGB camera, this means that each pixel location in the RGB camera 
has an associated depth value in the Depth image.

In this part, we have provided code to scale to bearing vectors to 3D
 point clouds, and what you need to do is to use Arun’s algorithm (with 
RANSAC) to compute the drone’s relative pose from frame to frame.

1.`cameraCallback`: Implement Arun’s algorithm

Implement[Arun’s algorithm](http://laurentkneip.github.io/opengv/namespaceopengv_1_1point__cloud.html#a047c3c5a395a740e7f3f2b8573289211)in this function. Use the evaluateRPE function you used previously to**plot the rotation error and the translation error over time**as
 well. Mind that, in this case, there is no scale ambiguity, therefore 
we cannot really compare the translation error of this approach against 
the previous ones. Implement Arun’s algorithm*with*RANSAC using OpenGV.

To run your code, use:

```bash
ros2 launch lab_4 video_tracking.launch.yaml pose_estimator:=3
```

with the`pose_estimator`parameter set to`3`so that Arun’s method is used.

**Note that while we can now reconstruct the trajectory by 
concatenating the relative poses, such a trajectory estimate will 
quickly diverge due to error accumulation. In future lectures, we will 
study Visual-Odometry and Loop closure detection as two ways to mitigate
 the error accumulation.**

Performance Expectations

What levels of rotation and translation errors should one expect from
 using these different algorithms? To set the correct expection, we 
think the following errors are satisfactory:

- Using 5-point or 8-pt with RANSAC, for most of the frames, you can 
get rotation error below 1 degree and translation error below 0.5 (note 
that the translation error is between 0 and 2 since both ground-truth 
translation and estimated translation have unit norm), with 5-pt 
algorithm slightly outperforming 8-pt algorithm.
- Using 2-point with RANSAC, for most of the frames, you can get the 
translation error below 0.1 (note that the translation error is between 0
 and 2).
- Using 3-point with RANSAC (3D-3D), for most of the frames, you can 
get rotation error below 0.1 degree, and translation error below 0.1 (if
 you normalize the translations), and even smaller if you don’t 
normalize the translations since the frame rate is very high.

### **Delivery 5: Pose estimation in real world! [20 Pts]**

In this exercise, you collect data when you drive the car in mini 
city. You need to drive the car in the minicity on a rectangular path 
shown in the picture. Try to drive in in the yellow line, which 
helps later for comparing with the ground truth. Measure the rectangle 
with the ruler, which you will use it as a baseline to compare with your
 estimation.

![square.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/square.png)

In order to collect a suitable rosbag, you must follow these steps inside the car:

1. First pull the repository

```bash
git pull
```

2. Drive the car using teleop

```bash
source /opt/ros/jazzy/setup.bash
cd ~/Vnavros2setup/workspaces/f1tenth_ws
```

3. Launch camera by running the following command. This ensures you have all the topics you need be published:

```bash
ros2 run realsense2_camera realsense2_camera_node --ros-args -p enable_color:=true -p spatial_filter.enable:=true -p temporal_filter.enable:=true -p accel_qos:=DEFAULT
```

4. Collect the rosbag of your trajectory of your car with all topics

`ros2 bag record -a`

5. The rosbag must contain raw RGB images (and IMU if want to 
work on task 2) for 2D-2D correspondence and depth image (requird 
for task 3 only). Please note that you may only record the topics you 
needed. Or if you do not wish to delivery 5 option 3, you may disable 
the depth (it is disabled by default), so you do not record a large 
amount of data.

6. After you collected the rosbag, you can upload it in your personal
 Google Drive or your Cloud/one drive via Remote Desktop. Then share it 
with your teammate for the next step. Please review the following tasks 
for the next step.

- **Important: Please follow the instructions to know how to use the car.**

**Camera calibration:**
 to get the reasonable result for your estimation, you have to change 
the camera calibration parameters (K and D) in pose_estimation 
file.

You can retrieve the camera calibration provided by manufacturer by:

`ros2 topic echo /camera/color/camera_info`

**Note that this is the default 
values for camera calibration parameters. To get the accurate value, you
 have to calibrate the camera. The camera calibration is a time 
consuming process. Although you need to do it for final project, but for
 this assignment is optional [+10 extra points]**

```bash

```

**Delivery 5 Tasks**

1. Run 2D-2D correspondence using the camera images. Plot the 
estimated relative pose of the camera (i.e.,the trajectory of the 
car) in 3D world. We do not have any ground truth; however, you 
have to explain if your estimation seems accurate by comparing 
with the approximated ground truth which can be measured by using the 
measuring tape provided for you in the cabinet of robots (please make 
sure you put it back after you use it) .

2. Optional [extra 10 pts], run 2 point algorithm using IMU data and 
plot estimated relative pose of the camera (i.e.,the trajectory of
 the car) in 3D.

3. Optional [extra 10 pts], run 3D-3D correspondence. For this 
exercise, you have to collect depth information along with stereo 
images. Then run the 3 point algorithm and plot estimated 
relative pose of the camera (i.e.,the trajectory of the car) in 
3D.

Note: please make sure you push your changes in a new folder for 
delivery5 outside lab4. Also, you are not going to compute error in the 
delivery5 as there is no ground truth to compare with.

## Summary of Team Deliverables

For a given dataset, we require you to run**all algorithms** (if applicable) on it and compare their performances. Therefore, as a summary for Team Deliverables:

1. Part 2: Plots of translation and rotation error for each of the 
methods (5pt, 8pt, 2pt, Arun 3 pt) using the given rosbag (using RANSAC 
is required, while without RANSAC is optional).
2. Part 3: repeat the tests using a rosbag you collect by car in 
minicity, plot the trajectory of the car/camera in 3D. overlay the
 estimated trajectory vs the ground truth you measure in the minicity 
(uptoscale)

---

**Previous**: [[Lab 3 - Exercises|⬅ Lab 3: Perspective Projection & Features]] | **Next**: [[Lab 5 - Exercises|Lab 5: Bundle Adjustment & Factor Graphs ➔]]
