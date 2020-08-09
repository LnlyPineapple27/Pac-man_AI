from Maze import *


def level1(map: Maze, cur_pos: Point):  #map: Maze(rows, columns, m_data, p_man, treats)
    goal = map.treats.pop()

    up = map.maze_data[cur_pos.x][cur_pos.y - 1]
    down = map.maze_data[cur_pos.x][cur_pos.y + 1]
    left = map.maze_data[cur_pos.x - 1][cur_pos.y]
    right = map.maze_data[cur_pos.x + 1][cur_pos.y]

    distance = {}
    if up != 1 and up != 3:
        distance["Up"] = up.manhattan_distance(goal)
    else:
        distance["Up"] = map.M_col + map.N_row

    if down != 1 and down != 3:
        distance["Down"] = down.manhattan_distance(goal)
    else:
        distance["Down"] = map.M_col + map.N_row

    if left != 1 and left != 3:
        distance["Left"] = left.manhattan_distance(goal)
    else:
        distance["Left"] = map.M_col + map.N_row

    if right != 1 and right != 3:
        distance["Right"] = right.manhattan_distance(goal)
    else:
        distance["Right"] = map.M_col + map.N_row

    return min(distance.items(), key=lambda x: x[1])[0]
