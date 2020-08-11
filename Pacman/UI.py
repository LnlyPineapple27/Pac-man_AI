import math
import sys
import turtle
from Maze import *
from tkinter import messagebox
import time
import random
import Level1

EMPTY = 0
WALL = 1
TREAT = 2
MONSTER = 3
TCPS = 1  # time cost per step
GOLD = 20
DEATH_COST = 100000
DELAY_TIME = 0.5
# --------------------------------------------Initial things-----------------------------
window = turtle.Screen()
root = turtle.Screen()._root
root.iconbitmap("..\\images\\icon\\Pacman.ico")
window.bgcolor('black')
window.title('AI Pacman')
window.setup(width=1000, height=810, startx=0, starty=10)
window.tracer(0)
# --------------------------------------------------
images = ["..\\images\\gif\\Blue_left.gif",
          "..\\images\\gif\\Red_left.gif",
          "..\\images\\gif\\Pink_left.gif",
          "..\\images\\gif\\Orange_left.gif",
          "..\\images\\gif\\Blue_right.gif",
          "..\\images\\gif\\Red_right.gif",
          "..\\images\\gif\\Pink_right.gif",
          "..\\images\\gif\\Orange_right.gif",
          "..\\images\\gif\\pacman_right.gif",
          "..\\images\\gif\\pacman_left.gif",
          "..\\images\\gif\\pacman_up.gif",
          "..\\images\\gif\\pacman_down.gif",
          "..\\images\\gif\\fruit.gif"]
for img in images:
    turtle.register_shape(img)


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self, init_pos: Point = None):
        turtle.Turtle.__init__(self)
        self.position = init_pos if init_pos else Point()
        self.shape("..\\images\\gif\\pacman_right.gif")
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        print("-- Pacman go up")
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        self.shape("..\\images\\gif\\pacman_up.gif")
        if (move_to_x, move_to_y) not in walls:
            self.position.x -= 1
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        print("-- Pacman go down")
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        self.shape("..\\images\\gif\\pacman_down.gif")
        if (move_to_x, move_to_y) not in walls:
            self.position.x += 1
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        print("-- Pacman go left")
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.position.y -= 1
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        print("-- Pacman go right")
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_right.gif")
        if (move_to_x, move_to_y) not in walls:
            self.position.y += 1
            self.goto(move_to_x, move_to_y)

    def move(self, next_move: str = None):
        if next_move == "Up":
            self.go_up()
        elif next_move == "Down":
            self.go_down()
        elif next_move == "Left":
            self.go_left()
        elif next_move == "Right":
            self.go_right()
        else:
            pass

    def exit(self):
        self.goto(self.xcor(), self.ycor())

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y, num):
        turtle.Turtle.__init__(self)
        self.num = num
        self.shape('triangle')

        if self.num == 0:
            self.shape("..\\images\\gif\\Blue_left.gif")
        elif self.num == 1:
            self.shape("..\\images\\gif\\Orange_left.gif")
        elif self.num == 2:
            self.shape("..\\images\\gif\\Pink_left.gif")
        elif self.num == 3:
            self.shape("..\\images\\gif\\Red_left.gif")

        self.color("green")
        self.penup()
        self.speed(0)
        # self.gold = 25
        self.goto(x, y)
        # self.direction = random.choice(["up", "down", "right", "left"])
        self.direction_to_init = None
        self.rotate = 0

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def go_(self, direction):
        move_to_x = self.xcor()
        move_to_y = self.ycor()
        if direction == "up":
            move_to_y += 24
        elif direction == "down":
            move_to_y -= 24
        elif direction == "right":
            move_to_x += 24
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_right.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_right.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_right.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_right.gif")
        elif direction == "left":
            move_to_x -= 24
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_left.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_left.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_left.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True
        return False

    def go_backward(self, direction):
        move_to_x = self.xcor()
        move_to_y = self.ycor()
        if direction == "down":
            move_to_y += 24
        elif direction == "up":
            move_to_y -= 24
        elif direction == "left":
            move_to_x += 24
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_right.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_right.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_right.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_right.gif")
        elif direction == "right":
            move_to_x -= 24
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_left.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_left.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_left.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            return True
        return False

    def move(self):
        if self.direction_to_init == None:
            # clock-wise move-ment
            directions_list = ["up", "right", "down", "left"]
            count = 0
            i = self.rotate
            if i == 3:
                i = 0
            elif i >= 0 and i < 3:
                i += 1
            while count < 4:
                count += 1
                try_val = self.go_(directions_list[i])
                if try_val:
                    self.direction_to_init = directions_list[i]
                    break
                else:
                    if i == 3:
                        i = 0
                    elif i >= 0 and i < 3:
                        i += 1
            self.forward(0)
            self.rotate = i
        else:
            try_val = self.go_backward(self.direction_to_init)
            if not try_val:
                print("[Error]: Something went wrong in ghost's movement to get back to initial place")
            self.direction_to_init = None


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\fruit.gif")
        self.color('black')
        self.penup()
        self.speed(0)
        self.gold = GOLD
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Global variable
treasures = []
enemies = []
walls = ['']
walls_block = Wall()
player = Player()


