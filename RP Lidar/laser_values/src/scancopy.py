#! /usr/bin/env python

import rospy
from math import degrees,cos,sin,sqrt,radians
import numpy
from sensor_msgs.msg import LaserScan
import pdb
import pandas as pd
import os

def callback(msg):
    os.system('clear')
    min_dist = min(msg.ranges)
    index = msg.ranges.index(min_dist)
    ranges = msg.ranges
    full_ranges = ranges + ranges[0:index-1]	
    print(len(ranges))
    print(len(full_ranges))
    print(index)

    intensities = msg.intensities
    full_intensities = intensities + intensities[0:index-1]
    print(len(intensities))
    print(len(full_intensities))
    


    print ('______________________________________')
    min_dist = min(full_ranges)
    index = msg.ranges.index(min_dist)
    #print(index)
    full = len(full_ranges)
    for i in range(full):
        if msg.ranges[i] == min_dist:
           break
    #print('index_of_msg_range %s'%i)
    #print ("Angle_of_closest_object %s" %(i*msg.angle_increment*(180/3.14)))
    angle1 = (i*msg.angle_increment)
    #print ('Angle_clockwise %f' %(angle_clockwise))
    #----------------------------print ("Angle_anticlockwise %f" %degrees(i*msg.angle_increment))
    print"Dist_of_closest_object: %f        " %(min_dist*100), "Angle_of_closest_object: %f         " %degrees(i*msg.angle_increment)
    #print degrees(i*msg.angle_increment)
    #print ('_________________________________________________________________')
    
    #mini_value_intensities = min(msg.intensities)
    #for i in range(0,360):
    #   if msg.intensities == mini_value_intensities:
    #    break
    #index_mini_intensities = msg.intensities.index(mini_value_intensities)
    #print (index_mini_intensities)
    #tolerance == 0.02
    #j = min_dist
    #for j in msg.ranges:
    print('___________________________________________________________________')
    full = len(full_ranges)
    for i in range(index,full,1):
        j = i
        #print(msg.ranges[i])
        #print(i)
        #limit = (msg.ranges[i+1] - msg.ranges[i])
        if (full_intensities[i] != 0): 
           if (full_intensities[i+1] == 0):
              if (full_intensities[i+2] != 0): # and full_ranges[i+2] != 'inf'):
                 limit = (full_ranges[i] - full_ranges[i+2])
                 if (abs(limit) >= 0.05):
                    if (i >= 360):
                       i = abs(360-i)
                       edge1_dist = full_ranges[i]
                       angle2 = (i*msg.angle_increment)
                       print(1)
                       break
                    elif (i <= 360):
                         edge1_dist = full_ranges[i]
                         angle2 = (i*msg.angle_increment)
                         print(1)
                         break
              if (full_intensities[i+2] == 0):
                 if (full_intensities[i+3] != 0):
                    limit = (full_ranges[i] - full_ranges[i+3])
                    if (abs(limit) >= 0.04):
                       if (i >= 360):
                          i = abs(360-i)
                          edge1_dist = full_ranges[i]
                          angle2 = (i*msg.angle_increment)
                          print(2)
                          break
                       elif (i <= 360):
                            edge1_dist = full_ranges[i]
                            angle2 = (i*msg.angle_increment)
                            print(2)
                            break
                 if (full_intensities[i+3] == 0):
                    if (i >= 360):
                       i = abs(360-i)
                       edge1_dist = full_ranges[i]
                       angle2 = (i*msg.angle_increment)
                       print(3)
                       break
                    elif (i <= 360):
                         edge1_dist = full_ranges[i]
                         angle2 = (i*msg.angle_increment)
                         print(3)
                         break
                 elif (abs(limit) >= 0.04):
                      if (i >= 360):
                         i = abs(360-i)
                         edge1_dist = full_ranges[i]
                         angle2 = (i*msg.angle_increment)
                         print(4)
                         break
                      elif (i <= 360):
                           edge1_dist = full_ranges[i]
                           angle2 = (i*msg.angle_increment)
                           print(4)
                           break
           elif (full_intensities[i+1] != 0 and full_intensities[i+2] != 0):
                limit = (full_ranges[i+2] - full_ranges[i+1])
                if (abs(limit) >= 0.03):
                   if (i >= 360):
                      i = abs(360-i)
                      edge1_dist = full_ranges[i+1]
                      angle2 = ((i+1)*msg.angle_increment)
                      print('el')
                      break
                   elif (i <= 360):
                        edge1_dist = full_ranges[i+1]
                        angle2 = ((i+1)*msg.angle_increment)
                        print('el')
                        break
        elif (full_intensities[i] == 0):
             continue
    #############################################################################################

    j = index
    for j in range(index,-full,-1):
        #limit = (full_ranges[j] - full_ranges[j-1])
        if (full_intensities[j] != 0):
           if (full_intensities[j-1] == 0):
              if (full_intensities[j-2] != 0): #and full_intensities[j-2] != 0):
                 limit = (full_ranges[j] - full_ranges[j-2])
                 if (abs(limit) >= 0.04):
                    if (j >= 360):
                       j = abs(360-j)
                       edge2_dist = full_ranges[j]
                       angle3 = (j*msg.angle_increment)
                       print(-1)
                       break
                    elif (j <= 360):
                         edge2_dist = full_ranges[j]
                         angle3 = (j*msg.angle_increment)
                         print(-1)
                         break
              if (full_intensities[j-2] == 0):
                 if (full_intensities[j-3] != 0):
                    limit = (full_ranges[j] - full_ranges[j-3])
                    if (abs(limit) >= 0.05):
                       if (j >= 360):
                          j = abs(360-j)
                          edge2_dist = full_ranges[j]
                          angle3 = (j*msg.angle_increment)
                          print(-2)
                          break
                       elif (j <= 360):
                            edge2_dist = full_ranges[j]
                            angle3 = (j*msg.angle_increment)
                            print(-2)
                            break
                 if (full_intensities[j-3] == 0): # and full_intensities[j-4] == 0):
                    if (j >= 360):
                       j = abs(360-j)
                       edge2_dist = full_ranges[j]
                       angle3 = (j*msg.angle_increment)
                       print(-3)
                       break
                    elif (j <= 360):
                         edge2_dist = full_ranges[j]
                         angle3 = (j*msg.angle_increment)
                         print(-3)
                         break
                 elif (abs(limit) >= 0.05):
                      if (j >= 360):
                         j = abs(360-j)
                         edge2_dist = full_ranges[j]
                         angle3 = (j*msg.angle_increment)
                         print(-4)
                         break
                      elif (j <= 360):
                           edge2_dist = full_ranges[j]
                           angle3 = (j*msg.angle_increment)
                           print(-4)
                           break
           elif (full_intensities[j-1] != 0 and full_intensities[j-2] != 0):
                limit = (full_ranges[j-2] - full_ranges[j-1])
                if (abs(limit) >= 0.03):
                   if (j >= 360):
                      j = abs(360-j)
                      edge2_dist = full_ranges[j-1]
                      angle3 = ((j-1)*msg.angle_increment)
                      print('-el')
                      break
                   elif (j <= 360):
                        edge2_dist = full_ranges[j-1]
                        angle3 = ((j-1)*msg.angle_increment)
                        print('-el')
                        break
        elif (full_intensities[j] == 0):
             continue

    print'edge2_dist: %f          ' %(edge2_dist*100), 'edge1_dist: %f          ' %(edge1_dist*100)
    print'Angle_of_edge2: %f    ' %degrees(j*msg.angle_increment), 'Angle_of_edge1: %f    ' %degrees(i*msg.angle_increment)
    


    #x0 = abs((abs((min_dist*100))) * (sin((angle1))))
    #y0 = abs((abs((min_dist*100))) * (cos((angle1))))
    #x1 = abs((abs((edge1_dist*100))) * (sin((angle2))))
    #y1 = abs((abs((edge1_dist*100))) * (cos((angle2))))
    x21 = abs(abs(edge2_dist*100) * sin((angle3)))
    y21 = abs(abs(edge2_dist*100) * cos((angle3)))
    #print(x0)
    #print(y0)
    #print(x1)
    #print(y1)

    a0 = (sin((angle1))) 
    b0 = (cos((angle1)))
    c0 = abs((min_dist*100))

    a1 = (sin((angle2)))
    b1 = (cos((angle2)))
    c1 = abs((edge1_dist*100))

    d1 = (sin((angle3)))
    d2 = (cos((angle3)))
    c2 = abs((edge2_dist*100))

    x0 = ((c0 * a0))
    y0 = ((c0 * b0))

    x1 = ((c1 * a1))
    y1 = ((c1 * b1))

    x2 = ((c2 * d1))
    y2 = ((c2 * d2))

    s1 = numpy.array((x0,y0))
    s2 = numpy.array((x1,y1))
    s3 = numpy.array((x2,y2))
    #print(s1)
    #print(s2)
    #print(s2)
    side1 = numpy.linalg.norm(s2 - s1)
    dist1 = ((sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)))
    dist2 = ((sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2)))
    dist3 = ((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))
    side2 = numpy.linalg.norm(s3 - s1)
    #print(side1)
    #print(dist1)
    #print(dist2)
    #print(dist3)
    #print(side2)
    flag = 0
    '''if (dist3 < 14.5 and (abs(degrees(angle1 - angle2))) <= 6):
       if (dist1 + dist2 >= dist3):
          print'I shape dectected                   ', 'lenght of a side is %f      '%max(dist1,dist2)
          flag = 1
       elif (flag != 1):
            print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
            flag = 1
    if (flag != 1 and dist3 < 14.5 and (abs(degrees(angle1 - angle3))) <= 6):
       if (dist1 + dist2 >= dist3):
          print'I shape dectected                   ', 'lenght of a side is %f      '%max(dist1,dist2)
          flag = 1
       elif (flag != 1):
            print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
            flag = 1'''
    if (flag != 1 and abs((dist1 + dist2) - dist3) <= 2 and (abs(degrees(angle1 - angle2))) <= 6):
       if (dist1 + dist2 >= dist3):
          print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
          flag = 1
       elif (flag != 1):
            print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
            flag = 1
    if (flag != 1 and abs((dist1 + dist2) - dist3) <= 2 and (abs(degrees(angle1 - angle3))) <= 6):
       if (dist1 + dist2 >= dist3):
          print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
          flag = 1
       elif (flag != 1):
            print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
            flag = 1

    if (flag != 1 and abs((dist1 + dist2) - dist3) <= 2):
       #if (dist1 + dist2 >= dist3):
       #   print'I shape dectected                   ', 'lenght of a side is %f      '%max(dist1,dist2)
       #   flag = 1
       if (flag != 1):
          print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
          flag = 1

    #if (abs((dist1 + dist2) - dist3) <= 2 and (abs(degrees(angle1 - angle2))) <= 5):
    #   print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
    #   flag = 1
    #   #print(1)
    #if (flag != 1 and abs((dist1 + dist2) - dist3) <= 2 and (abs(degrees(angle1 - angle3))) <= 5):
    #   print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
    #   flag = 1
    #   #print(2)
    #if (flag != 1 and abs(dist1 - dist2) >= 2):
    #   print'I shape dectected                   ', 'lenght of a side is %f      '%(dist1+dist2)
    #   flag = 1
    #   print(3)
       
    elif (flag != 1):
         #print'edge2_dist: %f          ' %(edge2_dist*100), 'edge1_dist: %f          ' %(edge1_dist*100)
         #print'Angle_of_edge2: %f    ' %degrees(j*msg.angle_increment), 'Angle_of_edge1: %f    ' %degrees(i*msg.angle_increment)
          print'lenght of a side1 is %f      '%dist1, 'lenght of a side2 is %f      '%dist2
    print(i)
    print(j)
    
    temp_ranges = [0] * full
    for a in range(full):
        temp_ranges[a] = full_ranges[a]
    
    for b in range(j,i,1):
        temp_ranges[b] = float("inf")

    full_ranges = 0
    full_ranges = temp_ranges
    for c in range(361,full):
        full_ranges[c] = float("inf")


    print(full_ranges[j:i])
    #print(full_ranges)

    min_dist = min(full_ranges)
    print(min_dist)
    index = full_ranges.index(min_dist)
    ranges = full_ranges
    full_ranges = ranges + ranges[0:index-1]
    print(index)
    #print(full_ranges)

    #full_ranges[j:i] = float("inf")


    #for a in range(j,i,1):
    #    full_intensities[a] = 0
    #    print(a)
    #    break
        

    print ('_________________________________________________________________')

    #ranges = 0                   
    #full_ranges = 0


rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
