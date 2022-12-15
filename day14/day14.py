class Grid:
    def __init__(self, points):
        self.obstacles = set()
        self.sand = set()
        self.parse_points_into_obstacles(points)

    def parse_points_into_obstacles(self, points):
        for line in points:
            for idx, add_point in enumerate(line, 1):
                if idx == len(line):
                    break # end of line
                else:
                    last_point = line[idx]
                    # add current point
                    self.add_obstacle_at(add_point)
                    # add points until last point
                    while add_point != last_point:
                        if add_point[0] < last_point[0]:
                            x, y = add_point[0] + 1, add_point[1]
                        elif add_point[0] > last_point [0]:
                            x, y = add_point[0] - 1, add_point[1]
                        elif add_point[1] < last_point [1]:
                            x, y = add_point[0], add_point[1] + 1
                        elif add_point[1] > last_point [1]:
                            x, y = add_point[0], add_point[1] - 1
                        add_point = (x,y)
                        self.add_obstacle_at(add_point)

    def is_obstacle_at(self, point):
        return point in self.obstacles or point in self.sand

    def add_obstacle_at(self, point):
        self.obstacles.add(point)

    def add_sand_at(self, point):
        self.sand.add(point)


with open("input.txt") as f:
    data = f.read().splitlines()

lines = [line.split(' -> ') for line in data]
points = [[(int(point.split(',')[0]), int(point.split(',')[1])) for point in line] for line in lines]

g = Grid(points)
falling = 0
while falling < 100:
    cur_point = sand_entry = (500, 0) # add new sand point
    blocked = False # sand is not blocked
    while not blocked and falling < 100:
        x,y = cur_point
        down = (x, y+1)
        down_l = (x-1, y+1)
        down_r = (x+1, y+1)
        # move sand
        if not g.is_obstacle_at(down):
            cur_point = down
            falling +=1
        elif not g.is_obstacle_at(down_l):
            cur_point = down_l
        elif not g.is_obstacle_at(down_r):
            cur_point = down_r
        else: # if snd cant move add it as an obstacle
            g.add_sand_at(cur_point)
            blocked = True # mark path as blocked so more sand is added
            falling = 0

print(f'Solution to part 1: {len(g.sand)}')
