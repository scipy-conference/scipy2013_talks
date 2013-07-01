#!/usr/bin/env python
import roslib; roslib.load_manifest('scipy')
from scipy.preparedearlier import *
import rospy
import std_msgs.msg

class Experiment:
    def __init__(self, rate, onval, offval):
        self.rate = rospy.Rate(rate)
        self.pub =  rospy.Publisher("stimulate", std_msgs.msg.UInt8)
        self.val = [onval, offval]

    def spin(self):
        i = 0
        while not rospy.is_shutdown():
            self.pub.publish( self.val[i] )
            i ^= 1
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node("experiment")
    Experiment(rospy.get_param('~rate', 0.5),
               rospy.get_param('~onval', 200),
               rospy.get_param('~offval', 10)).spin()

