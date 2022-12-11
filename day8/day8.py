with open("input.txt") as f:
    tree_map = [[tree for tree in row] for row in f.read().splitlines()]

EDGE_LEFT = EDGE_TOP = -1
EDGE_RIGHT = EDGE_BOTTOM = len(tree_map)
VISIBLE_TREES = 0
BEST_SCORE = 0

def tree_checker(row, col, tree_height, start, end, direction, step=1):
    score = 0
    blocked = False
    for x in range(start, end, step):
        if direction == 'COL':
            value = tree_map[row][x]
        else: # row
            value = tree_map[x][col]
        score += 1
        if value >= tree_height:
            blocked = True
            break
    return score, blocked

def check_visibility_and_score(row, col, val):
    visible = True
    if row == 0 or col == 0:
        return True, 0

    score_r, block_r = tree_checker(row, col, val, col+1, EDGE_RIGHT, 'COL', 1)
    score_l, block_l = tree_checker(row, col, val, col-1, EDGE_LEFT, 'COL', -1)
    score_b, block_b = tree_checker(row, col, val, row+1, EDGE_BOTTOM, 'ROW', 1)
    score_t, block_t = tree_checker(row, col, val, row-1, EDGE_TOP, 'ROW', -1)

    if block_r and block_l and block_b and block_t:
        visible = False

    return visible, score_r * score_l * score_b * score_t

for row, valrow in enumerate(tree_map):
     for col, val in enumerate(valrow):
        visible, tree_score = check_visibility_and_score(row,col, val)
        if visible:
            VISIBLE_TREES += 1
        if tree_score > BEST_SCORE:
            BEST_SCORE = tree_score

print(f"solution to part 1: {VISIBLE_TREES}")
print(f"solution to part 2: {BEST_SCORE}")
