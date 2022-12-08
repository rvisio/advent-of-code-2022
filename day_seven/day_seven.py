import os
import sys

def get_data():
    with open(f'{os.getcwd()}/day_seven/input.txt') as f:
        lines = f.readlines()
    return lines


def part_one():
    directories = {}
    directory_sizes = {}
    parent_directory = ''
    current_directory = ''

    commands = get_data()
    for command in commands:
        command = command.rstrip('\n')
        # process input command
        if command[0] == '$':
            if 'cd' in command:
                input = command.split(' ')
                if input[-1] == '..':
                    current_directory = parent_directory
                else:
                    parent_directory = current_directory
                    current_directory = input[-1]

                    if current_directory not in directories:
                        directories[current_directory] = []
                        directory_sizes[current_directory] = 0

            elif 'ls' in command:
                print(f'command is ls do we need to do anything')

        elif 'dir' in command:
            nested_dir = command.split(' ')[-1] #verify this gives what we want
            nested_dirs = directories[current_directory]

            if nested_dir not in nested_dirs:
                nested_dirs.append(nested_dir)
                directories[current_directory] = nested_dirs
        else:
            # we got a file with a size
            size = int(command.split(' ')[0])
            if current_directory in directory_sizes:
                current_size = directory_sizes[current_directory]
                current_size += size
                directory_sizes[current_directory] = current_size
            else:
                directory_sizes[current_directory] = size

    """RECURSIVE ATTEMPT FAILED"""
    # def add_stuff_recursively(parent_dir, current_dir, nested_directories):
    #     if len(nested_directories) == 0:
    #         current_dir_size = directory_sizes[current_dir]
    #         parent_dir_size = directory_sizes[parent_dir]
    #
    #         parent_dir_size += current_dir_size
    #
    #         directory_sizes[parent_dir] = parent_dir_size
    #     else:
    #         # this means we have more traversing to do
    #         for new_cur_dir in nested_directories:
    #             add_stuff_recursively(parent_dir=current_dir, current_dir=new_cur_dir, nested_directories=directories[new_cur_dir])
    #
    # dirs_to_big =
    # for
    #
    # root_dir = list(directories.keys())[0]
    #
    # add_stuff_recursively(parent_dir=root_dir, current_dir=root_dir, nested_directories=directories[root_dir])

    # For some reason the recursion isnt adding the size of the first diretory in the root directory array
    # first_item = directories[root_dir][0]
    # directory_sizes[root_dir] += directory_sizes[first_item]


    MAX_SIZE = 100000

    sum = 0
    for size in directory_sizes.values():
        if size < MAX_SIZE:
            sum += size

    print(f'SIZE SET TO {sum}')




    print(f'were at the end and its {directories}')
    print(f'were at the end and the directgory sizes are  {directory_sizes}')















