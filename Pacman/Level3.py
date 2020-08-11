from Maze import *

"""
def getsubgrid(x1, y1, x2, y2, grid):
    return [item[x1:x2] for item in grid[y1:y2]]
"""

def get_vision(map: Maze, cur_pos: Point):
    result = []
    up = Point(cur_pos.x - 1, cur_pos.y)
    down = Point(cur_pos.x + 1, cur_pos.y)
    left = Point(cur_pos.x, cur_pos.y - 1)
    right = Point(cur_pos.x, cur_pos.y + 1)


    up_right = Point(cur_pos.x - 1, cur_pos.y + 1)
    up_left = Point(cur_pos.x - 1, cur_pos.y - 1)
    down_right = Point(cur_pos.x + 1, cur_pos.y + 1)
    down_left = Point(cur_pos.x + 1, cur_pos.y - 1)


    outer_up = Point(cur_pos.x - 2, cur_pos.y)
    outer_down = Point(cur_pos.x + 2, cur_pos.y)
    outer_left = Point(cur_pos.x, cur_pos.y - 2)
    outer_right = Point(cur_pos.x, cur_pos.y + 2)


    outer_up_right = Point(cur_pos.x - 2, cur_pos.y + 2)
    outer_up_left = Point(cur_pos.x - 2, cur_pos.y - 2)
    outer_down_right = Point(cur_pos.x + 2, cur_pos.y + 2)
    outer_down_left = Point(cur_pos.x + 2, cur_pos.y - 2)
    result.append([outer_up_right, outer_up_left, outer_down_right, outer_down_left])

    return result


def level3(map: Maze, cur_pos: Point, explored: list):
    """
    start_1 = cur_pos.x - 3 if cur_pos.x - 3 >= 0 else 0
    end_1 = cur_pos.x + 2 if cur_pos.x + 2 <= map.N_row else map.N_row
    start_2 = cur_pos.y - 3 if cur_pos.y - 3 >= 0 else 0
    end_2 = cur_pos.y + 2 if cur_pos.y + 2 <= map.M_col else map.M_col
    print ("start 1: ", start_1, "end 1:", end_1)
    print ("start 2: ", start_2, "end 2:", end_2)

    vision = getsubgrid(start_1, start_2, end_1, end_2, map.maze_data)
    """
    vision = get_vision(map,cur_pos)
    print(vision)
    return 0
    # create an empty map

