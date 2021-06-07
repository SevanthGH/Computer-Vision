#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    #print min(msg.ranges)
    b = min(msg.ranges)
    print("Distance of the closed object %s" %(b*100))
    #index = msg.ranges.index(b)
    #print(index)
    index=0				
    for i in msg.ranges:
        if i != b:
           index = index+1
        elif i==b:
            break 
    angle = index*msg.angle_increment
    print (angle)
rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
