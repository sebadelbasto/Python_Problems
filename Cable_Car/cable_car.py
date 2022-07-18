import os.path
import sys
from collections import defaultdict
from os.path import exists

# 1. The program prompts the user to input a file name. If there is no file with that name in the working directory, then the program outputs an error message and exits.
file_name = input('Please enter the name of the file you want to get data from: ')
if not exists(file_name):
    print('Sorry, there is no such file.')
    sys.exit()

#  2. The contents of the file should consist of a strictly increasing sequence of at least two strictly positive integers. Consecutive numbers are separated by at least one space, and there can be extra spaces, including empty lines, anywhere. If that is not the case then the program outputs another error message and exits.
while True:

    try:
        with open(file_name) as file:
            ride = file.read().split()
            if len(ride) < 2:     # at least two items
                raise ValueError 
            if all([item.isdigit() for item in ride]) == False:  #Consecutive numbers are separated by at least one space, and there can be extra spaces, including empty lines, anywhere and not characters etc..
                raise ValueError 
            if all([[i] < [i + 1] for i in range(len(ride)-1)]) == False: #strictly increasing sequence
                raise ValueError
            if (len(ride) == len(set(ride))) == False:
                raise ValueError 
            if all([int(i) > 0 for i in ride]) == False: #are all positive integers?
                raise ValueError
            else: break

    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()

#PerfectRide?
ride = tuple(map(int, ride)) #convert str to int
ride_slopes = ([ride[i + 1] - ride[i] for i in range(len(ride)-1)]) 
if all(i == ride_slopes[0] for i in ride_slopes) == True:
    print('The ride is perfect!')
else:
    print('The ride could be better...')

#Longest good ride
longest = 0
count = 0
current = 0

for i in ride_slopes:
    if i == current:
        count += 1
    else:
        count = 1
        current = i
    longest = max(count, longest)
print(f'The longest good ride has a length of: {longest}')

#How many pillars to remove? Map and Count ALL possible slopes..Longest one indeed will require the less amount of pillars to remove.
mapping_slopes = defaultdict(lambda: 0)
count = 0

for x in range(len(ride)):
    for y in range(x):

        slope = ride[x] - ride[y]
        x_value = mapping_slopes[(x, slope)]
        y_value = mapping_slopes[(y, slope)]
        
        if x_value == False:
            a = 0
        else: a = x_value

        if y_value == False:
            b = 0
        else: b = y_value

        mapping_slopes[(x, slope)] = a + b + 1
        count += b
        
longest_ride = (max(mapping_slopes.values()))
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {(len(ride)-1)-longest_ride}.')











