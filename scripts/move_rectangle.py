#!/usr/bin/env python3

import rospy
from time import sleep as s
from geometry_msgs.msg import Twist

def move_turtle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_node', anonymous=True)
    
    # Create a publisher to send velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Define the rate at which the loop will run (10 Hz)
    rate = rospy.Rate(10)
    
    # Create a Twist message to set linear and angular velocity
    vel_msg = Twist()

    rospy.loginfo("Moving the turtle in a rectangle...")

    def rect_height():
        vel_msg.linear.x = 5.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        velocity_publisher.publish(vel_msg)
        s(1)

        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 2.0
        vel_msg.linear.z = 0.0
        velocity_publisher.publish(vel_msg)
        s(1)

        vel_msg.linear.x = -5.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        velocity_publisher.publish(vel_msg)
        s(1)

    def rect_width():
        vel_msg.linear.x = 0.0
        vel_msg.linear.y = -2.0
        vel_msg.linear.z = 0.0
        velocity_publisher.publish(vel_msg)
        s(1)

        vel_msg.linear.x = 5.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        velocity_publisher.publish(vel_msg)
        s(1)


    while not rospy.is_shutdown():
        rect_height()
        rect_width()
        rospy.loginfo("Completed the Path!")
        rate.sleep()
        break


if __name__ == '__main__':
    try:
        # Call the function to move the turtle
        move_turtle()
    except rospy.ROSInterruptException:
        pass