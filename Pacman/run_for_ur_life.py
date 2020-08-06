import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
DELAY = 60
#default locations for Pacman and monstas
w = 303-16 #Width
p_h = (7*60)+19 #Pacman height
m_h = (4*60)+19 #Monster height
b_h = (3*60)+19 #Binky height
i_w = 303-16-32 #Inky width
c_w = 303+(32-16) #Clyde width
WALL_THICKNESS = 6
CELL_EDGE = 60
TEST_CASE = 10

def display_window_evaluation(N:int, M:int)->(int,int):
    addition = WALL_THICKNESS * 2
    return N * CELL_EDGE + addition, M * CELL_EDGE + addition


if __name__ == '__main__':
    # init pygame
    pygame.init()

    # store display mode
    window_size = display_window_evaluation(TEST_CASE, TEST_CASE)
    gameDisplay = pygame.display.set_mode((window_size))
    gameDisplay.fill(BLACK)

    # Set the title of the window
    pygame.display.set_caption('AI Pacman')

    # Create a surface we can draw on
    background = pygame.Surface(gameDisplay.get_size())

    # Used for converting color maps and such
    background = background.convert()

    # Fill the screen with a black background
    background.fill(BLUE)

    # for delay timing
    clock = pygame.time.Clock()
    # game main loop
    crashed = False
    goal_state = False
    while not crashed and not goal_state:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(DELAY)

    pygame.quit()