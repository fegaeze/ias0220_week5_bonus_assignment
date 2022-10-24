#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class LocomotionNode():

    def __init__(self):

        self.twist = Twist()
        self.can_move = True

        self.twist.linear.x = 0.
        self.twist.linear.y = 0.
        self.twist.linear.z = 0.

        self.twist.angular.x = 0.
        self.twist.angular.y = 0.
        self.twist.angular.z = 0.

        self.rate = rospy.Rate(25)
        self.robot_velocities = rospy.Publisher("/ddrobot/robot_velocity_controller/cmd_vel", Twist, queue_size=10)   

    def robot_path(self):
        self.twist.linear.x = 3.6
        self.twist.angular.z = 0.3
        self.robot_velocities.publish(self.twist)
        pass


    def run(self):
        while not rospy.is_shutdown():
            self.robot_path()
            self.rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node('ddrobot_locomotion')
        locomotion_node = LocomotionNode()
        locomotion_node.run()
    except rospy.ROSInterruptException:
        pass
