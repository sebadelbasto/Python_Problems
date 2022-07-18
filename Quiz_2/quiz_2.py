# Written by *** for COMP9021
#
# Besides a function to generate a random dictionary,
# defines two functions that analyse a dictionary.
# See the pdf for explanations via an illustration
# and examples of possible uses.
#
# You can assume that both functions are called with proper
# arguments (namely, a dictionary whose keys are all integers
# between 1 and n for some strictly positive integer n
# and whose values are numbers between 1 and n,
# and an integer between 1 and n).
#
# The lines that are output by the
# function longest_strictly_decreasing_sequences_to()
# are ordered from smallest first value to largest first value.


from random import seed, randint

def generate_mapping(for_seed, length):
    seed(for_seed)
    return {i: randint(1, length) for i in range(1, length + 1)}

def follow_the_arrows_from(mapping, n):

    values_list = []
    values_list.append(n)

    for n in values_list:
        if mapping.get(n) in values_list:
            n = (mapping.get(n))
            break
        else: values_list.append(mapping.get(n))
        n = (mapping.get(n))

    indices = list(range(len(values_list)))
    value_positions = {values_list[i]: indices[i] for i in range(len(values_list))}
    start_loop = value_positions.get(n)

    if start_loop > 0:
        print(f'It starts with a stalk of length {start_loop}')
        print((f'It reaches {n} on a loop of length {len(values_list[start_loop:])}'))

    else: print((f'It is on a loop of length {len(values_list[start_loop:])}'))

def longest_strictly_decreasing_sequences_to(mapping, n):

    if n not in mapping.values():
        return
    # Hint: create a dictionary, D, whose keys are the
    # numbers i in the interval [n + 1, len(mapping)]
    # such that there is a path from i to n, with as
    # corresponding value the length of this path.
    # max(D.values()) evaluates to the largest length
    # of those paths; let M denote that value.
    # For each number i in the interval [n + 1, len(mapping)],
    # if i is a key of D and M is the associated value, then
    # output i, mapping[i], mapping[mapping[i]], ..., n,
    # separating consecutive values with ->.
    descending_lists = []
    re_duplicates_descending_lists = []

    for x in mapping:
    
        v_list = []
        ds = []
        v_list.append(x)

        for x in v_list:
            if mapping.get(x) in v_list:
                v_list.append(mapping.get(x))
                for i in range(0,len(v_list)-1):
                    if v_list[i] > v_list[i+1]:
                        if (v_list[i]) not in ds:
                            ds.append(v_list[i])
                        if (v_list[i+1]) not in ds:
                            ds.append(v_list[i+1])
                    else: None
                break
            else: v_list.append(mapping.get(x))
            x = (mapping.get(x))
    
        if n in ds:
            limit = ds.index(n) + 1
            descending_list = (ds[:limit])
            if descending_list == sorted(descending_list,reverse=True):
                descending_lists.append(descending_list)
        
            for elem in descending_lists:
                if elem not in re_duplicates_descending_lists:
                    re_duplicates_descending_lists.append(elem)
    descending_lists = re_duplicates_descending_lists

    for x in descending_lists:
        if x == None: continue
        z = len(max(descending_lists,key=len))
        if len(x) == z:
            print(" -> ".join(map(str,x)))

mapping = generate_mapping(0, 10)
follow_the_arrows_from(mapping, 1)
longest_strictly_decreasing_sequences_to(mapping, 5)