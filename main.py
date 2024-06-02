import pygame
import random

# pygame setup
pygame.init()
running = True
lastKey = None
speed_level = 10
SIZE = 800
PXL = 25
score = 0
score_text = '0'
font = pygame.font.Font(pygame.font.get_default_font(), 36)
screen = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()
player = pygame.Rect((random.randrange(SIZE-50),random.randrange(SIZE-50),PXL,PXL)) # starting position is random on screen with 50 px margin
food = pygame.Rect((random.randrange(SIZE-50),random.randrange(SIZE-50),PXL,PXL)) # starting position is random on screen with 50 px margin

# FUNCTIONS
def generateMeal():
    food = pygame.Rect((random.randrange(SIZE-50),random.randrange(SIZE-50),PXL,PXL)) # starting position is random on screen with 50 px margin
    return food
    
def lunch(): 
    if pygame.Rect.colliderect(player, food):
        return True
    else: return False

def speedControl(current_speed):
    speed = current_speed + 4
    return speed

def grow(player):
    player.inflate_ip(PXL,0)
    return player

# GAME LOOP
while running:
    
    # dec variables
    key = pygame.key.get_pressed()
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            lastKey = event.key

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    text_surface = font.render(score_text, True, (0, 0, 250))
    screen.blit(text_surface, dest=(0,0))

    # RENDER YOUR GAME HERE
    # directional inputs
    if lastKey == pygame.K_LEFT:
         player.x -= speed_level
    elif lastKey == pygame.K_RIGHT:
        player.x += speed_level
    elif lastKey == pygame.K_UP:
        player.y -= speed_level
    elif lastKey == pygame.K_DOWN:
        player.y += speed_level
    
    # detect meal
    eat = lunch()
    if eat:
        food = generateMeal()
        score += 1
        score_text = str(score)
        player = grow(player)
        if score % 5 == 0: 
            speed_level = speedControl(speed_level) # speed of player increases as score climbs; 5 level step
        
    # draw player and target
    pygame.draw.rect(screen, (250,0,0), player)
    pygame.draw.rect(screen, (0,250,0), food)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # fps
    clock.tick(30)  # this controls the speed of the game. low values makes the game slower, and large values makes the game faster.

# quit when game loop is exited
pygame.quit()