#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg


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




if __name__ == "__main__":

    rospy.logwarn("service started")

    rospy.init_node('NodeC')

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)

    rospy.Service('reach_cancel_ints', Empty, callback_service)

    rospy.spin()