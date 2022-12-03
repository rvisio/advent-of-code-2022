import os
from itertools import zip_longest


def get_data():
    with open(f'{os.getcwd()}/day_three/input.txt') as f:
        lines = f.readlines()
    return lines

# http://docs.python.org/library/itertools.html#itertools-recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26,
            'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38,
            'M': 39,
            'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51,
            'Z': 52}

def rucksack():
    sacks = get_data()
    sum = 0
    for first, second, third in grouper(sacks, 3, 0.0):
        first = first.rstrip('\n')
        second = second.rstrip('\n')
        third = third.rstrip('\n')

        group_counter_map = {}

        for item in first:
            group_counter_map[item] = 1

        for item in second:
            if item in group_counter_map:
                if group_counter_map[item] != 2:
                    group_counter_map[item] = group_counter_map[item] + 1

        for item in third:
            if item in group_counter_map:
                if group_counter_map[item] == 2:
                    group_counter_map[item] = group_counter_map[item] + 1

        for key, value in group_counter_map.items():
            if value == 3:
                sum += priority[key]

    print(f'sum set to {sum}')


    #     sack_length = len(sack)
    #     first_compartment = sack[0 : sack_length//2]
    #     second_compartment = sack[sack_length//2:]
    #     items = []
    #     for first_item in first_compartment:
    #         if first_item not in items:
    #             for second_item in second_compartment:
    #                 if first_item == second_item:
    #                     items.append(second_item)
    #                     print(f'found two similar {first_item} {second_item}')
    #
    #                     sum += priority[first_item]
    #                     break
    #
    # print(f'sum set to {sum}')



