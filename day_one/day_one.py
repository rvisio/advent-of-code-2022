import os

def get_data():
    with open(f'{os.getcwd()}/day_one/input.txt') as f:
        lines = f.readlines()
    return lines

def find_elf():
    elf_food = get_data()
    current_elf = 1
    current_calories = 0

    max_calories = 0
    second_most_calories = 0
    third_most_calories = 0
    max_elf = 1

    for food in elf_food:
        if food == '\n':
            max_elf = current_elf if current_calories > max_calories else max_elf

            if current_calories > max_calories:
                third_most_calories = second_most_calories
                second_most_calories = max_calories
                max_calories = current_calories
            elif current_calories > second_most_calories:
                third_most_calories = second_most_calories
                second_most_calories = current_calories
            elif  current_calories > third_most_calories:
                third_most_calories = current_calories


            max_calories = current_calories if current_calories > max_calories else max_calories

            current_elf += 1
            current_calories = 0
        else:
            current_calories += int(food)

    print(f'The max calories are {max_calories + second_most_calories + third_most_calories}')





