import math
import sys
import turtle
from Maze import *
from tkinter import messagebox


EMPTY = 0
WALL = 1
TREAT = 2
MONSTER = 3

# --------------------------------------------Initial things-----------------------------
window = turtle.Screen()
window.bgcolor('black')
window.title('AI Pacman')
window.setup(700, 700)
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
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\pacman_right.gif")
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        self.shape("..\\images\\gif\\pacman_up.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        self.shape("..\\images\\gif\\pacman_down.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
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
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\Blue_left.gif")
        self.color("blue")
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
            self.shape("..\\images\\gif\\Blue_right.gif")
        if self.direction == "left":
            dx = -24
            dy = 0
            self.shape("..\\images\\gif\\Blue_left.gif")
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
            screen_x = -288 + (j * 24)
            screen_y = 288 - (i * 24)
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
                enemies.append(Enemy(screen_x, screen_y))
    # print Player according to its given location
    player.goto(-288 + (init_col * 24), 288 - (init_row * 24))


def startGame(data: Maze, difficulty):
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
                print("Player died!!")
                player.destroy()
                died = True
 
        # Update screen
        window.update()
        # check goal
        if not treats_left:
            messagebox.showinfo("Boom Surprise Madafaka", "You WON")
        if died:
            messagebox.showinfo("Boom Surprise Madafaka", "You DIED")
            sys.exit()


if __name__ == "__main__":
    input_list = InputHandle()
    input_list.items()
    maze = input_list.get_maze("data1.txt")
    maze.print_raw_data()
    maze.print_entities()
    difficulty = 3
    startGame(maze, difficulty)
