import re
from functools import reduce

with open('cubes_input.txt') as fl:
    games = fl.readlines()

result = 0

for i, game in enumerate(games, 1):
    game = re.sub('Game [0-9]+: ', '', game.rstrip('\n')).split('; ')
    game = map(lambda x: x.split(', '), game)
    minimum = dict()
    for cubeset in game:
        for cube in cubeset:
            num, color = cube.split(' ')
            num = int(num)
            minimum[color] = max(minimum.get(color, 0), num)

    result += reduce(lambda x, y: x * y, minimum.values())
    
print(result)
            