from Maze import *
import random
import copy as cp
import Level1


def can_move(map: Maze, cur_pos: Point, current_path: list, dead_nodes: list) -> bool:
    keep_away_nodes = current_path + dead_nodes
    return map.maze_data[cur_pos.x][cur_pos.y] != map.WALL and cur_pos.coordinate() not in keep_away_nodes


def get_sub_list(start1, end1, start2, end2, list2d):
    return [items[start2:end2 + 1] for items in list2d[start1:end1 + 1]]


def vision(map: Maze, current_position: Point) -> Maze:
    start_1 = current_position.x - 2 if current_position.x - 2 >= 0 else 0
    end_1 = current_position.x + 2 if current_position.x + 2 < map.N_row else map.N_row
    start_2 = current_position.y - 2 if current_position.y - 2 >= 0 else 0
    end_2 = current_position.y + 2 if current_position.y + 2 < map.M_col else map.M_col
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vi = get_sub_list(start_1, end_1, start_2, end_2, map.maze_data)
    row_range = range(start_1, end_1 + 1)
    col_range = range(start_1, end_2 + 1)
    treats = [treat for treat in map.treats if treat.x in row_range and treat.y in col_range]
    new_pos = cp.copy(current_position)
    new_pos.x -= start_1
    new_pos.y -= start_2
    return Maze(map.N_row, map.M_col, vi, new_pos, treats)


def level3(map: Maze, cur_pos: Point, path: list, dead_node:list):
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vision_map = vision(map, cur_pos)

    if not vision_map.treats:
        directions = []
        print("rand")
        if can_move(map, cur_pos.up(), path, dead_node):
            directions.append("Up")
        if can_move(map, cur_pos.down(), path, dead_node):
            directions.append("Down")
        if can_move(map, cur_pos.left(), path, dead_node):
            directions.append("Left")
        if can_move(map, cur_pos.right(), path, dead_node):
            directions.append("Right")
        print(directions)
        return random.choice(directions) if directions else "Stuck"
    else:
        return Level1.level1(vision_map, vision_map.pacman_init_position, path, dead_node, True)


