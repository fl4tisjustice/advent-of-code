import re

with open('/home/fl4t/Documents/AoC2023/Day 2/cubes_input.txt') as fl:
    games = fl.readlines()

target = {'red': 12, 'green': 13, 'blue': 14}

result = 0

for i, game in enumerate(games, 1):
    game = re.sub('Game [0-9]+: ', '', game.rstrip('\n')).split('; ')
    game = map(lambda x: x.split(', '), game)
    possible = True
    for cubeset in game:
        current = target.copy()
        for cube in cubeset:
            num, color = cube.split(' ')
            num = int(num)
            if current.get(color):
                current[color] -= num
        if any(num < 0 for num in current.values()):
            possible = False
            break

    result += i if possible else 0
    
print(result)
            