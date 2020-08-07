import os
import random
#from UI import startGame


INPUT_DIR = "..\\input"
EMPTY = 0
WALL = 1
TREAT = 2
MONSTER = 3
ENTITY_NAME = ["Empty", "Wall", "Treat", "Monster"]


class Maze:
    def __init__(self, m_row=0, m_col=0, m_data=None, m_p_index=None):
        self.N_row = m_row
        self.M_col = m_col
        self.maze_data = m_data
        self.pacman_init_position = m_p_index

    def print_raw_data(self):
        for i in self.maze_data:
            print(i)

    def print_entities(self) -> None:
        """
        Print all entities by name. \n
        :return: None
        """
        for row in self.maze_data:
            for ent in row:
                print(ENTITY_NAME[row[ent]], end="\t")
            print("\n")


class InputHandle:
    """
    Store all of input file path
    """
    def __init__(self, input_dir=INPUT_DIR):
        self.path_list = {}
        with os.scandir(input_dir) as i:
            for entry in i:
                if entry.is_file():
                    self.path_list[entry.name] = input_dir + '\\' + entry.name

    def items(self) -> None:
        """
        List item read.\n
        item\t\t|\tpath.\n
        :return:
        """
        print("Item\t\t|\tPath")

        for item in self.path_list.items():
            print(item[0] + "\t|\t" + item[1])


    def get_maze(self, file_name: str = None) -> Maze:
        """
        Just get a maze from item in list of input.
        Random maze in input's item if null argument or wrong name.\n
        :param file_name: Name of item to get maze
        :return: A Maze
        """
        # choices random item if file name is null
        file_path = self.path_list[file_name] if file_name and file_name in self.path_list.keys()\
                                            else random.choices(list(self.path_list.values())).pop()
        with open(file_path, 'r') as file:
            lines = file.readlines()
            '''
            tmp = lines.pop(0)
            tmp = tmp.rstrip('\n')
            tmp = tmp.split(" ")
            print(tmp)
            m_col = int(tmp.pop())
            n_row = int(tmp.pop())
            '''
            # First line includes N, M as "N M"
            tokens = lines.pop(0).split(" ")  # tokens = ["N", "M"]
            n_row, m_col = int(tokens[0]), int(tokens[1])

            # Last line includes x, y as "x y"
            tokens = lines.pop().split(" ")  # tokens = ["x", "y"]
            p_man = int(tokens[0]), int(tokens[1])

            # Data reading
            '''
            for line in lines:
                line = line.rstrip('\n')
                line = line.split(" ")
                tokens = []
                for i in line:
                    tokens.append(int(i))
                m_data.append(tokens)
            '''
            m_data = [[int(i) for i in tokens.split(" ")] for tokens in lines]

        return Maze(n_row, m_col, m_data, p_man)

