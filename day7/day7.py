import re

with open("input.txt") as f:
    data = f.read().splitlines()

files = {}
current_dir = '/'

# Find all files and store their path and size
for line in data:
    if line.startswith('$ cd'):
        cd_argument = line.split('$ cd ')[1]
        if cd_argument == '..':
            current_dir = '/'.join(current_dir.split('/')[:-2]) + '/'
        elif cd_argument == '/':
            pass
        else: # we are moving into a dir
            current_dir += cd_argument + '/'

    if not line.startswith('$'):
        match = re.match(r'(\d+)\s+(\S+)', line)
        if match:
            size, name = match.groups()
            size = int(size)
            files[current_dir + name] = size

# Calculate the total sizes of the directories
dir_sizes = {}
for path, size in files.items():
    path = path.split('/')[:-1]
    current_dir = ''
    for part in path:
        current_dir += part + '/'
        if current_dir not in dir_sizes:
            dir_sizes[current_dir] = 0
        dir_sizes[current_dir] += size

max_size = 100000
total_size = 0
for size in dir_sizes.values():
    if size < 100000:
        total_size += size

print(f"solution to part 1: {total_size}")

total_disk = 70000000
space_needed = 30000000
unused_space = total_disk - dir_sizes['/']
need_to_free = space_needed - unused_space

dirs_sorted = dict(sorted(dir_sizes.items(), key=lambda x:x[1]))

total_size = 0
for size in dirs_sorted.values():
    if size > need_to_free:
        total_size = size
        break

print(f"solution to part 2: {total_size}")
