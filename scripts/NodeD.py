#!/usr/bin/env python3


from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import math

from assignment_2_2022.msg import odom_custom_msg

import rospy

counter =0
temp_vel =0
avg_vel =0
des_pos_distance=0


# def callback(req):
#     global cancel_counetr,reach_counter
#     print(f"Number of canceled goal: {cancel_counetr} , number of reached goal: {reach_counter}")
#     return EmptyResponse()


def callback_subscriber(data):

    des_pos_x = rospy.get_param("/des_pos_x")
    des_pos_y = rospy.get_param("/des_pos_y")

    cur_pos_x = data.x
    cur_pos_y = data.y

    cur_vel_x = data.vel_x
    cur_vel_y = data.vel_y


    cur_vel= math.sqrt(((cur_vel_x)**2)+((cur_vel_y)**2))

    global counter
    global temp_vel
    global avg_vel
    global des_pos_distance

    if counter<5:

        temp_vel=temp_vel+cur_vel
        counter +=1

    elif counter==5:

        counter=0
        temp_vel /= 5
        avg_vel=temp_vel
        temp_vel=0

    des_pos_distance= math.sqrt(((des_pos_x - cur_pos_x)**2)+((des_pos_y - cur_pos_y)**2))


    





if __name__ == "__main__":

    rospy.logwarn("NodeD started")

    rospy.init_node('NodeD')
    
    rate = rospy.Rate(rospy.get_param("/print_interval"))

    rospy.Subscriber("chatter", odom_custom_msg, callback_subscriber)

    while not rospy.is_shutdown():

        print(f"distance: {des_pos_distance : .3f}")
        print(f'average velocity: {avg_vel: .3f}')
        print(f"---------------------------")
        rate.sleep()
