#!/usr/bin/env python
import urllib
import rospy
from std_msgs.msg import Empty


class PhotoNode:

    def __init__(self):
        rospy.init_node("photo_node", anonymous=True)
        rospy.Subscriber("/photo", Empty, self.callback)

        self.ip = rospy.get_param("endpoint", "http://192.168.31.128:8089/")
        self.count = 0

    def callback(self, data):
        rospy.loginfo("Downloading image...")

        filename = "photo-" + str(self.count) + ".jpg"
        urllib.urlretrieve(self.ip + "photoaf.jpg",  filename)
        self.count += 1

        rospy.loginfo("Finished")

    def spin(self):
        rospy.spin()


if __name__ == "__main__":
    PhotoNode().spin()

