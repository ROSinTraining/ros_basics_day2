#!/usr/bin/env python
# import
import rospy
from std_msgs . msg import String

# definitions of variables
# definitions of functions
def callback ( msg ):
    print msg.data
    # definition of publisher / subscriber and services

def main():
    # node initialization
    rospy.init_node("sub")
    rospy.Subscriber('first_topic', String , callback )
    # main program
    # endless loop till shut down
    rospy.spin ()

if __name__ == '__main__':
    main()
