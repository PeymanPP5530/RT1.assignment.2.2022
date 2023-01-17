#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Point, Pose, Twist
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from tf import transformations
from std_srvs.srv import *
import time

# Brings in the SimpleActionClient
import actionlib
import actionlib_msgs
import assignment_2_2022.msg

import os







def target_client():


    value1 = input("Please enter X position:")
    value2 = input("Please enter Y position:")
 
    value1 = int(value1)
    value2 = int(value2)
 
    print(f'You entered position X:{value1} and position Y:{value2}')
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    #client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    global client

    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )

    # Waits until the action server has started up and started
    # listening for goals.
    print("\nWating for connection to the action server")
    client.wait_for_server()

    # Creates a goal to send to the action server.
    #goal = actionlib_tutorials.msg.FibonacciGoal(order=20)


    goal = PoseStamped()


    goal.pose.position.x = value1
    goal.pose.position.y = value2

    goal = assignment_2_2022.msg.PlanningGoal(goal)

    rospy.sleep(1)
    
    # Sends the goal to the action server.
    client.send_goal(goal)
    print("\nGoal sent to the sever")
    rospy.sleep(2)
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
    print(f'target canceled')
    interface()


def input_client():

    print("            Robot control interface            ")
    value1 = input("enter 1 for set target position and 2 for cancelation\n ")
    
    if(value1=="1"):
        target_client()
    elif(value1=="2"):
        cancel_target()  

def interface():
    os.system('clear')
    print("###############################################\n")    
    print("            Robot control interface            \n")
    print("###############################################\n")
    print("Select your operation:\n")
    print("1:Target position\n")
    print("2:Cancel\n")
    print("3:Exit\n")   
    
    value1 = input()
    if(value1=="1"):
        target_client()
    elif(value1=="2"):
        cancel_target() 
    elif(value1=="3"):
        exit()
    else:
        print("wrong input\n")
        rospy.sleep(2)
        interface()


    

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('client_py')
        
        interface()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
