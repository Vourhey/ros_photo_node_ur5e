#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import Empty

def talker():
    pub = rospy.Publisher("/photo", Empty, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.1)
    while not rospy.is_shutdown():
	rospy.loginfo("Sending...")
	pub.publish(Empty())
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
