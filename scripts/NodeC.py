#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os

start_description_flag=1


reached_goal_counter =0
canceled_goal_counetr = 0
sequence =1 


def callback_service(req):
    global canceled_goal_counetr , reached_goal_counter , sequence
    print(f"Sequence: {sequence}\nNumber of canceled goal: {canceled_goal_counetr}\nnumber of reached goal: {reached_goal_counter}")
    print("-------------------------------------")
    sequence += 1
    return EmptyResponse()



def callback_subscriber(data):

    if data.status.status == 2:

        global canceled_goal_counetr
        canceled_goal_counetr += 1
    
    elif data.status.status == 3:

        global reached_goal_counter
        reached_goal_counter += 1


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This node is a service node that, when called,")
        print("prints the number of goals reached and canceled.")
        input("\n\nPress Enter to continue!")
        start_description_flag=0   


if __name__ == "__main__":

    start_description(start_description_flag)

    rospy.logwarn("service started")

    rospy.init_node('NodeC')

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)

    rospy.Service('reach_cancel_ints', Empty, callback_service)

    rospy.spin()