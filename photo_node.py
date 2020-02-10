#!/usr/bin/env python

import urllib
import roslib
import rospy
from std_msgs.msg import String

def callback():
    urllib.urlretrive("http://192.168.1.100:8080/photoaf.jpg", "photo.jpg")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Photo", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
