import math
import sys
import turtle
from Maze import *
from tkinter import messagebox
import time


EMPTY = 0
WALL = 1
TREAT = 2
MONSTER = 3
TCPS = 10  # time cost per sec
DEATH_COST = 1000
# --------------------------------------------Initial things-----------------------------
window = turtle.Screen()
window.bgcolor('black')
window.title('AI Pacman')
window.setup(width = 1000, height = 800, startx = 0, starty = 10)
window.tracer(0, 0)
turtle.ht()
turtle.speed(0)

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
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\pacman_right.gif")
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        print("Pacman go up")
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        self.shape("..\\images\\gif\\pacman_up.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        print("Pacman go down")
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        self.shape("..\\images\\gif\\pacman_down.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        print("Pacman go left")
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        print("Pacman go right")
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_right.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

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
        self.direction = random.choice(["up", "down", "right", "left"])
        # "up", "down",

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        if self.direction == "down":
            dx = 0
            dy = -24
        if self.direction == "right":
            dx = 24
            dy = 0
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_right.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_right.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_right.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_right.gif")
        if self.direction == "left":
            dx = -24
            dy = 0
            if self.num == 0:
                self.shape("..\\images\\gif\\Blue_left.gif")
            elif self.num == 1:
                self.shape("..\\images\\gif\\Orange_left.gif")
            elif self.num == 2:
                self.shape("..\\images\\gif\\Pink_left.gif")
            elif self.num == 3:
                self.shape("..\\images\\gif\\Red_left.gif")
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = 'left'
            if player.xcor() > self.xcor():
                self.direction = 'right'
            if player.ycor() < self.ycor():
                self.direction = 'down'
            if player.ycor() > self.ycor():
                self.direction = 'up'
        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if space is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        # Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(10, 30))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\fruit.gif")
        self.color('black')
        self.penup()
        self.speed(0)
        self.gold = 100
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

    init_col = init_index[0]
    init_row = init_index[1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            # get the character of each x,y coord

            unity = board[i][j]
            val_x = 400
            val_y = 350
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
    player.goto(((-1) * val_x) + (init_col * 24), val_y - (init_row * 24))


def score_evaluation(gold, died, total_time):
    dc = DEATH_COST if died else 0
    return gold - dc - total_time * TCPS


def startGame(data: Maze, difficulty):

    try:
        start_time = time.time()
        setup_maze(data.maze_data, difficulty, data.pacman_init_position)
        turtle.listen()
        turtle.onkey(player.go_up, 'Up')
        turtle.onkey(player.go_down, 'Down')
        turtle.onkey(player.go_right, 'Right')
        turtle.onkey(player.go_left, 'Left')

        # Initiate motion of the enemies
        for enemy in enemies:
            turtle.ontimer(enemy.move, t=250)

        treats_left = len(treasures)
        died = False
        while treats_left or not died :
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

            for enemy in enemies:
                if player.is_collision(enemy):
                    player.gold -= 1000
                    print("Player died!!")
                    player.destroy()
                    died = True

            # Update screen
            window.update()
            # check goal
            if not treats_left or died:
                print("END game")
                end_time = time.time()
                total_time = int(end_time - start_time)
                score = score_evaluation(player.gold, died, total_time)
                mesg = "You WON" if not treats_left else "You DIED"
                mesg += ", Score = {}, took {} seconds".format(score, total_time)
                messagebox.showinfo("Boom Surprise Madafaka", mesg)
                sys.exit()

        turtle.exitonclick()
    except Exception:
        pass
    finally:
        print("[Game closed]")

if __name__ == "__main__":
    input_list = InputHandle()
    input_list.items()
    maze = input_list.get_maze("walls.txt")
    # maze.print_raw_data()
    # maze.print_entities()
    difficulty = 3
    startGame(maze, difficulty)
