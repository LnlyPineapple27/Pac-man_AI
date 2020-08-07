'''
wall = 1
food = 2
monster = 3
empty path = 0
'''


class Maze:

    def __init__(self):
        self.N_row = 0
        self.M_col = 0
        self.maze_data = []  # list of list, n list , each list contain m element
        self.pacman_index = [] # where pacman is at the beginning

    def __init__(self, m_row, m_col, m_data, m_p_index):
        self.N_row = m_row
        self.M_col = m_col
        self.maze_data = m_data
        self.pacman_index = m_p_index

    def print_data(self):
        print("Data: ")
        for i in self.maze_data:
            print(i)


def readfile(file_des):
    with open(file_des, 'r') as file:
        lines = file.readlines()

        tmp = lines.pop(0)
        tmp = tmp.rstrip('\n')
        tmp = tmp.split(" ")
        print(tmp)
        m_col = int(tmp.pop())
        n_row = int(tmp.pop())

        tmp = lines.pop()
        tmp = tmp.rstrip('\n')
        tmp = tmp.split(" ")
        p_man = tmp

        data = []
        for line in lines:
            line = line.rstrip('\n')
            line = line.split(" ")
            tmp = []
            for i in line:
                tmp.append(int(i))
            data.append(tmp)

    return n_row, m_col, data, p_man


if __name__ == "__main__":
    row, col, data, p_index = readfile("..\\input\\data1.txt")
    maze_1 = Maze(row, col, data, p_index)
    print("Size: \tRow:", maze_1.N_row, " Col:", maze_1.M_col)
    #print("Data: ", maze_1.maze_data)
    maze_1.print_data()
    print("Pacman: ", maze_1.pacman_index)

