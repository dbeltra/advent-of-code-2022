from copy import deepcopy

with open("input.txt") as f:
    data = f.read().splitlines()

CONTAINERS = {
    '1': ['C', 'F', 'B', 'L', 'D', 'P', 'Z','S'],
    '2': ['B', 'W', 'H', 'P', 'G', 'V', 'N'],
    '3': ['G', 'J', 'B', 'W', 'F'],
    '4': ['S', 'C', 'W', 'L', 'F', 'N', 'J', 'G'],
    '5': ['H', 'S', 'M', 'P', 'T', 'L', 'J', 'W'],
    '6': ['S', 'F', 'G', 'W', 'C', 'B'],
    '7': ['W', 'B', 'Q', 'M', 'P', 'T', 'H'],
    '8': ['T', 'W', 'S', 'F'],
    '9': ['R', 'C', 'N']
}

def move_containers(containers, num, origin, dest):
    for n in range(num):
        crate = containers[origin].pop(0)
        containers[dest].insert(0, crate)

def move_containers_blocks(containers, num, origin, dest):
    crates_to_move = []
    for n in range(num):
        crate = containers[origin].pop(0)
        crates_to_move.insert(0, crate)

    for crate in crates_to_move:
        containers[dest].insert(0, crate)

def get_top_containers(containers):
    result = ''
    for c in containers.values():
        result += c[0]
    return result

CONT1 = deepcopy(CONTAINERS)
CONT2 = deepcopy(CONTAINERS)

for instruction in data:
    if 'move' in instruction:
        i = instruction.split(' from ')
        num = i[0].replace('move ', '')
        origin = i[1].split(' to ')[0]
        dest = i[1].split(' to ')[1]
        move_containers(CONT1, int(num), origin, dest)
        move_containers_blocks(CONT2, int(num), origin, dest)

resultp1 = get_top_containers(CONT1)
resultp2 = get_top_containers(CONT2)

print(f'solution to part 1: {resultp1}')
print(f'solution to part 2: {resultp2}')
