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
    end_1 = current_position.x + 2 if current_position.x + 2 < map.N_row else map.N_row - 1
    start_2 = current_position.y - 2 if current_position.y - 2 >= 0 else 0
    end_2 = current_position.y + 2 if current_position.y + 2 < map.M_col else map.M_col - 1
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    vi = get_sub_list(start_1, end_1, start_2, end_2, map.maze_data)
    row_range = range(start_1, end_1 + 1)
    col_range = range(start_2, end_2 + 1)
    treats = [evaluate_point(treat, start_1, start_2) for treat in map.treats if in_map(row_range, col_range, treat.coordinate())]
    new_pos = evaluate_point(current_position, start_1, start_2)
    return Maze(len(row_range), len(col_range), vi, new_pos, treats), row_range, col_range


def find_ghost_in_vision(vision_map: Maze, current_position: Point, row_range, col_range):
    ghost_list = []

    print("Range: ", "row: ", row_range, "col: ", col_range)
    for i in row_range:
        for j in col_range:
            #print("Hi", i - row_range[0], j - col_range[0])
            #print("value: ", vision_map.maze_data[i - row_range[0]][j - col_range[0]])
            if vision_map.maze_data[i - row_range[0]][j - col_range[0]] == vision_map.MONSTER:
                ghost_list.append(Point(i, j))
    return ghost_list


def level3(map: Maze, cur_pos: Point, path: list, dead_node: list, ghost_appearance: list):
    # print ("start 1: ", start_1, "end 1:", end_1)
    # print ("start 2: ", start_2, "end 2:", end_2)
    # GHOST_ENCOUNTER = (map.N_row + map.M_col)/3
    vision_map, r1, r2 = vision(map, cur_pos)
    print("Vision Map:")
    vision_map.print_raw_data()
    print("Treats: ", [item.coordinate() for item in vision_map.treats])
    ghosts_in_vision = find_ghost_in_vision(vision_map, cur_pos, r1, r2)
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
            if can_move(map, up, path, dead_node) and (up not in ghost_appearance):
                directions["Up"] = 0
            if can_move(map, down, path, dead_node) and (down not in ghost_appearance):
                directions["Down"] = 0
            if can_move(map, left, path, dead_node) and (left not in ghost_appearance):
                directions["Left"] = 0
            if can_move(map, right, path, dead_node) and (right not in ghost_appearance):
                directions["Right"] = 0

            # being corner reset path to find a way out
            if len(directions) < 2:
                path.clear()
                if can_move(map, up, path, dead_node):
                    directions["Up"] = 0
                if can_move(map, down, path, dead_node):
                    directions["Down"] = 0
                if can_move(map, left, path, dead_node):
                    directions["Left"] = 0
                if can_move(map, right, path, dead_node):
                    directions["Right"] = 0

            for ghost in ghosts_in_vision:
                for dir in directions:
                    if dir == "Up":
                        temp_dist = up.manhattan_distance(ghost)
                        if directions["Up"] < temp_dist:
                            directions["Up"] = temp_dist
                    elif dir == "Down":
                        temp_dist = down.manhattan_distance(ghost)
                        if directions["Down"] < temp_dist:
                            directions["Down"] = temp_dist
                    elif dir == "Left":
                        temp_dist = left.manhattan_distance(ghost)
                        if directions["Left"] < temp_dist:
                            directions["Left"] = temp_dist
                    elif dir == "Right":
                        temp_dist = right.manhattan_distance(ghost)
                        if directions["Right"] < temp_dist:
                            directions["Right"] = temp_dist
                # add the place ghost appear into ghost_appearance
                if ghost not in ghost_appearance:
                    ghost_appearance.append(ghost)

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
            if can_move(map, cur_pos.up(), path, dead_node) and (up not in ghost_appearance):
                directions.append("Up")
            if can_move(map, cur_pos.down(), path, dead_node) and (down not in ghost_appearance):
                directions.append("Down")
            if can_move(map, cur_pos.left(), path, dead_node) and (left not in ghost_appearance):
                directions.append("Left")
            if can_move(map, cur_pos.right(), path, dead_node) and (right not in ghost_appearance):
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
            if can_move(map, up, path, dead_node) and (up not in ghost_appearance):
                directions["Up"] = 0
            if can_move(map, down, path, dead_node) and (down not in ghost_appearance):
                directions["Down"] = 0
            if can_move(map, left, path, dead_node) and (left not in ghost_appearance):
                directions["Left"] = 0
            if can_move(map, right, path, dead_node) and (right not in ghost_appearance):
                directions["Right"] = 0

            # being corner reset path to find a way out
            if len(directions) < 2:
                path.clear()
                if can_move(map, up, path, dead_node):
                    directions["Up"] = 0
                if can_move(map, down, path, dead_node):
                    directions["Down"] = 0
                if can_move(map, left, path, dead_node):
                    directions["Left"] = 0
                if can_move(map, right, path, dead_node):
                    directions["Right"] = 0

            for ghost in ghosts_in_vision:
                for dir in directions:
                    if dir == "Up":
                        temp_dist = up.manhattan_distance(ghost)
                        if directions["Up"] < temp_dist:
                            directions["Up"] = temp_dist
                    elif dir == "Down":
                        temp_dist = down.manhattan_distance(ghost)
                        if directions["Down"] < temp_dist:
                            directions["Down"] = temp_dist
                    elif dir == "Left":
                        temp_dist = left.manhattan_distance(ghost)
                        if directions["Left"] < temp_dist:
                            directions["Left"] = temp_dist
                    elif dir == "Right":
                        temp_dist = right.manhattan_distance(ghost)
                        if directions["Right"] < temp_dist:
                            directions["Right"] = temp_dist
                # add the place ghost appear into ghost_appearance
                if ghost not in ghost_appearance:
                    ghost_appearance.append(ghost)

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
            vision_path = [evaluate_coordinate(node, r1[0], r2[0]) for node in path if in_map(r1, r2, node)]
            vision_dead_nodes = [evaluate_coordinate(node, r1[0], r2[0]) for node in dead_node if in_map(r1, r2, node)]

            return Level1.level1(vision_map, vision_map.pacman_init_position, vision_path, vision_dead_nodes, True)


