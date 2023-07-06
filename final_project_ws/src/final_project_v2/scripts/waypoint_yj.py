#!/usr/bin/env python3

import rospy
import time
import tf.transformations

from std_msgs.msg import Empty
from geometry_msgs.msg import PoseWithCovarianceStamped

# wp_id : (x, y)
wp_list = {1 : (4.5, 0.7),
           2 : (5.36, -3.37),
           3 : (-6.25, -3.9),
           4 : (-12.5, -0.7),
           5 : (-9.5, 0.02)}

"""
user:~$ rosmsg show geometry_msgs/PoseWithCovarianceStamped
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
"""

def talker():
    pub_wp = rospy.Publisher('my_t3_waypoints', PoseWithCovarianceStamped, queue_size=1)
    pub_path_ready = rospy.Publisher('path_ready', Empty, queue_size=1)

    rospy.init_node('waypoint_publisher', anonymous=True)
    rate = rospy.Rate(10) # hz

    my_wp = PoseWithCovarianceStamped()
    my_wp.header.stamp = rospy.Time.now()
    my_wp.header.frame_id = 'odom'

    init_roll = 0.0
    init_pitch = 0.0
    init_yaw = 0.64

    quaternion = tf.transformations.quaternion_from_euler(init_roll, init_pitch, init_yaw)
	# transfromation from roll, pitch, yaw to x y z w
    
    my_wp.pose.pose.orientation.x = quaternion[0]
    my_wp.pose.pose.orientation.y = quaternion[1]
    my_wp.pose.pose.orientation.z = quaternion[2]
    my_wp.pose.pose.orientation.w = quaternion[3]
    
    # my_wp.pose.pose.orientation.x = 0.0
    # my_wp.pose.pose.orientation.x = 0.0
    # my_wp.pose.pose.orientation.x = 0.3
    # my_wp.pose.pose.orientation.w = 0.9

    for i in range(len(wp_list)):
        rospy.loginfo("Waypoint" + str(i))
        my_wp.pose.pose.position.x = wp_list[i+1][0]
        my_wp.pose.pose.position.y = wp_list[i+1][1]

        while not rospy.is_shutdown():
            connections = pub_wp.get_num_connections()
            if connections > 0:
                pub_wp.publish(my_wp)
                break
            rospy.loginfo("Wait for 'my_t3_waypoints' topic")
            rate.sleep()

        rospy.loginfo("Published waypoint number " + str(i))
        time.sleep(2)

    start_command = Empty()

    while not rospy.is_shutdown():
        connections = pub_path_ready.get_num_connections()
        if connections > 0:
            pub_path_ready.publish(start_command)
            rospy.loginfo("Sent waypoint list execution command")
            break
        rospy.loginfo("Waiting for 'path_ready' topic")
        rate.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass