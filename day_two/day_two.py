import os


def get_data():
    with open(f'{os.getcwd()}/day_two/input.txt') as f:
        lines = f.readlines()
    return lines


"""
Input
First column: what opponent plays. A = rock, B = Paper, C = Scissors
Second Column: result of game . X = lose, Y = draw, Z = win

Scoring:
Shape I play = Rock/X 1 pt, Paper/Y 2 pts, Scissors/Z 3 pts
Outcome = 0 if loss, 3 if draw, 6 if won
"""


def getResult(opponent, result):
    # opponent plyed rock
    if opponent == 'A':
        # need to lose by playing scissors
        if result == 'X':
            return 0 + 3
        # draw by playing rock
        if result == 'Y':
            return 3 + 1
        # win by playing paper
        if result == 'Z':
            return 6 + 2
    # opponent played paper
    if opponent == 'B':
        # lose by playing rock
        if result == 'X':
            return 0 + 1
        # draw by playing paper
        if result == 'Y':
            return 3 + 2
        # win by playing scissors
        if result == 'Z':
            return 6 + 3
    # opponent played scissors
    if opponent == 'C':
        # lose by playing paper
        if result == 'X':
            return 0 + 2
        # draw by playing scissors
        if result == 'Y':
            return 3 + 3
        # win by playing rock
        if result == 'Z':
            return 6 + 1


def day_two():
    matches = get_data()
    total = 0
    for match in matches:
        opponent, result = match.rstrip('\n').split(' ')
        result = getResult(opponent, result)
        total += result

    print(total)
