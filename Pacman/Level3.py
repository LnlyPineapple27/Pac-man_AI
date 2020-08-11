from Maze import *


def get_sub_list(start1, end1, start2, end2, list2d):
    return [items[start2:end2 + 1] for items in list2d[start1:end1 + 1]]

def level3(map: Maze, cur_pos: Point, explored: list):

    start_1 = cur_pos.x - 2 if cur_pos.x - 2 >= 0 else 0
    end_1 = cur_pos.x + 2 if cur_pos.x + 2 < map.N_row else map.N_row
    start_2 = cur_pos.y - 2 if cur_pos.y - 2 >= 0 else 0
    end_2 = cur_pos.y + 2 if cur_pos.y + 2 < map.M_col else map.M_col
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)

    vision = get_sub_list(start_1, end_1, start_2, end_2, map.maze_data)
    print(vision)
    return 0
    # create an empty map

