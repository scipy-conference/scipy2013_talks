#!/usr/bin/env python
import roslib; roslib.load_manifest('scipy')
from scipy.preparedearlier import *
import rospy
import std_msgs.msg
import sensor_msgs.msg
import scipy.msg

class Assay:
    def __init__(self, device, cage):
        self.dev = VideoSource(device) if device != -1 else FakeSource()
        self.cage = MouseCage(cage)
        self.img = rospy.Publisher("~image", sensor_msgs.msg.Image)
        self.temp = rospy.Publisher("~temp", std_msgs.msg.Float32)
        self.event = rospy.Publisher("~event", scipy.msg.Event)
        self.sub =  rospy.Subscriber("stimulate", std_msgs.msg.UInt8, self.on_stimulate)
        rospy.Timer(rospy.Duration(0.1),
            lambda evt: self.img.publish(self.dev.get_frame())
        )
        rospy.Timer(rospy.Duration(0.2),
            lambda evt: self.temp.publish(self.cage.get_temperature())
        )

    def on_stimulate(self, msg):
        self.cage.stimulate(msg.data)

    def spin(self):
        while not rospy.is_shutdown():
            if self.cage.get_event():
                self.event.publish(self.cage.last_event)

if __name__ == "__main__":
    rospy.init_node("assay")
    Assay(rospy.get_param('~device', -1),
          rospy.get_param('~cage', 0)).spin()

