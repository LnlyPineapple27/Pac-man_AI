from Maze import *


def get_vision(map: Maze, cur_pos: Point):
    result = []
    up = Point(cur_pos.x - 1, cur_pos.y)
    down = Point(cur_pos.x + 1, cur_pos.y)
    left = Point(cur_pos.x, cur_pos.y - 1)
    right = Point(cur_pos.x, cur_pos.y + 1)
    result.append(up, down, left, right)

    up_right = Point(cur_pos.x - 1, cur_pos.y + 1)
    up_left = Point(cur_pos.x - 1, cur_pos.y - 1)
    down_right = Point(cur_pos.x + 1, cur_pos.y + 1)
    down_left = Point(cur_pos.x + 1, cur_pos.y - 1)
    result.append(up_right, up_left, down_right, down_left)

    outer_up = Point(cur_pos.x - 2, cur_pos.y)
    outer_down = Point(cur_pos.x + 2, cur_pos.y)
    outer_left = Point(cur_pos.x, cur_pos.y - 2)
    outer_right = Point(cur_pos.x, cur_pos.y + 2)
    result.append(outer_up, outer_down, outer_left, outer_right)

    outer_up_right = Point(cur_pos.x - 2, cur_pos.y + 2)
    outer_up_left = Point(cur_pos.x - 2, cur_pos.y - 2)
    outer_down_right = Point(cur_pos.x + 2, cur_pos.y + 2)
    outer_down_left = Point(cur_pos.x + 2, cur_pos.y - 2)
    result.append(outer_up_right, outer_up_left, outer_down_right, outer_down_left)

    return result


def level3(map: Maze, cur_pos: Point, explored: list):
    vision = get_vision(map, cur_pos)

    # create an empty map
    knowledge = []
    for i in range(map.N_row):
        for j in range(map.M_col):
            knowledge.append(0)

    # load data from vision into knowledge
    for node in vision:
        knowledge[node.x][node.y] = map[node.x][node.y]