# start position of character
def setup_maze(board, difficulty, init_index):
    player.position = init_index
    print(player.position.position())

    val_x = 400
    val_y = 350
    for i in range(len(board)):
        for j in range(len(board[i])):
            # get the character of each x,y coord

            unity = board[i][j]

            # 288
            screen_x = ((-1) * val_x) + (j * 24)
            screen_y = val_y - (i * 24)
            # printing the maze

            if unity == WALL:
                walls_block.goto(screen_x, screen_y)
                # walls_block.shape('Wall.gif')
                walls_block.stamp()
                # Add co-ordinates to list
                walls.append((screen_x, screen_y))

            if unity == TREAT:
                treasures.append(Treasure(screen_x, screen_y))

            if unity == MONSTER and difficulty != 1:
                num = len(enemies)
                enemies.append(Enemy(screen_x, screen_y, num))
    # print Player according to its given location
    player.goto(((-1) * val_x) + (player.position.y * 24), val_y - (player.position.x * 24))
    # :)
    window.update()




def score_evaluation(gold, died, total_time):
    dc = DEATH_COST if died else 0
    return gold - dc - total_time * TCPS


def endGame():
    print("[Game closed]")
    sys.exit()


def startGame(data: Maze, difficulty):
    step = 1
    start_time = time.time()
    setup_maze(data.maze_data, difficulty, data.pacman_init_position)
    """
    turtle.listen()
    turtle.onkey(player.go_up, 'Up')
    turtle.onkey(player.go_down, 'Down')
    turtle.onkey(player.go_right, 'Right')
    turtle.onkey(player.go_left, 'Left')
    """
    treats_left = len(maze.treats)
    died = False
    explored = [player.position]
    ghost = difficulty >= 1
    while treats_left or not died:
        # Time delay
        time.sleep(DELAY_TIME)

        # Check collision
        for enemy in enemies:
            if player.is_collision(enemy):
                player.gold -= DEATH_COST
                print("Player died!!")
                player.destroy()
                died = True

        # Check alive
        if not died:
            # Think next move
            next_move = Level1.level1(maze, player.position, explored, ghost)
            old_pos = player.position
            # Move
            player.move(next_move)
            new_pos = player.position
            if old_pos.position() == new_pos.position():
                explored.pop()
            explored.append(player.position.position())

            for treasure in treasures:
                if player.is_collision(treasure):
                    # Desc treats left
                    treats_left -= 1
                    # Add the treasure gold to the player gold
                    player.gold += treasure.gold
                    print('Player Gold: {}'.format(player.gold))
                    # Destroy the treasure
                    treasure.destroy()
                    # Remove the treasure
                    treasures.remove(treasure)
            # double check
            for enemy in enemies:
                if player.is_collision(enemy):
                    player.gold -= 1000
                    print("Player died!!")
                    player.destroy()
                    died = True
                if difficulty != 2:
                    enemy.move()

        # Update screen

        window.update()
        if not treats_left or died:
            print("END game")
            end_time = time.time()
            total_time = int(end_time - start_time)
            score = score_evaluation(player.gold, died, total_time)
            mesg = "You WON" if not treats_left else "You DIED"
            mesg += ", Score = {}, took {} seconds".format(score, step)
            print("[RESULT]:" + mesg)
            messagebox.showinfo("Congratulations!!!!", mesg)
            endGame()
        step += 1

    # turtle.exitonclick()
    endGame()


if __name__ == "__main__":
    input_list = InputHandle()
    input_list.items()
    maze = input_list.get_maze("lv1.txt")
    # maze.print_raw_data()
    # maze.print_entities()
    difficulty = 1
    messagebox.showinfo()
    startGame(maze, difficulty)
