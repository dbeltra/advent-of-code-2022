def range_contains(elf1, elf2):
    if (set(elf2).issubset(set(elf1))):
        return True
    return False

def range_overlaps(elf1,elf2):
    if (len(list(set(elf1) & set(elf2))) > 0):
        return True
    return False

def get_list_from_range(elf_range):
    range_parts = elf_range.split('-')
    return [*range(int(range_parts[0]), int(range_parts[1])+1)]

with open("input.txt") as f:
    data = f.read().splitlines()

num_contained = 0
num_overlaps = 0
for elf_pair in data:
    elf1 = get_list_from_range(elf_pair.split(',')[0])
    elf2 = get_list_from_range(elf_pair.split(',')[1])

    if range_contains(elf1, elf2) or range_contains(elf2, elf1):
        num_contained +=1

    if range_overlaps(elf1, elf2):
        num_overlaps +=1

print(f'solution to part 1: {num_contained}')
print(f'solution to part 2: {num_overlaps}')
