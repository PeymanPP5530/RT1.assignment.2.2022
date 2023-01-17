#!/usr/bin/env python3


from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg

import rospy

reach_counter =0
cancel_counetr = 0


def callback(req):
    global cancel_counetr,reach_counter
    print(f"Number of canceled goal: {cancel_counetr} , number of reached goal: {reach_counter}")
    return EmptyResponse()

def callback_subscriber(data):


    if data.status.status == 2:

        global cancel_counetr
        cancel_counetr += 1
    
    elif data.status.status == 3:

        global reach_counter
        reach_counter += 1




if __name__ == "__main__":

    rospy.logwarn("service started")

    rospy.init_node('reach_cancel_node')

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)

    rospy.Service('reach_cancel_ints', Empty, callback)

    rospy.spin()