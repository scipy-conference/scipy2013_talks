import roslib; roslib.load_manifest('scipy')
import cv2
import numpy as np
import random
import time

import rospy
import ros_flydra.cv2_bridge
import scipy.msg

class VideoSource:
    def __init__(self, device):
        pass

class FakeSource:
    def __init__(self, w=640, h=480, color=True):
        self._nchan = 3 if color else 1
        self._w = w
        self._h = h
        self._id = 0

    def get_frame(self):
        now = rospy.Time.now()

        im = np.zeros((self._h, self._w, self._nchan), dtype=np.uint8)
        im.fill(255)

        color = (255, 0, 0) if self._nchan == 3 else (0, 0, 0)

        cv2.putText(im,
                "%.2f" % now.to_sec(),
                (5, 70), cv2.FONT_HERSHEY_PLAIN, 2.0, color, 2
        )

        cv2.putText(im,
                "%d" % self._id,
                (5, 150), cv2.FONT_HERSHEY_PLAIN, 2.0, color, 2
        )

        self._id += 1

        return ros_flydra.cv2_bridge.numpy_to_imgmsg(im, stamp=now)
        
class VideoSource:
    def __init__(self, device):
        self._cam = cv2.VideoCapture(0)
        w = 0
        while not w:
            self._cam.read()
            w = int(self._cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
            h = int(self._cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

        self._w = w
        self._h = h

    def get_frame(self):
        now = rospy.Time.now()
        ok,im = self._cam.read()

        if not ok:
            im = np.random.random_integers(0,255,(self._h, self._w, 3)).astype(np.uint8)

        return ros_flydra.cv2_bridge.numpy_to_imgmsg(im, stamp=now)

class MouseCage:
    def __init__(self, n):
        self._base = random.randrange(15,18)
        self._thresh = 0.98

    def get_temperature(self):
        return self._base + random.random()

    def stimulate(self, val):
        self._thresh = (255.0-val)/255.0

    @property
    def last_event(self):
        msg = scipy.msg.Event()
        msg.reward = self._reward
        msg.header.stamp = rospy.Time.now()
        return msg

    def get_event(self):
        time.sleep(0.05)
        if random.random() > self._thresh:
            self._reward = random.choice(
                            (scipy.msg.Event.REWARD_GREEN,scipy.msg.Event.REWARD_RED))
            return True
        return False



