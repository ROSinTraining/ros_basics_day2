#!/usr/bin/env python
import rospy

def main():
    rospy.init_node("myfirstnode")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # ADD YOUR CODE HERE 
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        rate.sleep ()


if __name__ == '__main__':
    main()