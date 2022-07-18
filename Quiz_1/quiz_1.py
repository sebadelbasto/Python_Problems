# Written by Sebastian del Basto for COMP9021
#
# Prompts the user for two strictly positive integers,
# then used to draw a 'picture'.
#
# Also prompts the user for the name of a file, assumed to be
# stored in the working directory, to then read its contents
# and output derived sentences.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
# person_name, profession:year_of_birth--year_of_death
# with no space anywhere except after the comma and between
# the various parts of person_name; in particular, there is
# no space before person_name and no space after year_of_death.
# year_of_birth and year_of_death are strictly positive integers
# (so DC years), the difference between both being at least 2.

import sys
from os.path import exists

try:
    plus_number, dash_number =\
            (int(x) for x in input('Enter two strictly positive integers '
                                   'for the picture dimensions: '
                                  ).split()
            )
    if plus_number <= 0 or dash_number <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
file_name = input('Input the name of a file in the working directory: ')
if not exists(file_name):
    print('Incorrect input, giving up.')
    sys.exit()

print("First, here is some kind of 'picture':")
print()
def image():

        def display_mixtape():
            print('*','*'.join('+' * ((plus_number))),'*', '-' *(dash_number) ,'*', '*'.join('+' * ((plus_number))),'*', sep='')
        display_mixtape()

        def display_empty_tape():
            print('*',' '.join(' ' * ((plus_number))),' ', ' ' *(dash_number) ,' ', ' '.join(' ' * ((plus_number))),'*', sep='')
        display_empty_tape()

        def display_middle_tape():
            print('*',' '.join(' ' * ((plus_number))),' ', '*' *(dash_number) ,' ', ' '.join(' ' * ((plus_number))),'*', sep='')
        display_middle_tape()

        display_empty_tape()
        display_mixtape()
image()

print()
print("And now comes some information about some people:")

def processing_people_file():
    
    with open(file_name) as file:

        a = file.read().replace(":", "," ).replace("--", "," ).replace(", ",",").strip().replace("  ","") #clean

        b = filter(str.strip, a.splitlines()) #remove empty spaces left
            
        for i in list(b): 
            c = i.split(',') #convert into individual lists
            for x in list(c):
                name = c[0]
                proffesion = c[1]
                age = [int(z) for z in c if type(z) == int or z.isdigit()] # could not substract indexes [2] and [3] values of list(c) due to string types...created a new list(age) with only integers, process learnt from  'https://www.geeksforgeeks.org/sum-of-list-with-string-types-in-python/'
                if x == name: # I was iterating over the list and printing 4 times each person. Used debugger and thought in putting 'if x==name:' which allowed me to skip iteration over others indexes.
                    print(f'* The {proffesion} "{name}" lived for {age[1]-age[0]} many years.')
processing_people_file()
