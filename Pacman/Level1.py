from Maze import *


def can_move(maze: Maze, position: Point, explored: list, dead_path: list, ghost: bool) -> bool:
    entity = maze.maze_data[position.x][position.y]
    print(position.coordinate(), maze.ENTITY_NAME[entity])
    print("Ex:",explored)
    print("dead_path:",dead_path)
    keep_away_nodes = (explored + dead_path)
    #rint("not_wall ^ (not_ghost or have ghost) ^ not_in_freakingup", entity != maze.WALL,entity != maze.MONSTER or not ghost,position.coordinate() not in keep_away_nodes)
    return entity != maze.WALL and (entity != maze.MONSTER or not ghost) and position.coordinate() not in keep_away_nodes

'''
def check_stuck(maze: Maze, dead_pos: Point) -> bool:
    stuck_pos = maze.maze_data[dead_pos.x][dead_pos.y]
    return stuck_pos == maze.WALL or stuck_pos == maze.MONSTER
'''


def level1(map: Maze, cur_pos: Point, current_path: list, dead_node: list, ghost=False) -> str:
    goal = map.treats[0]
    print("current: ", cur_pos.coordinate(), ", goal: ", goal.coordinate())
    up = cur_pos.up()
    down = cur_pos.down()
    left = cur_pos.left()
    right = cur_pos.right()

    distance = {}
    max_dist = map.M_col + map.N_row
    print("Up: ", end=" ")
    distance["Up"] = up.manhattan_distance(goal) if can_move(map, up, current_path, dead_node, ghost) else max_dist
    print("Down: ", end=" ")
    distance["Down"] = down.manhattan_distance(goal) if can_move(map, down, current_path, dead_node, ghost) else max_dist
    print("Left: ", end=" ")
    distance["Left"] = left.manhattan_distance(goal) if can_move(map, left, current_path, dead_node, ghost) else max_dist
    print("Right: ", end=" ")
    distance["Right"] = right.manhattan_distance(goal) if can_move(map, right, current_path, dead_node, ghost) else max_dist

    got_stuck = all([max_dist == vl for vl in distance.values()])
    next_step = min(distance.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
    print(distance)
    return next_step
