import sys
import copy
from operator import concat

#1 
while True:
    try: 
        number = list(map(int, input("Please input the heroes' powers: ").split()))
        break
    except ValueError:
        print('Sorry, these are not valid power values.')
        sys.exit()

#2
while True:
    try: 
        nb_of_swiches = int(input("Please input the number of power flips: "))
        if nb_of_swiches < 0:
            raise ValueError
        if nb_of_swiches > len(number):
            raise ValueError
        else: break
    except ValueError:
        print('Sorry, this is not a valid number of power flips.')
        sys.exit()


# Problem 1 and 2
def FP_1_2():

    numbers = sorted(number)
    final_sum = []
    negative_values = sorted(x for x in number if x < 0)

    for x in negative_values:
        if len(final_sum) < nb_of_swiches:
            if x in numbers:
                numbers.remove(x)
            x *= -1
            final_sum.append(x)   #que pasa si el valor es negativo.... que pasa si el unicco valor negativo es menor que el otro y podira meterle con tdo ???

    switch_count = len(final_sum)
    final_sum = sorted(concat(final_sum, numbers))

    def same_hero_many_times():
        
        #prevent changing global variable values
        switch_count_1 = copy.deepcopy(switch_count)
        final_sum_1 = copy.deepcopy(final_sum)

        if  switch_count_1 >= nb_of_swiches:
            return(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum(final_sum_1)}.')
        else:
            while  switch_count_1 < nb_of_swiches:
                final_sum_1[0] *= -1
                switch_count_1 += 1
                if  switch_count_1 == nb_of_swiches:
                    return(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum(final_sum_1)}.')

    def same_hero_once():
        
        #prevent changing global variable values
        switch_count_2 = copy.deepcopy(switch_count)
        final_sum_2 = copy.deepcopy(final_sum)
        numbers_2 = copy.deepcopy(numbers)  

        if switch_count_2 >= nb_of_swiches:
            return(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum(final_sum_2)}.')
        else:
            while switch_count_2 < nb_of_swiches:
                min_number = min(numbers_2)
                final_sum_2.remove(min_number)
                for x in numbers_2:
                    if x == min_number:
                        numbers_2.remove(x)
                min_number *= -1
                final_sum_2.append(min_number)
                switch_count_2 += 1

                if switch_count_2 == nb_of_swiches:
                    return(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum(final_sum_2)}.')

    print(same_hero_many_times())
    print(same_hero_once())

# Problem 3: 
def consecutive_heroes_n_nb_of_swiches():

    #Exceptional cases for None and 0 flips
    if len(number): zero = number
    else: zero = [0]
    if nb_of_swiches == 0:
        print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {zero[0]}.')
        return

    else:
        indexing_number = [x for x in range(len(number))]
        possible_index_sums = []
        nb_of_swiches_3 = copy.deepcopy(nb_of_swiches)

        for i in indexing_number:
            if nb_of_swiches_3 <= len(number):
                combination = tuple(x for x in range(i, nb_of_swiches_3))
                possible_index_sums.append(combination)
                nb_of_swiches_3 += 1

        possible_value_sums = []
        for i in possible_index_sums:
            values = []
            for p in i:
                z = number[p] * -1
                values.append(z)
            possible_value_sums.append(tuple(values))

        max_value = (max(possible_value_sums, key=lambda item:sum(item)))
        mapping_to_index = dict(zip(possible_value_sums, possible_index_sums))

        list_max_indexes = list(mapping_to_index.get(max_value))
        list_max_value = list(max_value)
        number_3 = copy.deepcopy(number)
        del number_3[list_max_indexes[0]:list_max_indexes[-1]+1]
        max_sequence = list_max_value + number_3
        print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum(max_sequence)}.')


# Problem 4:
def max_consecutive_heroes():

    #Exceptional cases for None and 0 flips
    if len(number): zero = number
    else: zero = [0]
    if nb_of_swiches == 0:
        print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {zero[0]}.')
        return

    else:
        indexing_number = [x for x in range(len(number))]
        possible_index_sums = []
        possible_nb_of_swiches = tuple(range(len(number)))
        maxsum = []

        for n in possible_nb_of_swiches: 

            if n == 0:
                maxsum.append(sum(number)) 

            else:
                for i in indexing_number:
                    if n <= len(number):
                        combination = tuple(x for x in range(i, n))
                        possible_index_sums.append(combination)
                        n += 1

                possible_value_sums = []
                for i in possible_index_sums:
                    values = []
                    for p in i:
                        z = number[p] * -1
                        values.append(z)
                    possible_value_sums.append(tuple(values))

                max_value = (max(possible_value_sums, key=lambda item:sum(item)))
                mapping_to_index = dict(zip(possible_value_sums, possible_index_sums))

                list_max_indexes = list(mapping_to_index.get(max_value))
                list_max_value = list(max_value)
                number_4 = copy.deepcopy(number)
                del number_4[list_max_indexes[0]:list_max_indexes[-1]+1]
                max_sequence = list_max_value + number_4
                maxsum.append(sum(max_sequence))

        print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {max(maxsum)}.')


FP_1_2()
consecutive_heroes_n_nb_of_swiches()
max_consecutive_heroes()


# Personal notes:
# For explanations and pseudocode go to "Question1.ipynb" on /Users/Programming/Desktop/COMP9021/ASSIGNMENT/Question_1/Question1.ipynb