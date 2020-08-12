from Maze import *
import random
import copy as cp
import Level1


def can_move(map: Maze, cur_pos: Point, current_path: list, dead_nodes: list) -> bool:
    keep_away_nodes = current_path + dead_nodes
    return map.maze_data[cur_pos.x][cur_pos.y] != map.WALL and cur_pos.coordinate() not in keep_away_nodes


def get_sub_list(start1, end1, start2, end2, list2d):
    return [items[start2:end2 + 1] for items in list2d[start1:end1 + 1]]


def evaluate_point(pnt: Point, start1, start2):
    cp_point = cp.deepcopy(pnt)
    cp_point.x -= start1
    cp_point.y -= start2
    return cp_point


def evaluate_coordinate(node: tuple, start1, start2):
    return node[0] - start1, node[1] - start2


def in_map(range_x, range_y, coordinate):
    return coordinate[0] in range_x and coordinate[1] in range_y


def vision(map: Maze, current_position: Point) -> (Maze, list, list):
    """
    Return a tuple of (sub-map of map that in vision of pacman, row range, column range)
    :param map:
    :param current_position:
    :return:
    """
    start_1 = current_position.x - 2 if current_position.x - 2 >= 0 else 0
    end_1 = current_position.x + 2 if current_position.x + 2 < map.N_row else map.N_row
    start_2 = current_position.y - 2 if current_position.y - 2 >= 0 else 0
    end_2 = current_position.y + 2 if current_position.y + 2 < map.M_col else map.M_col
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vi = get_sub_list(start_1, end_1, start_2, end_2, map.maze_data)
    row_range = range(start_1, end_1 + 1)
    col_range = range(start_2, end_2 + 1)
    treats = [evaluate_point(treat, start_1, start_2) for treat in map.treats if in_map(row_range, col_range, treat.coordinate())]
    new_pos = evaluate_point(current_position, start_1, start_2)
    return Maze(map.N_row, map.M_col, vi, new_pos, treats), row_range, col_range


def level3(map: Maze, cur_pos: Point, path: list, dead_node:list):
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vision_map, r1, r2 = vision(map, cur_pos)
    print("Map:")
    vision_map.print_raw_data()
    print("Treats: ", [item.coordinate() for item in vision_map.treats])
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
        vision_path = [evaluate_coordinate(node, r1[0], r2[0]) for node in path if in_map(r1, r2, node)]
        vision_dead_nodes = [evaluate_coordinate(node, r1[0], r2[0]) for node in dead_node if in_map(r1, r2, node)]
        return Level1.level1(vision_map, vision_map.pacman_init_position, vision_path, vision_dead_nodes, True)


