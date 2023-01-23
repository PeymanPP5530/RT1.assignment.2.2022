#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import odom_custom_msg
import os

start_description_flag=1



def callback(data):

    my_publisher = rospy.Publisher('position_and_velocity', odom_custom_msg, queue_size=5)

    my_custom_message = odom_custom_msg()

    my_custom_message.x = data.pose.pose.position.x
    my_custom_message.y = data.pose.pose.position.y
    my_custom_message.vel_x = data.twist.twist.linear.x
    my_custom_message.vel_y = data.twist.twist.linear.y

    print("----------------------------------------")
    print(my_custom_message)
    my_publisher.publish(my_custom_message)

   # rospy.sleep(1)   This node publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom.

def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This node publishes the robot position and velocity ")
        print("as a custom message (x,y, vel_x, vel_z), by relying ")
        print("on the values published on the topic /odom.")
        input("\n\nPress Enter to continue!")
        start_description_flag=0   
    

if __name__ == '__main__':

    start_description(start_description_flag)
    rospy.init_node('NodeB')    
    rospy.Subscriber("/odom", Odometry, callback)
    
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()
