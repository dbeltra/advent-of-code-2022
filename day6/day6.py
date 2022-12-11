with open("input.txt") as f:
    data = f.read()

packet = {
    'marker': [],
    'max_len': 4,
    'position': 0
}

message = {
    'marker': [],
    'max_len': 14,
    'position': 0
}

def add_to_marker(comm_obj, character):
    marker = comm_obj['marker']
    max_len = int(comm_obj['max_len'])
    marker.append(character)
    if len(marker) > max_len:
        marker.pop(0)

def validate_marker(comm_obj, pos):
    marker = comm_obj['marker']
    max_len = int(comm_obj['max_len'])
    if len(marker) < max_len or len(set(marker)) < max_len:
        return False
    if comm_obj['position'] == 0:
        comm_obj['position'] = pos
    return True

for idx, character in enumerate(data):
    add_to_marker(packet, character)
    add_to_marker(message, character)
    validate_marker(packet, idx+1)
    validate_marker(message, idx+1)

print(f"solution to part 1: {packet['position']}")
print(f"solution to part 2: {message['position']}")
