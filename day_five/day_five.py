import os


def get_data():
    with open(f'{os.getcwd()}/day_five/input.txt') as f:
        lines = f.readlines()
    return lines

num_stacks = 9
def sort_crates():
    crates = get_data()
    stacks = []
    for num in range(0,num_stacks):
        stacks.append([])

    for crate in crates:
        if '[' in crate:
            crate = crate.rstrip('\n')
            for value in range(0, len(crate), 2):
                if crate[value] == '[':
                    if value == 0:
                        stacks[0].insert(0, crate[value+1])
                    elif value == 4:
                        stacks[1].insert(0, crate[value+1])
                    elif value == 8:
                        stacks[2].insert(0, crate[value+1])
                    elif value == 12:
                        stacks[3].insert(0, crate[value + 1])
                    elif value == 16:
                        stacks[4].insert(0, crate[value + 1])
                    elif value == 20:
                        stacks[5].insert(0, crate[value + 1])
                    elif value == 24:
                        stacks[6].insert(0, crate[value + 1])
                    elif value == 28:
                        stacks[7].insert(0, crate[value + 1])
                    elif value == 32:
                        stacks[8].insert(0, crate[value + 1])
        elif 'move' in crate and 'from' in crate:
            commands = crate.split(' ')
            amount = int(commands[1])
            from_column = int(commands[3]) - 1
            to_column = int(commands[5]) - 1

            print(f' were going to move {amount} crates from {from_column} to {to_column}')
            originial_to_col_length = len(stacks[to_column])
            for move in range(0,amount):
                temp = stacks[from_column].pop()
                if amount > 1:
                    stacks[to_column].insert(originial_to_col_length,temp)
                else:
                    stacks[to_column].append(temp)


                print(f' we just updated the stacks are now {stacks}')

    string = ''
    for x in range(0, num_stacks):
        string = f'{string}{stacks[x][-1]}'
    print(f'string is {string}')
    # print(f'the crates at the end are {stacks[x][-1].pop() for x in range(0,num_stacks)}')


