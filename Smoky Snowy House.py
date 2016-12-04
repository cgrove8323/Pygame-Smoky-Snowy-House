# Imports
import pygame
import math
import random
# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Smoky Snowy House"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (93, 242, 67)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
PINK = (255, 0, 225)
TIEL = (55, 252, 242)
GREY = (69, 72, 76)
SKY_BLUE = (153, 236, 255)
SUN = (255, 255, 40)
BROWN = (119, 62, 9)
TREE = (50, 109, 23)
STAR = (255, 255, 255)
SHINING_STAR = (255, 255, 0)
SNOWMAN = (242, 245, 249)

smoke = []
for s in range(20):
    x = s * 50 + 150
    smoke.append(x)

def make_snow(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 10, 10])

def shining_star():
        pygame.draw.polygon(screen, SHINING_STAR, [[400, 325], [425, 325], [412.5, 310]])
        pygame.draw.polygon(screen, SHINING_STAR, [[385, 325], [412.5, 325], [412.5, 340]])
        pygame.draw.polygon(screen, SHINING_STAR, [[412.5, 325], [412.5, 340], [440, 325]])
        pygame.draw.polygon(screen, SHINING_STAR, [[390, 350], [400, 330], [412.5, 340]])
        pygame.draw.polygon(screen, SHINING_STAR, [[412.5, 340], [435, 350], [425, 330]])
        pygame.draw.line(screen, SHINING_STAR, [370, 370], [385, 355], 5)
        pygame.draw.line(screen, SHINING_STAR, [365, 305], [380, 320], 5)
        pygame.draw.line(screen, SHINING_STAR, [460, 305], [445, 320], 5)
        pygame.draw.line(screen, SHINING_STAR, [455, 370], [440, 355], 5)

def make_frosty():
    pygame.draw.line(screen, BROWN, [605, 385], [590, 385], 5)
    pygame.draw.line(screen, BROWN, [695, 385], [725, 420], 5)
    pygame.draw.ellipse(screen, SNOWMAN, [600, 400, 100, 75])
    pygame.draw.ellipse(screen, SNOWMAN, [605, 355, 90, 65])
    pygame.draw.ellipse(screen, SNOWMAN, [610, 315, 80, 55])
    pygame.draw.ellipse(screen, BLACK, [630, 325, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [655, 325, 15, 15])
    pygame.draw.line(screen, ORANGE, [648, 335], [665, 345], 5)
    pygame.draw.ellipse(screen, BLACK, [620, 345, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [630, 350, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [640, 355, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [650, 355, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [660, 355, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [670, 350, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [680, 345, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [640, 375, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [640, 410, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [640, 435, 20, 20])
    
'''make snow'''
snow = []
for i in range (200):
    x = random.randrange(0, 800)
    y = random.randrange(-600, 0)
    snow.append([x, y])
starshine = False
hello = False
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                starshine = not starshine
            elif event.key == pygame.K_h:
                hello = not hello
            else:
                pass
        else:
            pass
    
    '''pressed = pygame.key.get_pressed'''


    # Game logic (Check for collisions, update points, etc.)
    ''' move smoke ''' 
    smoke = [s + 1 if s < 800 else 150 for s in smoke]

    '''snow fall'''
    for n in snow:
        n[1] += 1
        if n[1] == 535:
            n[0] = random.randrange(0, 800)
            n[1] = random.randrange(-600, 0)


            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])
    pygame.draw.ellipse(screen, SUN, [700, 0, 100, 100])
    for s in smoke:
        x = s
        y = 15 *(0-1) * (math.sqrt(x - 25)) + 450
        
        pygame.draw.ellipse(screen, GREY, [x, y, 25, 25])
    if s == 850:
        x = s[2]
    '''house'''
    pygame.draw.rect(screen, RED, [50, 375, 150, 150])
    pygame.draw.rect(screen, GREEN, [105, 450, 40, 75])
    pygame.draw.ellipse(screen, RED, [135, 487.5, 8, 8])
    pygame.draw.rect(screen, RED, [150, 295, 25, 50])
    pygame.draw.polygon(screen, GREEN, [[45, 375], [205, 375], [125, 275]])
    pygame.draw.rect(screen, GREEN, [70, 400, 25, 25])
    pygame.draw.rect(screen, GREEN, [155, 400, 25, 25])
    '''tree'''
    pygame.draw.rect(screen, BROWN, [400, 500, 25, 25])
    pygame.draw.polygon(screen, TREE, [[350, 500], [475, 500], [412.5, 400]])
    pygame.draw.polygon(screen, TREE, [[360, 450], [465, 450], [412.5, 350]])
    pygame.draw.polygon(screen, TREE, [[370, 400], [455, 400], [412.5, 325]])
    pygame.draw.ellipse(screen, RED, [375, 480, 10, 10])
    pygame.draw.ellipse(screen, RED, [440, 480, 10, 10])
    pygame.draw.ellipse(screen, RED, [408, 460, 10, 10])
    pygame.draw.ellipse(screen, RED, [435, 430, 10, 10])
    pygame.draw.ellipse(screen, RED, [380, 430, 10, 10])
    pygame.draw.ellipse(screen, RED, [408, 410, 10, 10])
    pygame.draw.ellipse(screen, RED, [385, 380, 10, 10])
    pygame.draw.ellipse(screen, RED, [430, 380, 10, 10])
    pygame.draw.ellipse(screen, RED, [408, 360, 10, 10])
    '''star'''
    if starshine == True:
        STAR = SHINING_STAR
        shining_star()
    else:
        STAR = (255, 255, 255)
    pygame.draw.polygon(screen, STAR, [[400, 325], [425, 325], [412.5, 310]])
    pygame.draw.polygon(screen, STAR, [[385, 325], [412.5, 325], [412.5, 340]])
    pygame.draw.polygon(screen, STAR, [[412.5, 325], [412.5, 340], [440, 325]])
    pygame.draw.polygon(screen, STAR, [[390, 350], [400, 330], [412.5, 340]])
    pygame.draw.polygon(screen, STAR, [[412.5, 340], [435, 350], [425, 330]])

    for n in snow:
        make_snow(n[0], n[1])
    '''snowman'''
    make_frosty()
    if hello == True:
        pygame.draw.line(screen, BROWN, [590, 385], [600, 350], 5)
    else:
        pygame.draw.line(screen, BROWN, [590, 385], [575, 350], 5)
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
