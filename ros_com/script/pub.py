#!/usr/bin/env python
# import
import rospy
from std_msgs.msg import String

def main():
    # node initialization
    rospy.init_node (" pub ")
    # definitions of variables
    msg_string = String ()
    # definitions of functions
    # definition of publisher / subscriber and service
    pub = rospy.Publisher ('first_topic', String , queue_size =1)
    # main program
    r = rospy.Rate (5) #5 Hz
    # endless loop till shut down #
    while not rospy.is_shutdown():
        # assign value to ROS message and publish it
        msg_string.data = " Welcome to ROS !"
        pub.publish( msg_string )
        r.sleep()

if __name__ == '__main__':
    main()
