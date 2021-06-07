#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    b = min(msg.ranges)
    print("Distance of the closed object %s" %(b*100))
    #index = msg.ranges.index(b)
    #print(index)
    i=0
    for i in range(0,360):
        if msg.ranges[i] != b:
           i = i+1
        elif msg.ranges[i] == b:
            break
            #print (i*angle_increment)
    angle = i*msg.angle_increment
    print (angle*180/3.14)
            

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
