#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

import actionlib.msg
import assignment_2_2022.msg
#from std_srvs.srv import *


# Brings in the SimpleActionClient
import actionlib
import assignment_2_2022.msg
import os

start_description_flag=1





def target_client():


    x_position = input("\nPlease enter X position: ")
    y_position = input("Please enter Y position: ")

 
    x_position = int(x_position)
    y_position = int(y_position)
 
    print(f'\nYou entered: \nposition X: {x_position}  \nposition Y: {y_position}')
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    #global client

 

    # Waits until the action server has started up and started
    # listening for goals.

    print("\n###############################################")
    print("\nWating for connection to the action server")

    client.wait_for_server()

    # Creates a goal to send to the action server.
    #goal = actionlib_tutorials.msg.FibonacciGoal(order=20)


    goal = PoseStamped()


    goal.pose.position.x = x_position
    goal.pose.position.y = y_position

    goal = assignment_2_2022.msg.PlanningGoal(goal)

   # rospy.sleep(1)
    
    # Sends the goal to the action server.
    client.send_goal(goal)
    print("\n**Goal sent to the sever**")
    input("\nPress Enter to select an operation!")
    # rospy.sleep(8)
    # client.cancel_goal()
    interface()
      


    # Waits for the server to finish performing the action.
    #####client.wait_for_result()


def cancel_target():

    #client = actionlib.SimpleActionClient('/reaching_goal',actionlib_msgs/GoalID )
    #global client
    #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    # Waits until the action server has started up and started
    # listening for goals.
    #client.wait_for_server()
    client.cancel_goal()
    print(f"\nTarget canceled")
    input("\n\nPress Enter to select an operation!")
    interface()



def wrong():

    print("!!!! Wrong input !!!!")
    rospy.sleep(2)
    interface()



def interface():

    os.system('clear')
    print("###############################################\n")    
    print("##          Robot control interface          ##\n")
    print("###############################################\n")
    print("1:Target position\n")
    print("2:Cancel\n")
    print("3:Exit\n")   

    user_selection = input("Select your operation: ")
    
    if   (user_selection == "1"):
        target_client()

    elif (user_selection == "2"):
        cancel_target() 

    elif (user_selection == "3"):
        exit()

    else:
        wrong()


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This is the node that implements an action client, ")
        print("allowing the user to set a target (x, y) or to ")
        print("cancel it.")
        input("\n\nPress Enter to continue!")
        start_description_flag=0   

    

if __name__ == '__main__':
    # try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
    start_description(start_description_flag)

    rospy.init_node('NodeA')
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    interface()

    rospy.spin()
    # except rospy.ROSInterruptException:
    #     print("program interrupted before completion", file=sys.stderr)
