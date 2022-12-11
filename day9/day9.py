with open("input.txt") as f:
    data = f.read().splitlines()

class Head():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, units):
        if direction == 'R':
            self.x += units
        elif direction == 'L':
            self.x -= units
        elif direction == 'U':
            self.y += units
        elif direction == 'D':
            self.y -= units

class Tail():
    def __init__(self, x, y, head):
        self.x = x
        self.y = y
        self.head = head
        self.visited_positions = []

    def update(self):
        if (self.x, self.y) not in self.visited_positions:
            self.visited_positions.append((self.x, self.y))
        if not self.is_touching_head():
            self.catch_up()

    def is_touching_head(self):
        adjacent_positions = [(self.x, self.y), (self.x, self.y+1), (self.x, self.y-1),
            (self.x+1, self.y), (self.x+1, self.y+1), (self.x+1, self.y-1),
            (self.x-1, self.y), (self.x-1, self.y+1), (self.x-1, self.y-1)]
        if (self.head.x, self.head.y) in adjacent_positions:
            return True
        return False

    def catch_up(self):
        if self.head.x > self.x:
            self.x +=1
        if self.head.x < self.x:
            self.x -=1
        if self.head.y > self.y:
            self.y +=1
        if self.head.y < self.y:
            self.y -=1

H = Head(0, 0)
T = Tail(0, 0, H)

tails = {1:  Tail(0, 0, H)}
for t in range(2, 10):
    tails[t] = Tail(0, 0, tails[t-1])

for instruction in data:
    direction, units = instruction.split(' ')
    for s in range(int(units)):
        H.move(direction, 1)
        T.update()
        for tail in tails.values():
            tail.update()

print(f'Solution to part 1: {len(T.visited_positions)}')
print(f'Solution to part 2: {len(tails[9].visited_positions)}')
