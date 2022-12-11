with open("input.txt") as f:
    input = f.read().splitlines()

def init_signals():
    signals = []
    x = 1
    for command in input:
        if command == 'noop':
            signals = signals + [x]
        else:
            val = command.split(' ')[1]
            signals = signals + [x, x]
            x += int(val)
    return signals

def get_pixel_val(cycle, pos):
	if (cycle - 1) % 40 in [pos-1, pos, pos+1]:
		return '#'
	return '.'

cycle = 1
total = 0
watch_cycles = [20, 60, 100, 140, 180, 220]

print(f'Solution to part 2 is:')

for idx, val in enumerate(init_signals(), start=1):
    pix_val = get_pixel_val(cycle, val)
    end = ' '
    if idx % 40 == 0:
        end = '\n'
    print(pix_val,  end=end)

    if cycle in watch_cycles:
        total += cycle * val
    cycle += 1

print(f'Solution to part 1 is {total}')
