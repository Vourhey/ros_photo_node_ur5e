#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("Photo", String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        str = "hellow world %s" % rospy.get_time()
	rospy.loginfo(str)
	pub.publish(str)
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
