from Maze import *


def can_move(maze: Maze, position: Point, explored: list, dead_path: list, ghost: bool) -> bool:
    entity = maze.maze_data[position.x][position.y]
    #print(position.position(), maze.ENTITY_NAME[entity])
    return entity != maze.WALL and (entity != 3 or not ghost) and position.position() not in explored \
           and position.position() not in dead_path


def check_stuck(maze: Maze, dead_pos: Point) -> bool:
    stuck_pos = maze.maze_data[dead_pos.x][dead_pos.y]
    return stuck_pos == maze.WALL or stuck_pos == maze.MONSTER


def level1(map: Maze, cur_pos: Point, explored: list, dead_path: list, ghost=False) -> str:  # map: Maze(rows, columns, m_data, p_man, treats)
    goal = map.treats[0]
    print(cur_pos.position(), goal.position())
    up = Point(cur_pos.x - 1, cur_pos.y)
    down = Point(cur_pos.x + 1, cur_pos.y)
    left = Point(cur_pos.x, cur_pos.y - 1)
    right = Point(cur_pos.x, cur_pos.y + 1)

    num_check = 0
    if check_stuck(map, up):
        num_check += 1
    if check_stuck(map, down):
        num_check += 1
    if check_stuck(map, left):
        num_check += 1
    if check_stuck(map, right):
        num_check += 1

    if num_check >= 3:
        return "Stuck"

    distance = {}
    max_dist = map.M_col + map.N_row
    #print("Up: ", end=" ")
    distance["Up"] = up.manhattan_distance(goal) if can_move(map, up, explored, dead_path, ghost) else max_dist
    #print("Down: ", end=" ")
    distance["Down"] = down.manhattan_distance(goal) if can_move(map, down, explored, dead_path, ghost) else max_dist
    #print("Left: ", end=" ")
    distance["Left"] = left.manhattan_distance(goal) if can_move(map, left, explored, dead_path, ghost) else max_dist
    #print("Right: ", end=" ")
    distance["Right"] = right.manhattan_distance(goal) if can_move(map, right, explored, dead_path, ghost) else max_dist
    m = min(distance.items(), key=lambda x: x[1])
    print(distance)

    return m[0]
