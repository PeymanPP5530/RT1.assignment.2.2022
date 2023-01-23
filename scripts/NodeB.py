#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import odom_custom_msg


def callback(data):

    my_publisher = rospy.Publisher('position_and_velocity', odom_custom_msg, queue_size=5)

    my_custom_message = odom_custom_msg()

    my_custom_message.x = data.pose.pose.position.x
    my_custom_message.y = data.pose.pose.position.y
    my_custom_message.vel_x = data.twist.twist.linear.x
    my_custom_message.vel_y = data.twist.twist.linear.y

    print("###################################")
    print(my_custom_message)
    my_publisher.publish(my_custom_message)

   # rospy.sleep(1)   
    

if __name__ == '__main__':

    rospy.init_node('NodeB')    
    rospy.Subscriber("/odom", Odometry, callback)
    
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()
