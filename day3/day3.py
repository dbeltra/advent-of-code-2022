def letter_to_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter.lower()) - 96 + 26

with open("input.txt") as f:
    data = f.read().splitlines()

total_priority = 0
for rucksack in data:
    l = len(rucksack)
    comp1 = rucksack[:l//2]
    comp2 = rucksack[l//2:]

    for item in comp1:
        position = comp2.find(item)
        if position != -1:
            total_priority += letter_to_priority(item)
            break

print(f'solution to part 1: {total_priority}')

total_priority = 0
elf_group = []
for rucksack in data:
    elf_group.append(rucksack)
    if len(elf_group) == 3:
        for item in elf_group[0]:
            position1 = elf_group[1].find(item)
            position2 = elf_group[2].find(item)
            if position1 != -1 and position2 != -1:
                total_priority += letter_to_priority(item)
                break

        elf_group = []

print(f'solution to part 2: {total_priority}')
