import turtle
import random
import math
import sys

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
            "..\\images\\gif\\pacman_down.gif"]

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Maze Game')
wn.setup(700, 700)
wn.tracer(0)
class Pen(turtle.Turtle):
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
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        self.shape("..\\images\\gif\\pacman_down.gif")
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_left.gif")
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape("..\\images\\gif\\pacman_right.gif")
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def exit(self):
        self.goto(self.xcor(), self.ycor())
# xử lí va chạm của object Player
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

# Add obstacles
"""
class obstacle(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('triangle')
        self.color('green')
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.direction = random.choice(['left','right'])

    def move(self):
        if self.direction == 'left':
            dx = -24
            dy = 0
            self.shape('triangle')
        elif self.direction == 'right':
            dx = 24
            dy = 0
            self.shape('triangle')
        else:
            dx = 0
            dy = 0

# Calculation for motion
        move_to_x = self.xcor()+dx
        move_to_y = self.ycor()+dy
# Prevent motion into walls
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(['left','right'])
# Cause motion within given millisecond
        turtle.ontimer(self.move, t=random.randint(100,300))
"""
for img in images:
    turtle.register_shape(img)

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("..\\images\\gif\\Blue_left.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

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

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if space is a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        #Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(10, 30))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
       self.goto (2000,2000)
       self.hideturtle()

levels = ['']
treasures =[]
level_1 = [
    '111111111111111111111111',
    '1P1111111  E      111111',
    '1  1111111   11111111111',
    '1  1111111   11111111111',
    '1   2                111',
    '11111111111111111   1111',
    '111         2 2 2   1111',
    '111111111111111111111111',
]




# Add level 1 to maze list
levels.append(level_1)
enemies = []
walls=['']

# start position of character
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # get the character of each x,y coord

            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
# printing the maze
            # X for wall
            if character == '1':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add co-ordinates to list
                walls.append((screen_x,screen_y))
            # P for player
            if character == 'P':
                player.goto(screen_x, screen_y)
            # T for Treasure
            if character == '2':
                treasures.append(Treasure(screen_x, screen_y))

            #Check if it is a E(Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
            """
            if character == 'O':
                # Print obstacles
                # Add to list of obstacles
                obstacles.append(obstacle(screen_x, screen_y))
            """
pen = Pen()
player = Player()

#Add obstacles to a list
# obstacles = []

setup_maze(levels[1])

#Initiate motion of the obstacles
"""
for obstacle in obstacles:
    turtle.ontimer(obstacle.move, t=200)
"""

# Keyboard binding
turtle.listen()
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_left,'Left')
#turtle.exitonclick()

"""
# Collision with obstacle
if player.xcor() == obstacle.xcor():
    print('Player is dead! Restart Now or Click the Screen to Exit.')
        #restart game
    turtle.update
"""
#wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)
#Main game loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print ('Player Gold: {}'.format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print ("Player dies!!")
            sys.exit()
    #Update screen
    wn.update()

