from Maze import *
import random
import copy as cp
import Level3
import Level1


def ghost_can_move(map: Maze, cur_pos: Point) -> bool:
    return map.maze_data[cur_pos.x][cur_pos.y] != map.WALL


def ghost_vision(map: Maze, current_position: Point) -> (Maze, list, list):
    """
    Return a tuple of (sub-map of map that in vision of pacman, row range, column range)
    :param map:
    :param current_position:
    :return:
    """
    VISION_RANGE = 1
    start_1 = current_position.x - VISION_RANGE if current_position.x - VISION_RANGE >= 0 else 0
    end_1 = current_position.x + VISION_RANGE if current_position.x + VISION_RANGE < map.N_row else map.N_row - 1
    start_2 = current_position.y - VISION_RANGE if current_position.y - VISION_RANGE >= 0 else 0
    end_2 = current_position.y + VISION_RANGE if current_position.y + VISION_RANGE < map.M_col else map.M_col - 1
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vi = Level3.get_sub_list(start_1, end_1, start_2, end_2, map.maze_data)
    row_range = range(start_1, end_1 + 1)
    col_range = range(start_2, end_2 + 1)
    #new_pos = evaluate_point(current_position, start_1, start_2)
    return vi, row_range, col_range


def find_pacman_in_vision(vision_map: Maze, current_position: Point, row_range, col_range, pacman_location):
    ghost_list = []

    print("Range: ", "row: ", row_range, "col: ", col_range)
    for i in row_range:
        for j in col_range:
            if vision_map.maze_data[i - row_range[0]][j - col_range[0]] == ???:
                ghost_list.append(Point(i, j))
    return ghost_list


def ghost_move(map: Maze, cur_pos: Point, dict_for_ghost_tracing: dict, pacman_location):
    print("ghost current: ", cur_pos.coordinate())
    up = cur_pos.up()
    down = cur_pos.down()
    left = cur_pos.left()
    right = cur_pos.right()

    directions = []
    view, new_pos, r1, r2 = ghost_vision(map, cur_pose)
    print("ghost rand")
    if ghost_can_move(map, up):
        directions.append("Up")
    if ghost_can_move(map, down):
        directions.append("Down")
    if ghost_can_move(map, left):
        directions.append("Left")
    if ghost_can_move(map, right):
        directions.append("Right")
    print(directions)
    g_move = random.choice(directions) if directions else "Stuck"
    return g_move


#------------------------------------Dont touch this ------------------------------------------------
def level4(map: Maze, cur_pos: Point, path: list, dead_node: list):
    vision_map, r1, r2 = Level3.vision(map, cur_pos)
    print("Vision Map:")
    vision_map.print_raw_data()
    print("Treats: ", [item.coordinate() for item in vision_map.treats])
    ghosts_in_vision = Level3.find_ghost_in_vision(vision_map, cur_pos, r1, r2)
    up = cur_pos.up()
    down = cur_pos.down()
    left = cur_pos.left()
    right = cur_pos.right()
    if not vision_map.treats:
        # food not in vision
        if ghosts_in_vision:
            print("Ghost in vision be careful")
            directions = {}
            min_dist = 0
            # get possible direction
            if Level3.can_move(map, up, path, dead_node):
                directions["Up"] = 0
            if Level3.can_move(map, down, path, dead_node):
                directions["Down"] = 0
            if Level3.can_move(map, left, path, dead_node):
                directions["Left"] = 0
            if Level3.can_move(map, right, path, dead_node):
                directions["Right"] = 0

            for ghost in ghosts_in_vision:
                for dir in directions:
                    if dir == "Up":
                        temp_dist = up.manhattan_distance(ghost)
                        if directions["Up"] < temp_dist:
                            directions["Up"] = temp_dist
                    if dir == "Down":
                        temp_dist = down.manhattan_distance(ghost)
                        if directions["Down"] < temp_dist:
                            directions["Down"] = temp_dist
                    if dir == "Left":
                        temp_dist = left.manhattan_distance(ghost)
                        if directions["Left"] < temp_dist:
                            directions["Left"] = temp_dist
                    if dir == "Right":
                        temp_dist = right.manhattan_distance(ghost)
                        if directions["Right"] < temp_dist:
                            directions["Right"] = temp_dist


            print("--------------------------------CALCULATION:", directions)
            got_stuck = all([min_dist == vl for vl in directions.values()])

            # randomly delete 1 direction if more than 1 direction has value equal to max value in directions
            dup_val = 0
            d_list = []
            temp_step = max(directions.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
            for dir in directions:
                if directions[dir] == temp_step:
                    print(dir, directions[dir])
                    d_list.append(dir)
                    dup_val += 1
            if dup_val > 1:
                index = random.randrange(0, len(d_list), 1)
                del directions[d_list[index]]

            next_step = max(directions.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
            return next_step
        else:
            directions = []
            print("rand")
            if Level3.can_move(map, cur_pos.up(), path, dead_node):
                directions.append("Up")
            if Level3.can_move(map, cur_pos.down(), path, dead_node):
                directions.append("Down")
            if Level3.can_move(map, cur_pos.left(), path, dead_node):
                directions.append("Left")
            if Level3.can_move(map, cur_pos.right(), path, dead_node):
                directions.append("Right")
            print(directions)
            return random.choice(directions) if directions else "Stuck"
    else:
        # food in vision
        if ghosts_in_vision:
            print("Ghost in vision be careful")
            directions = {}
            min_dist = 0
            # get possible direction
            if Level3.can_move(map, up, path, dead_node):
                directions["Up"] = 0
            if Level3.can_move(map, down, path, dead_node):
                directions["Down"] = 0
            if Level3.can_move(map, left, path, dead_node):
                directions["Left"] = 0
            if Level3.can_move(map, right, path, dead_node):
                directions["Right"] = 0

            for ghost in ghosts_in_vision:
                for dir in directions:
                    if dir == "Up":
                        temp_dist = up.manhattan_distance(ghost)
                        if directions["Up"] < temp_dist:
                            directions["Up"] = temp_dist
                    if dir == "Down":
                        temp_dist = down.manhattan_distance(ghost)
                        if directions["Down"] < temp_dist:
                            directions["Down"] = temp_dist
                    if dir == "Left":
                        temp_dist = left.manhattan_distance(ghost)
                        if directions["Left"] < temp_dist:
                            directions["Left"] = temp_dist
                    if dir == "Right":
                        temp_dist = right.manhattan_distance(ghost)
                        if directions["Right"] < temp_dist:
                            directions["Right"] = temp_dist


            print("--------------------------------CALCULATION:", directions)
            got_stuck = all([min_dist == vl for vl in directions.values()])

            # randomly delete 1 direction if more than 1 direction has value equal to max value in directions
            dup_val = 0
            d_list = []
            temp_step = max(directions.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
            for dir in directions:
                if directions[dir] == temp_step:
                    print(dir, directions[dir])
                    d_list.append(dir)
                    dup_val += 1
            if dup_val > 1:
                index = random.randrange(0, len(d_list), 1)
                del directions[d_list[index]]

            next_step = max(directions.items(), key=lambda x: x[1])[0] if not got_stuck else "Stuck"
            return next_step
        else:
            vision_path = [Level3.evaluate_coordinate(node, r1[0], r2[0]) for node in path if Level3.in_map(r1, r2, node)]
            vision_dead_nodes = [Level3.evaluate_coordinate(node, r1[0], r2[0]) for node in dead_node if Level3.in_map(r1, r2, node)]

            return Level1.level1(vision_map, vision_map.pacman_init_position, vision_path, vision_dead_nodes, True)


