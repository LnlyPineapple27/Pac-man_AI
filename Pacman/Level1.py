from Maze import *


def level1(map: Maze, cur_pos: Point, explored: list, ghost=False) -> str:  #map: Maze(rows, columns, m_data, p_man, treats)
    goal = map.treats[0]
    #print(cur_pos.position())
    up = Point(cur_pos.x - 1, cur_pos.y)
    down = Point(cur_pos.x + 1, cur_pos.y)
    left = Point(cur_pos.x, cur_pos.y - 1)
    right = Point(cur_pos.x, cur_pos.y + 1)

    distance = {}
    max_dist = map.M_col + map.N_row
    up_unity = map.maze_data[up.x][up.y]
    down_unity = map.maze_data[down.x][down.y]
    left_unity = map.maze_data[left.x][left.y]
    right_unity = map.maze_data[right.x][right.y]

    distance["Up"] = up.manhattan_distance(goal) if up_unity != 1 and (up_unity != 3 or not ghost) and up.position() not in explored else max_dist
    distance["Down"] = down.manhattan_distance(goal) if down_unity != 1 and (down_unity != 3 or not ghost) and down.position() not in explored else max_dist
    distance["Left"] = left.manhattan_distance(goal) if left_unity != 1 and (left_unity != 3 or not ghost) and left.position() not in explored else max_dist
    distance["Right"] = right.manhattan_distance(goal) if right_unity != 1 and (right_unity != 3 or not ghost) and right.position() not in explored else max_dist
    m = min(distance.items(), key=lambda x: x[1])
    return m[0]
