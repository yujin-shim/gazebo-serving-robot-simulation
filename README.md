# Gazebo - Serving robot simulation
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyujin-shim%2Fgazebo-serving-robot-simulation&count_bg=%23FFD89C&title_bg=%23A2CDB0&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

<img src="https://img.shields.io/badge/ros-22314E?style=plastic&logo=ROS&logoColor=white"/> <img src="https://img.shields.io/badge/CMake-064F8C?style=plastic&logo=cmake&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white"/>

* all the project was produced by programmers
* team_mate : yujin, geonwoo, jungpin, chanyoung
* 2023-07-03~2023-07-05
* we are still working on the project to improve the navigation part

# Project

## task1 - mapping & localization 

- cafe world
- using gmapping and map_server, map the world and save as .pgm & yaml file
- localication is done by AMCL node

## task2 - navigation
- navigation using move_base,global & local planner

## task3 - mission for serving robot
- used state machine, waypoints were given as constant(list)
### mission 
- starting from #1
- move through #2 - #3 - #4 - #5 - #6

![Screenshot from 2023-07-05 17-56-02](https://github.com/yujin-shim/gazebo-serving-robot-simulation/assets/108443602/598b1b4f-6378-49bb-9cbf-8787b80c8679)



# Running
roslaunch final_project final_world_nav.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch
rosrun final_project waypoint_yj.py

## Result

![final_porject_demo](https://github.com/yujin-shim/gazebo-serving-robot-simulation/assets/108443602/fef49ab4-29b0-4375-9875-c8b0192fad2a)

