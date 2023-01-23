#!/usr/bin/env python3


import math
from assignment_2_2022.msg import odom_custom_msg
import rospy
import os

start_description_flag=1

counter =0
temp_vel =0
avg_vel =0
des_pos_distance=0





def callback_subscriber(data):

    global counter
    global temp_vel
    global avg_vel
    global des_pos_distance

    des_pos_x = rospy.get_param("/des_pos_x")
    des_pos_y = rospy.get_param("/des_pos_y")

    cur_pos_x = data.x
    cur_pos_y = data.y

    des_pos_distance= math.sqrt(((des_pos_x - cur_pos_x)**2)+((des_pos_y - cur_pos_y)**2))



    cur_vel_x = data.vel_x
    cur_vel_y = data.vel_y

    cur_vel= math.sqrt(((cur_vel_x)**2)+((cur_vel_y)**2))

    if counter<5:

        temp_vel=temp_vel+cur_vel
        counter +=1

    elif counter==5:

        counter=0
        temp_vel /= 5
        avg_vel=temp_vel
        temp_vel=0


#This node subscribes to the robot’s position and velocity (using the custom message)
#  and prints the distance of the robot from the target and the robot’s average speed. 
# You can set the "print_interval" parameter in assignment_2_2022 launch flie to set how fast the node publishes the information.


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This node subscribes to the robot’s position and ")
        print("velocity (using the custom message) and prints the ")
        print("distance of the robot from the target and the ")
        print("robot’s average speed. ")
        print("You can set the \"print_interval\" parameter in ")
        print("assignment_2_2022 launch flie to set how fast the")
        print("node publishes the information.")
        

        input("\n\nPress Enter to continue!")
        start_description_flag=0   


    



if __name__ == "__main__":

    start_description(start_description_flag)

    rospy.logwarn("NodeD started")

    rospy.init_node('NodeD')
    
    rate = rospy.Rate(rospy.get_param("/print_interval"))

    rospy.Subscriber("position_and_velocity", odom_custom_msg, callback_subscriber)

    while not rospy.is_shutdown():

        print(f"distance: {des_pos_distance : .3f}")
        print(f'average velocity: {avg_vel: .3f}')
        print(f"---------------------------")
        rate.sleep()
