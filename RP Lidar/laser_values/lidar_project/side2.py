    for j in range(index,-50,-1):
        limit = (full_ranges[j] - full_ranges[j-1])
        if (full_intensities[j] != 0):
           if (full_intensities[j-1] == 0):
              if (full_intensities[j-2] != 0): #and full_intensities[j-2] != 0):
                 limit = (full_ranges[j] - full_ranges[j-2])
                 if (abs(limit) >= 0.03):
                    edge2_dist = full_ranges[j]
                    angle3 = degrees(j*msg.angle_increment)
                   # print('edge2_dist: %f'%(edge2_dist*100))
                   # print('Angle_of_edge2: %f' %degrees(j*msg.angle_increment))
                    print(-1)
                   # print(j)
                    break
              if (full_intensities[j-2] == 0):
                 if (full_intensities[j-3] != 0):
                    limit = (full_ranges[j] - full_ranges[j-3])
                    if (abs(limit) >= 0.03):
                       edge2_dist = full_ranges[j]
                       angle3 = degrees(j*msg.angle_increment)
                    #   print('edge2_dist: %f'%(edge2_dist*100))
                    #   print('Angle_of_edge2: %f' %degrees(j*msg.angle_increment))
                       print(-2)
                    #   print(j)
                       break
                 if (full_intensities[j-3] == 0): # and full_intensities[j-4] == 0):
                    edge2_dist = full_ranges[j]
                    angle3 = degrees(j*msg.angle_increment)
                  #  print('edge2_dist: %f'%(edge2_dist*100))
                  #  print('Angle_of_edge2: %f' %degrees(j*msg.angle_increment))
                    print(-3)
                  #  print(i)
                    break
                 elif (abs(limit) >= 0.04):
                      edge2_dist = full_ranges[j]
                      angle3 = degrees(j*msg.angle_increment)
                     # print('edge2_dist: %f'%(edge1_dist*100))
                     # print('Angle_of_edge2: %f' %degrees(j*msg.angle_increment))
                      print(-4)
                     # print(j)
                      break
           elif (full_intensities[j-1] != 0 and full_intensities[j-2] != 0):
                limit = (full_ranges[j-2] - full_ranges[j-1])
                if (abs(limit) >= 0.03):
                    edge2_dist = full_ranges[j-1]
                    angle3 = ((j-1)*msg.angle_increment)
                    print('-el')
                    break
        elif (full_intensities[j] == 0):
             continue

