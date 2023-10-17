#!/usr/bin/env python3

# 실행 방법 : > roslaunch ros

import rospy
from rosserial_msgs.msg import ToCooperation as ToCooperation

def talker():
    pub = rospy.Publisher('/kriso/to_cooperation', ToCooperation, queue_size=10)
    rospy.init_node('test_cooperation_publish', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    msg = ToCooperation()

    msg.id = 111
    msg.length = 63
    msg.packet = bytearray(63)

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass