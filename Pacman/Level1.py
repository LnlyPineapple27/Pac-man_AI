from Maze import *


def can_move(maze: Maze, position: Point, explored: list, dead_path: list, ghost: bool) -> bool:
    entity = maze.maze_data[position.x][position.y]
    #print(position.coordinate(), maze.ENTITY_NAME[entity])
    return entity != maze.WALL and (entity != maze.MONSTER or not ghost) and position.coordinate() not in (explored + dead_path)

'''
def check_stuck(maze: Maze, dead_pos: Point) -> bool:
    stuck_pos = maze.maze_data[dead_pos.x][dead_pos.y]
    return stuck_pos == maze.WALL or stuck_pos == maze.MONSTER
'''


def level1(map: Maze, cur_pos: Point, current_path: list, dead_node: list, ghost=False) -> str:
    goal = map.treats[0]

    up = Point(cur_pos.x - 1, cur_pos.y)
    down = Point(cur_pos.x + 1, cur_pos.y)
    left = Point(cur_pos.x, cur_pos.y - 1)
    right = Point(cur_pos.x, cur_pos.y + 1)

    distance = {}
    max_dist = map.M_col + map.N_row
    #print("Up: ", end=" ")
    distance["Up"] = up.manhattan_distance(goal) if can_move(map, up, current_path, dead_node, ghost) else max_dist
    #print("Down: ", end=" ")
    distance["Down"] = down.manhattan_distance(goal) if can_move(map, down, current_path, dead_node, ghost) else max_dist
    #print("Left: ", end=" ")
    distance["Left"] = left.manhattan_distance(goal) if can_move(map, left, current_path, dead_node, ghost) else max_dist
    #print("Right: ", end=" ")
    distance["Right"] = right.manhattan_distance(goal) if can_move(map, right, current_path, dead_node, ghost) else max_dist

    got_stuck = all([max_dist == vl for vl in distance.values()])
    next_step = min(distance.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
    #print(distance)
    return next_step
