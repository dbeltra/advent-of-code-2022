import functools

with open("input.txt") as f:
    data = f.read()
data = [p.splitlines() for p in data.split("\n\n")]

packets = {}
for idx, packet in enumerate(data, 1):
    packets[idx] = (eval(packet[0]), eval(packet[1]))

def compare_data(left, right):
    for el_left, el_right in zip(left, right):
        if type(el_left) == int and type(el_right) == int:
            if el_left < el_right:
                return 1
            if el_left > el_right:
                return -1
        elif type(el_left) == list and type(el_right) == list:
            result = compare_data(el_left, el_right)
            if result != 0:
                return result
        elif type(el_left) == int:
            result = compare_data([el_left], el_right)
            if result != 0:
                return result
        else:
            result = compare_data(el_left, [el_right])
            if result != 0:
                return result

    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1

    return 0

total = 0
for key, value in packets.items():
    if compare_data(value[0], value[1]) == 1:
        total += key

print(f'Solution to part one: {total}')

packets = [[[2]],[[6]]]
for pair in data:
    packets.append(eval(pair[0]))
    packets.append(eval(pair[1]))

packets = sorted(packets, key=functools.cmp_to_key(compare_data), reverse=True)
decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f'Solution to part two: {decoder_key}')
