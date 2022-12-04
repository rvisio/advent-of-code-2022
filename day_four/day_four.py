import os


def get_data():
    with open(f'{os.getcwd()}/day_four/input.txt') as f:
        lines = f.readlines()
    return lines

def assignment_overlap():
    assignments = get_data()
    count = 0

    for assignment in assignments:
        assignment = assignment.rstrip('\n')
        first_elf, second_elf = assignment.split(',')
        first_elf_start, first_elf_end = [int(x) for x in first_elf.split('-')]
        second_elf_start, second_elf_end = [int(y) for y in second_elf.split('-')]

        #first_contains_second = first_elf_start <= second_elf_start and first_elf_end >= second_elf_end

        second_within_first = second_elf_start >= first_elf_start and second_elf_start <= first_elf_end


        # if first_elf_start <= second_elf_start and first_elf_end >= second_elf_end:
        #     count += 1
        # if first_contains_second:

        # second_contains_first = second_elf_start <= first_elf_start and second_elf_end >= first_elf_end
        first_within_second = first_elf_start >= second_elf_start and first_elf_start <= second_elf_end
        # if second_elf_start <= first_elf_start and second_elf_end >= first_elf_end:
        if second_within_first or first_within_second:
            count += 1

    print(f' count se to {count}')


