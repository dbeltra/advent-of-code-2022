
results_p1 = {'AX': 3+1, 'AY': 6+2, 'AZ': 0+3, 'BX': 0+1, 'BY': 3+2,
    'BZ': 6+3, 'CX': 6+1, 'CY': 0+2, 'CZ': 3+3}

results_p2 = {'AX': 0+3, 'AY': 3+1, 'AZ': 6+2, 'BX': 0+1, 'BY': 3+2,
    'BZ': 6+3, 'CX': 0+2, 'CY': 3+3, 'CZ': 6+1}

with open("input.txt") as f:
    data = f.read().strip().replace(" ", "").splitlines()

totalp1 = totalp2 = 0
for match in data:
    totalp1 += results_p1[match]
    totalp2 += results_p2[match]

print(f'solution to part 1: {totalp1}')
print(f'solution to part 1: {totalp2}')
