---
title: "Lab 6 - Exercises"
tags:
  - vnav
  - labs
---

# Lab 6 - Exercises

> [!warning] Submission Deadline
> This lab will be cloned from both individual and team repos on **November 14th at 11:59 PM**. Submit files in a folder called `lab6`.

> [!info] Overview: YOLO & Factor Graph Estimation
> In this lab, we use **YOLO** as a front-end object detector and solve for the 3D position of target objects using **GTSAM** factor graphs.
> We use the [RGB-D TUM Freiburg3 Teddy sequence](https://cvg.cit.tum.de/data/datasets/rgbd-dataset/download).

## **Individual part**

## **Deliverable 1 [30 points]**

Read the[DBoW paper](http://doriangalvez.com/papers/GalvezTRO12.pdf)paper.
 Then provide answers to the following questions. When complete, your 
writeup should be 1+ page long – aim for each response to be 200-250 
words. Be sure to give speific examples in your response and include 
pictures or diagrams as needed. Your goal is to convince the grader you 
deeply understand this topic.

1. [10 points] Explain which components provide robustness against 
illumination and 3D viewpoint changes in a basic BoW-based place 
recognition system. Why?
2. [10 points] Explain the purpose of Inverse Document Frequency (IDF) term (i.e.,`tf-idf`). What would happen without this term and why? [5 points]
  - Hint: Additional resources for building intuition include[the citation provided in the DBoW paper](https://scholar.google.com/citations?view_op=view_citation&citation_for_view=NCtKHnQAAAAJ:u5HHmVD_uO8C)or[this tutorial](https://www.analyticsvidhya.com/blog/2020/02/quick-introduction-bag-of-words-bow-tf-idf/).

3. [10 points] How does the vocabulary size in BoW-based systems affect
 the performance of the system? Consider performance metrics such as: 
(i) computational cost, (ii) precision, (iii) recall.
  - Hint: How would adding words to the vocabulary change 
the ability to identify 2 documents/images are similar? Are more words 
always better?

## **Team Deliverable [70 points]**

**Purpose:**Use YOLO as a front end 
object detector to solve a back end estimation problem with GTSAM. 
Practice developing with ROS2 with less “training wheels”.

Recall, YOLO is a Convolutional Neural Network based on the paper[“You Only Look Once: Unified, Real-Time Object Detection”](https://pjreddie.com/media/files/papers/yolo.pdf).

In the previous part we setup and used YOLO to detect objects in 
various images. This time we will use YOLO as a front end to detect an 
object of interest across multiple frames of a video, and solve for the 
object’s position with GTSAM by building a factor graph of camera poses 
with object detections.

The[RGB-D TUM dataset](https://cvg.cit.tum.de/data/datasets/rgbd-dataset/download)is
 a popular video benchmarking dataset (with ground truth) for various 
robotic vision applications. We specifically will be using the`freiburg3_teddy`sequence.
 This dataset is great, but it was collected in the early 2010s so a few
 things are outdated (i.e., their video previews use Flash and the data 
is in ROS1). Luckily, we updated the data for you! Checkout a video 
preview of`freiburg3_teddy`[here](https://drive.google.com/file/d/1uuRuJu8dAj0L5MA0jE8qFdQjlQPO8dF-/view?usp=sharing). Our goal will be to determine the position of the Teddy Bear!

Although we still provide starter code for this deliverable, you will
 be given a lot more freedom implementing this deliverable. This is to 
better simulate how one might use ROS2 in their research (i.e., with 
less “training wheels”).

## Installation & Setup

This lab assumes you already have your VNAV workspace setup, with ROS2, OpenCV, and GTSAM installed from the earlier labs.

## Deliverable 2 - Running YOLO w/ Ultralytics [20 pts]

**Purpose of this Question:**YOLO is a
 seminal work in our domain. Especially given how easy it is to 
install/run these days, everyone working in this space should know how 
to do this.

Since the[introduction of YOLO (You Only Look Once) in 2015](https://scholar.google.com/citations?view_op=view_citation&citation_for_view=TDk_NfkAAAAJ:u-x6o8ySG0sC)(yes,
 a seminal work is named after a meme), YOLO and its evolutions (aptly 
named YOLOv2, YOLOv3, etc.) have become a staple in object detection, 
image segmentation, etc.

These days, you can easily install[YOLOv11 through the Ultralytics](https://github.com/ultralytics/ultralytics)package through`pip`,`docker`,
 etc. Once installed, you can easily perform detection, image 
sementation, etc. through easy code wrappers (e.g., Python) or via 
command line.

1. Explain the following tasks in your own words:
  - Detection
  - Segmentation
  - Classification
  - Oriented Bounding Box Detection
  - Hint: Checkout the[official YOLOv11 documentation](https://docs.ultralytics.com/)

2. Install[YOLOv11 through the Ultralytics](https://github.com/ultralytics/ultralytics)package. We recommend using`pip`since it is the most straight forward.
  - Hint: If you install via`pip`to the user and your command line doesn’t find`yolo`, you might need to include`~/.local/bin`on your terminal’s`$PATH`variable. You can do this by adding`PATH="$PATH:~/.local/bin"`to your`~/.bashrc`file and resourcing with`source ~/.bashrc`.
  - Hint: If`yolo`is not detecting your file, try giving an absolute or relative path. It appears the`source=`command line parameter does not expand`~`to`$HOME`.

3. Select some pictures of your choice (taking your own pictures is 
highly encouraged!) – don’t just use the example picture in the 
Ultralytics documentation (i.e.,`https://ultralytics.com/images/bus.jpg`).
 Use YOLOv11 (we recommend the CLI since it is the most straight 
forward) to perform the 5 tasks outlined above. Make sure to select 
images that make it clear the system is working (e.g., an image without a
 person in it won’t make sense for pose detection). Include your 
processed images in your PDF – be sure to state which image corresponds 
with which task.
4. **(Optional) Extra Credit (5 pts):**Install
 and run YOLOv11 through the official Docker image. How did you “get 
your image” into the Docker image? How did you “get the processed image”
 out of the Docker image? Provide a short explaination and a 
screenshot(s) of it running on your computer.

### **Setup the code for Deliverable 3:**

### Downloading the dataset as a ROS2 bag

1. If you don’t already have one, create a data folder within your VNAV workspace:

```bash
mkdir -p ~/vnav/data
```
2. Download the`freiburg3_teddy`sequence as a ROS2 bag[here](https://drive.google.com/file/d/1oxf73-Ge2Nrh__ZSMpGtfyqLmHVkHH9s/view?usp=sharing). Place it in`~/vnav/data`.
3. Uncompress the data with the following command:

```bash
tar xzvf lab6_data.tar.gz
```

You should now have a folder called`rgbd_dataset_freiburg3_teddy`with the following files:

```bash
~/vnav/data/rgbd_dataset_freiburg3_teddy
├── metadata.yaml
└── rgbd_dataset_freiburg3_teddy.db3
```
4. Try running the bag with:

```bash
ros2 bag play -l ~/vnav/data/rgbd_dataset_freiburg3_teddy
```

and viewing the image data in either`rviz`or`rqt`. Note the`-l`argument will infinitely repeat the bag replay.

### Setup code

1. Update the starter code repo:

```bash
cd ~/vnav/labs
git pull
```
2. Copy relevant starter code to your`team-submissions`repo:

```bash
cp -r ~/vnav/labs/lab6 ~/vnav/team-submissions
```
3. Link submission code to your code:

```bash
mkdir -p ~/vnav/ws/lab6/src
cd ~/vnav/ws/lab6/src
ln -s ../../../team-submissions/lab6 lab_6
```
4. Clone and setup the[Ultralytics ROS2 package](https://github.com/Alpaca-zip/ultralytics_ros):

```
cd ~/vnav/ws/lab6/src
GIT_LFS_SKIP_SMUDGE=1 git clone -b humble-devel https://github.com/Alpaca-zip/ultralytics_ros.git
rosdep install -r -y -i --from-paths .For this lab, you need to use virtual environment for Python packages. For example:python3 -m venv ~/.venvs/ultra_ros If it says “venv not found,” install it:
```

`sudo apt install python3-venv -y`

Now, activate it:

```bash
source ~/.venvs/ultra_ros/bin/activate
```
5. Now Install PyTorch, TorchVision, and TorchAudio in this virtual environment

#### a) With CPU only (no CUDA):

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

#### b) If you have a CUDA GPU (e.g., NVIDIA card):

First, check your CUDA version:

```bash
nvidia-smi
```

Then choose the matching PyTorch version, e.g.:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

If you received any error regarding pyyaml, install them:

`pip install pyyaml typeguard`

`pip install pyyaml typeguard empy numpy catkin_pkg`

`pip install --upgrade pip`

Then try installing pytorch again:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

After installing PyTorch, install following packages

```bash
pip install --upgrade pip setuptools wheel
```

```bash
pip install lapxpip install numpypip install --no-deps lapx
```

1. Build the starter code:

```bash
cd ~/vnav/ws/lab6
colcon buildNote: if the build failed, go to ultralytics_ros and build it manually:colcon build --packages-select ultralytics_ros
```
2. Confirm your`~/.bashrc`now contains the following line to source lab6:

```bash
source ~/vnav/ws/lab6/install/setup.bash
```
3. ```bash
source ~/.bashrc
```

### Running the starter code

1. To test our code, we want to play the ROS2 bag and launch YOLO to process frames:

```bash
# terminal 1
ros2 bag play -l ~/vnav/data/rgbd_dataset_freiburg3_teddy
# terminal 2
ros2 launch ultralytics_ros tracker.launch.xml debug:=true input_topic:=/camera/rgb/image_color
```

Note that`input_topic:=/camera/rgb/image_color`is telling YOLO to process data on that bag topic. By default, YOLO will send processed frames to the`/yolo_image`topic.
2. Open up`rviz`or`rqt`to confirm YOLO is running. Confirm you can see something like this:

![yolo-running.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/yolo-running.png)

Note: Depending on your computer hardware, YOLO may not run at the same framerate as the original video.
3. Run the starter C++ code with:

```bash
# terminal 3
ros2 run lab_6 deliverable_3
```

The starter code should show you how to get camera pose information from`/tf`and pixel information about YOLO’s “Teddy Bear” detections. This will be needed for your implementation!

## Deliverable 3 - Object Localization [50 pts]

Our goal for this exercise is to localize the teddy bear that is at the center of the scene in the`freiburg3_teddy`dataset.
 To do so, we will use YOLO detections to know where the teddy bear is. 
With the bounding box of the teddy bear, we can calculate a crude 
approximation of the*bear’s 3D position*by
 using the center pixel of the bounding box. If we accumulate enough 2D 
measurements, we can formulate a least-squares problem in GTSAM to 
triangulate the 3D position of the teddy bear.

For that, we will need to perform the following steps:

1. Examine the C++ starter code to understand how we are (i) getting 
the ground-truth transformation of the camera with respect to the world 
from the`tf`topic and (ii) getting the center of the Teddy Bear bounding box from YOLO.
2. Formulate a GTSAM problem where we are trying to estimate the 3D 
position of the center pixel in the bounding box. You will need to use 
multiple`GenericProjectionFactors`in order to fully constrain the 3D position of the teddy bear and estimate the 3D position of the teddy bear. (*Recall
 the GTSAM exercise where you performed a toy-example of Bundle 
Adjustment problem and use the same factors to build the problem.*) 
Note that now, the poses of the camera are given to you as ground-truth 
information, so you might want to this as priors instead of as odometry.*Tip: If you need it, the bag file has camera calibration info in the`camera_info`topics.*
3. Solve the problem in GTSAM.*(Consider repurposing code from`lab_5`!)*
4. In`rviz`,
 plot the (i) estimated 3D position of the teddy bear, (ii) the 
trajectory of the camera, and (iii) which frames got a good detection of
 the teddy bear. For instance, your`rviz`should look something like this:

![deliverable_2.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/deliverable_2.png)

where the green line is (i), purple sphere is (ii), and the red arrows are (iii).

- **(Optional) Extra Credit (10 pts)**Calculate the covariance of the teddy bear estimate, place it in a`geometry_msgs::PoseWithCovariance`message, and plot it in`rviz`using the size of the sphere to represent the covariance.

### [Optional +15 points] Deliverable 4: RTDMAP for Loop closure detection

Follow the instruction [here](https://github.com/introlab/rtabmap_ros#installation) and follow the [tutorial](https://github.com/introlab/rtabmap/wiki/Loop-closure-detection) 
 for loop closure detection example. You need take some pictures from 
minicity (preferably using mounted real sense cameras) and find the 
matched images. Try to take some pictures from the same location but 
from different angles. take few snapshots of the RTDMAP application when
 you run it in multiple instances and submit it as your deliverables. 
Explain RTMAP and how it detects the loop closure.

Note: you may find more examples in the [tutorial page](https://github.com/introlab/rtabmap/wiki/Tutorials) that you would like to try!

Also RTDMAP wiki page can be found [here](https://github.com/introlab/rtabmap/wiki).

### What to submit in team deliverables

To evaluate this deliverable, we will examine your implementation, 
but will not focus on the end result (although it will count). Instead 
we ask you add a PDF to your team submission repo called`lab6-team-writeup.pdf`with the following information:

1. A small summary of your design choices and considerations taken in order to solve this problem.
2. Your “best” estimate of the position of the teddy bear as`geometry_msgs::PointStamped`message.
3. A screenshot of`rviz`showing the plotted information (as explained above).
4. **(Optional)**If you did the extra 
credit covariance calculation and plotting above, include an additional 
screenshot and the “best” estimate of covariance as a`geometry_msgs::PoseWithCovariance`message.Re-source your`~/.bashrc`to ensure lab6 is sourced in your current session:
5. [Optional] Explain RTMAP and how it detects the loop closure. 
Submit screen shots/video recording of RTMAP (video is preferred) 
showing loop closure detection in minicity

All together this writeup should be at least 250 words.

```bash

```
