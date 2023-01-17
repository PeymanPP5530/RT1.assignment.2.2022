#! /usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from assignment_2_2022.msg import odom_custom_msg



def callback(data):

    pub = rospy.Publisher('chatter', odom_custom_msg, queue_size=50)
    #print(data)
    msg=odom_custom_msg()

    msg.x = data.pose.pose.position.x
    msg.y = data.pose.pose.position.y
    msg.vel_x = data.twist.twist.linear.x
    msg.vel_y = data.twist.twist.linear.y


    print(msg)
    pub.publish(msg)

   # rospy.sleep(1)   
    
def listener():
    

    rospy.init_node('NodeB')

    rospy.Subscriber("/odom", Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    