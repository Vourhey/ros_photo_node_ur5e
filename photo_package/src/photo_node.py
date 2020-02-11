#!/usr/bin/env python
import urllib
import rospy
import os
from std_msgs.msg import Empty
from datetime import datetime


class PhotoNode:

    def __init__(self):
        rospy.init_node("photo_node", anonymous=True)
        rospy.Subscriber("/photo", Empty, self.callback)

        self.ip = rospy.get_param("endpoint", "http://192.168.1.100:8080/")
        self.count = 0
	self.now = datetime.now()

    def callback(self, data):
	current_date = self.now.strftime("%Y-%m-%d-%H-%M-%S")

        rospy.loginfo("Downloading image...")

        filename = "photo-" + str(self.count) + "--"+ current_date + ".jpg"
	directory_view_count = "result_view/photo_view_" + str(self.count % 3)
	
	full_filename = os.path.join(directory_view_count, filename)
        urllib.urlretrieve(self.ip + "photoaf.jpg",  full_filename)
        self.count += 1

        rospy.loginfo("Finished")

    def spin(self):
        rospy.spin()


if __name__ == "__main__":
    PhotoNode().spin()
