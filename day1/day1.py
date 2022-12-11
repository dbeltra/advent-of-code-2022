with open("input.txt") as f:
    data = f.read().splitlines()

elf_calories = []
elf_total = 0
for line in data:
    if line != '':
        elf_total += int(line)
    else:
        elf_calories.append(elf_total)
        elf_total = 0

elf_calories.sort(reverse=True)

print(f'solution to part 1: {elf_calories[0]}')
print(f'solution to part 1: {elf_calories[0] + elf_calories[1] + elf_calories[2]}')
