import re
from functools import reduce

with open ('trebuchet_input.txt', 'r') as fl:
    lines = fl.readlines();

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i, line in enumerate(lines):
    for j, num in enumerate(numbers):
        line = line.replace(num, f"{num[0]}{str(j + 1)}{num[-1]}")

    lines[i] = line

lines = [int(re.sub('([0-9]).*([0-9])|[A-Za-z]', r'\1\2', line).rstrip('\n')) for line in lines]
callback = lambda x, y: x + y if y >= 10 else x + 10 * y + y
print(reduce(callback, lines));