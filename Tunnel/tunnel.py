import os.path
import sys
from collections import deque

file_name = input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(file_name):
    print('Sorry, there is no such file.')
    sys.exit()

with open(file_name) as file:
    tunnel_beta = file.read().splitlines()
    tunnel_beta_2 = [x.split() for x in tunnel_beta]
    tunnel = [x for x in tunnel_beta_2 if x]
    tunnel_3 = [y.lstrip("-") for x in tunnel for y in x]


    #i-th number of the first sequence should be strictly greater than the i-th number of the second sequence
    ith_condition_false = 0
    for line in tunnel:
        for x in range(len(line)):
            if (len(tunnel[0]) == len(tunnel[1])) == False:  #avoid index out of range error
                break
            if int(tunnel[0][x]) <= int(tunnel[1][x]):
                ith_condition_false += 1
                break
            else: continue
        break

  
while True:
    try:

        if len(tunnel) < 2:     # at least two lines
            raise ValueError
        if all([len(line) > 1 for line in tunnel]) == False:     # at least two numbers in each line
            raise ValueError
        if all([elem.isdigit() for line in tunnel_3 for elem in line]) == False: #All are digits ...tunnel_3 to eliminate (-)
            raise ValueError
        if (len(tunnel[0]) == len(tunnel[1])) == False: #same amount of elements in each line
            raise ValueError
        if ith_condition_false == 1: # same number of at least two (positive or negative) integers. 
            raise ValueError
        else: break

    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()

# Improve tunnel
tunnel_2 = []
for x in tunnel: 
    x = tuple(map(int, x)) #convert str to int
    tunnel_2.append(x)

roof, floor = tunnel_2
roof_floor = tuple(zip(roof, floor))

# Map positions 
positions = {}
for x in range(len(roof_floor)):
    positions[x] = roof_floor[x]



#problem 1

for x in positions:
    count = 0
    current_path = []
    
    for y in positions:
        range_x = list(range(positions[x][1],positions[x][0]))
        range_y = list(range(positions[y][1],positions[y][0]))

        if x > y: 
            None
        else:
            if bool(current_path) == True:
                current_path[0] = set(current_path[0]).intersection(range_y)
                if set(current_path[0]).isdisjoint(range_y) == False:
                    count += 1
                    if y == len(positions)-1:
                        print(f'From the west, one can into the tunnel over a distance of {count}')
                    else: None
                else:
                    print(f'From the west, one can into the tunnel over a distance of {count}')
                    break

            #First entrance to tunnel    
            else:
                window = set(range_x).intersection(range_y)
                if bool(window) == True:
                    current_path.append(window)

                    if window.isdisjoint(range_y) == False:
                        count += 1
                        if y == len(positions)-1:
                            print(f'From the west, one can into the tunnel over a distance of {count}')
                        else: None
                    else:
                        print(f'From the west, one can into the tunnel over a distance of {count}')
                        break
                else: break
    break #break at first x iteration..its entry!

#problem 2 inside the tunnel
views_inside_tunnel = set()

for x in positions:
    count = 0
    current_path = []
    
    for y in positions:
        range_x = list(range(positions[x][1],positions[x][0]))
        range_y = list(range(positions[y][1],positions[y][0]))

        if x > y: 
            None
        else:
            if bool(current_path) == True:
                current_path[0] = set(current_path[0]).intersection(range_y)
                if set(current_path[0]).isdisjoint(range_y) == False:
                    count += 1
                    if y == len(positions)-1:
                        views_inside_tunnel.add(count)
                    else: None
                else:
                    views_inside_tunnel.add(count)
                    break

            #First entrance to tunnel    
            else:
                window = set(range_x).intersection(range_y)
                if bool(window) == True:
                    current_path.append(window)

                    if window.isdisjoint(range_y) == False:
                        count += 1
                        if y == len(positions)-1:
                            views_inside_tunnel.add(count)
                        else: None
                    else:
                        views_inside_tunnel.add(count)
                        break
                else: break
print(f'Inside the tunnel, one can into the tunnel over a maximum distance of {max(views_inside_tunnel)}')



