with open('gear_input.txt', 'r') as fl:
    schematic = fl.read().splitlines()

width = len(schematic[0])
height = len(schematic)

issymbol = lambda s: s != '.' and s.isascii() and not s.isalnum()
positions = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

sum = 0;
l_edge = r_edge = 0

for ln, line in enumerate(schematic):
    for idx, ch in enumerate(line):
        if issymbol(ch):
            for n, (i, j) in enumerate(positions):
                if n % 3 == 0:
                    l_edge = r_edge = 0
                if not (0 <= ln + i < height and 0 <= idx + j < width):
                    continue
                if schematic[ln + i][idx + j].isdigit():
                    if l_edge < idx + j < r_edge:
                        continue
                    cleaned = ''.join(map(lambda s: '.' if not s.isdigit() else s, schematic[ln + i]))                
                    l_edge = cleaned.rfind('.', 0, idx + j)
                    r_edge = cleaned.find('.', idx + j)
                    num_str = ''.join(cleaned[l_edge+1:r_edge if r_edge != -1 else None])
                    sum += int(num_str)

print(sum)