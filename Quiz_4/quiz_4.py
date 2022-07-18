# Written by *** for COMP9021

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

#We display a rectangle of minimal size that contains all points that are eventually switched on.


import sys
import time
start_time = time.time()

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

def lights(nb_of_leading_zeroes, code):
    
    number = '0' * nb_of_leading_zeroes + f'{int(code):o}'
    number_list = [int(a) for a in reversed(str(number))]
    coordinates = {0: (0,1), 1:(1,1), 2: (1,0), 3: (1,-1), 4: (0,-1), 5: (-1,-1), 6: (-1,0), 7: (-1,1)}
    lights_on = [(0,0)]
    last_visited = [(0,0)]

    for x in number_list:
        if x in coordinates:
            x = coordinates[x]
            y = tuple(map(sum, zip(last_visited[-1],x)))
            last_visited.append(y)
            if y not in lights_on:
                lights_on.append((y))
            else: lights_on.remove((y))
    lights_on = sorted(lights_on)

    if bool(lights_on) == False:
        None
    else: build_rectangle(lights_on, on, off)
        
def build_rectangle(lights_on, on, off):

    max_width = max(lights_on,key=lambda item:item[0]) # max x value
    max_height = max(lights_on,key=lambda item:item[1]) # max y value
    min_width = min(lights_on,key=lambda item:item[0])  # min x value
    min_height = min(lights_on,key=lambda item:item[1])  # min y value

    max_vertex = (max_width[0], max_height[1])
    min_vertex = (min_width[0], min_height[1])

    all_vertex = [(x,y) for x in range(min(min_vertex), max(max_vertex)+1) for y in range(min(min_vertex), max(max_vertex)+1)]
    lights_on_off_rectangle = []
    for x in all_vertex: 
        if x >= min_vertex and x <= max_vertex:
            lights_on_off_rectangle.append(x)
    rectangle_vertex_sorted = (sorted(lights_on_off_rectangle, key=lambda x: x[1]))
    
    height = list(reversed([x for x in range(min_height[1], max_height[1]+1)]))

    for y in height:
        for x in rectangle_vertex_sorted:
            if x[1] == y:
                print(on
                if x in lights_on
                else off, end=''
                )
        print()

lights(nb_of_leading_zeroes, code)
print("--- %s seconds ---" % (time.time() - start_time))
