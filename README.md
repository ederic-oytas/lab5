# Lab 5: Follow the Gap

In this lab, you'll work on your "Follow the Gap" algorithm, which you'll use
for Race 1. Each team will demonstrate and submit one implementation of the
algorithm.

## Learning Goals

* Implement the "Follow the Gap" algorithm to navigate an entire racetrack,
  avoiding any obstacles on the track.
* Fine-tune parameters to ensure safety and optimize performance.

## Lab Setup

We will build off the local file structure given in the first lab. Keep this
structure in mind while you are working through the instructions!

```
${HOME}
  |
  +-- lab1_ws/              -- Lab 1 Workspace folder
  |
  +-- lab2_ws/              -- Lab 2 Workspace folder
  |
  +-- lab3_ws/              -- Lab 3 Workspace folder
  |
  +-- lab4_ws/              -- Lab 4 Workspace folder
  |
  +-- lab5_ws/              -- Lab 5 Workspace folder (NEW)
  |
  +-- sim_ws/               -- Simulator Workspace folder
```

To start with the lab, clone the repository:

```bash
cd ~
git clone https://github.com/unlv-f1/lab5 lab5_ws
```

Then, mount *~/lab5_ws* onto your Docker container, just as you've done for the
previous labs. The repository contains the base code for you to get started.

## Part 1: Follow the Gap Overview

The lecture slides provide the best visual resources for understanding the
Follow the Gap algorithm. In summary, the steps are:

1. Preprocess (Modify) LiDAR scans
    * Extend disparities
    * Deploy safety bubble

2. Identify all gaps and select a gap to follow
    * Options for selection:
        * Widest gap
        * Deepest gap (gap with deepest point)
        * (Your own custom method?)

3. Find best point in gap
    * Options for selecting best point:
        * Furthest point
        * "Better Idea" discussed in lecture
        * (Your own custom method?)

4. Drive the car to drive toward best point
    * Calculate steering angle
    * Calculate drive speed
    * Publish

Additionally, you may need to adjust your algorithm for the following issues:

* **Wiggling**: When going down a long hallway, your algorithm may "wiggle"
  because it is switching between two far-apart points.
* **Going around corners**: When going around corners, be careful to publish a
  steering angle which may hit the corner.

## Part 2: Implementation

### 2-1: Specification

Create a package named `gap_follow`, which implements the Follow the Gap
algorithm.

#### Running Your Package

You are free to run your package by using either `ros2 launch` or `ros2 run`.
You may include parameters that you think are necessary for running your node
successfully.

Here is an example `ros2 run` invocation:

```bash
ros2 run gap_follow gap_follow_node --ros-args \
    -p drive_speed_min:=1.0 \
    -p drive_speed_max:=5.0 \
    -p safety_bubble_diameter:=0.3 \
    -p disparity_threshold:=0.3 \
    -p disparity_extension_length:=0.3 \
    -p gap_depth_threshold:=1.0 \
    -p gap_width_threshold:=5
```

Here is an example `ros2 run` invocation using a parameter file. (All parameter
values are stored in this file instead.)

```bash
ros2 run gap_follow gap_follow_node --ros-args --params-file path/to/params-file.yaml
```

#### Simulator Demonstration

Demonstrate your implementation by completing one lap around the track
**without collision** on two maps in RViz:

1. `levine_blocked` (levine map with exits blocked)
2. `levine_obs` (blocked levine map with obstacles)

#### Vehicle Demonstration

Demonstrate your implementation by completing two laps around the track
**without collision**.

1. The first lap is on the track **without** any obstacles
2. The second lap is on the track **with** obstacles.

#### Code Submission

Your team will submit a link to your repository on Canvas.

### 2-2: Changing Maps

To test your implementation on the new maps, you'll need to change the map that
`f1tenth_gym_ros` uses.

First, download the map files from this repository:

* `maps/levine_blocked.png`
* `maps/levine_blocked.yaml`
* `maps/levine_obs.png`
* `maps/levine_obs.yaml`

Put these inside your `/sim_ws/src/f1tenth_gym_ros/maps` directory inside your
container. The directory should look like this:

```
/sim_ws/src/f1tenth_gym_ros/maps
  |
  +-- levine.png
  |
  +-- levine.yaml
  |
  +-- levine_blocked.png     -- NEW FILE
  |
  +-- levine_blocked.yaml    -- NEW FILE
  |
  +-- levine_obs.png         -- NEW FILE
  |
  +-- levine_obs.yaml        -- NEW FILE
  |
  +-- Spielberg_map.png
  |
  +-- Spielberg_map.yaml
```

Then, edit your `/sim_ws/src/f1tenth_gym_ros/config/sim.yaml`, find the line
for `map_path`. You'll see that the current value is set to this:

```yaml
    map_path: '/sim_ws/src/f1tenth_gym_ros/maps/levine'
```

To change the map to `levine_blocked`, change it:

```yaml
    map_yaml: '/sim_ws/src/f1tenth_gym_ros/maps/levine_blocked'
```

Then, rebuild the `f1tenth_gym_ros` package using:

```bash
cd /sim_ws
colcon build --packages-select f1tenth_gym_ros
source install/local_setup.bash
```

Then, launch the gym:

```bash
ros2 launch f1tenth_gym_ros gym_bridge_launch.py
```

You should see that the map has changed to `levine_blocked`.

### 2-3: Tips for Testing

This lab is larger than the previous labs in terms of the amount of code. As a
result, students in the past have struggled to pinpoint the exact part of their
code which caused issues.

Thus, it's recommended that you visualize the effects of your code in RViz.
Consider publishing messages containing your modified laser scan ranges to a
topic and displaying that in RViz. You can also make use of **ROS 2 markers** to
display custom shapes, lines, and text in RViz.

## Grading Rubric

* Simulator Demonstration: **50** points
* Vehicle Demonstration: **50** points

## Extra Resources

* UNC Follow the Gap Video: https://youtu.be/ctTJHueaTcY
* Tutorial on parameter files from the Robotics Back-End:
  https://roboticsbackend.com/ros2-yaml-params/
* ROS 2 Markers Tutorial:
  https://docs.ros.org/en/jazzy/Tutorials/Intermediate/RViz/Marker-Display-types/Marker-Display-types.html
    * Note: This is for a newer ROS 2 distro, but the tutorial tips should help
      regardless.
