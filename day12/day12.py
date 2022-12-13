from collections import deque

with open("input.txt") as f:
    data = f.read().splitlines()

grid = [list (d) for d in data]

def find_shortest_path(grid, start, goal):
  # maintain a queue of paths
  queue = deque([[start]])
  # maintain a set of visited cells to avoid repeating paths
  visited = set()

  while queue:
    # get the first path from the queue
    path = queue.popleft()
    # get the last node from the path
    node = path[-1]

    # if the current node is the goal, we have found the shortest path
    if node == goal:
      return path

    # check all the possible movements from the current node
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      # compute the new coordinates of the potential next move
      x, y = node[0] + move[0], node[1] + move[1]
      # if the new coordinates are valid and not visited, we can add them to the queue
      if (x, y) not in visited and is_valid_move(grid, node, x, y):
        visited.add((x, y))
        new_path = path + [(x, y)]
        queue.append(new_path)

  return None

def find_start_end(grid):
    # Find the beggining and end points in the grid
    # and replace their values for the correct height
    start = None
    goal = None
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 'S':
                start = (x,y)
                grid[x][y] = 'a'
            if val == 'E':
                goal = (x,y)
                grid[x][y] = 'z'
            if start and goal:
                return grid, start, goal

def is_valid_move(grid, node, x, y):
  # check if the coordinates are outside the grid boundaries
  if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
    return False
  # check if we can climb to the cell
  cur_height = ord(grid[node[0]][node[1]])
  valid_heights = [h for h in range(97, cur_height+2)]
  if ord(grid[x][y]) not in valid_heights:
    return False
  return True

grid, start, goal = find_start_end(grid)
path = find_shortest_path(grid, start, goal)
print(f'Solution to part one is {len(path)-1}')
