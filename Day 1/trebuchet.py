import re
from functools import reduce

with open ('trebuchet_input.txt', 'r') as fl:
    lines = fl.readlines();

lines = [int(re.sub('([0-9]).*([0-9])|[A-Za-z]', r'\1\2', line).rstrip('\n')) for line in lines]
callback = lambda x, y: x + y if y >= 10 else x + 10 * y + y
print(reduce(callback, lines));