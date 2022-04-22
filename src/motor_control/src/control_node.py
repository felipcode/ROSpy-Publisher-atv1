#!/usr/bin/en python3

import rospy
from std_msgs.msg import Int32

def control_node():
    rospy.init_node('control_node', anonymous=False)
    pub = rospy.Publisher('control/pwm', Int32, queue_size = 10)
    rate = rospy.Rate(10) # Hz
    pwm = Int32()
    pwm.data = 0

    while not rospy.is_shutdown():
        sensor_msg = "value %s" % pwm.data
        rospy.loginfo(sensor_msg)
        pub.publish(pwm)
        rate.sleep()
        pwm.data = pwm.data + 1
        if pwm.data > 255:
            pwm.data = 0
    return 0
    
if __name__ == '__main__':
    try:
        control_node()
    except rospy.ROSInterruptExeption:
        pass

