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
roslaunch final_project_v2 final_world_nav_jp_for_jp.launch    
roslaunch final_project_v2 start_follow_waypoints.launch    

## Result

### gif
![final_porject_demo](https://github.com/yujin-shim/gazebo-serving-robot-simulation/assets/108443602/fef49ab4-29b0-4375-9875-c8b0192fad2a)

### youtube-link
#### ver 1
[![Gazebo simulation](http://img.youtube.com/vi/Gd7UHNoDKlw/sddefault.jpg)](https://youtu.be/Gd7UHNoDKlw?t=0s) 

#### ver2 - path planning improved
[![Gazebo simulation](http://img.youtube.com/vi/dQZdvLGBVOU/sddefault.jpg)](https://youtu.be/dQZdvLGBVOU?t=0s) 

---

## Details
### Local map parameters  
While a larger local costmap can provide more information about the environment and potentially improve path planning, it also comes with some drawbacks.  
As the local costmap increases in size, there is a possibility of the sensor capturing noisy data or mistakenly recognizing obstacles that are located farther away.

- width & height : 5  
  ![param5](https://github.com/yujin-shim/gazebo-serving-robot-simulation/assets/108443602/9cdedd4a-cd89-4a94-b28d-4af3bdc077fe)  
  The robot encounters difficulty when navigating corners, repeatedly recalculating the local path.

- width & height : 1.5  
  ![param1 5](https://github.com/yujin-shim/gazebo-serving-robot-simulation/assets/108443602/5a39c302-2a2f-4ca4-9d1d-20eb34052001)  
  The robot shows smooth cornering
