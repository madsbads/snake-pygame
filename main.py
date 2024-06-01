import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
player = pygame.Rect((200,200,25,25))
target = pygame.Rect((300,300,25,25))
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    # draw player and target
    pygame.draw.rect(screen, (250,0,0), player)
    pygame.draw.rect(screen, (0,250,0), target)

    # RENDER YOUR GAME HERE
    # directional inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.x -= 4
    elif key[pygame.K_RIGHT] == True:
        player.x += 4
    elif key[pygame.K_UP] == True:
        player.y -= 4
    elif key[pygame.K_DOWN] == True:
        player.y += 4

    # flip() the display to put your work on screen
    pygame.display.flip()

    # fps
    clock.tick(30)  # this controls the speed of the game. low values makes the game slower, and large values makes the game faster.

pygame.quit()



# import pygame
# pygame.init()

# screen = pygame.display.set_mode((800, 800))
# clock = pygame.time.Clock()
# player = pygame.Rect((200,200,25,25))
# run = True

# while run:
    
#     screen.fill((0,0,0))
    
#     pygame.draw.rect(screen, (250,0,0), player)
    
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT] == True:
#         player.move_ip(-1,0)
#     elif key[pygame.K_RIGHT] == True:
#         player.move_ip(1,0)
#     elif key[pygame.K_UP] == True:
#         player.move_ip(0,-1)
#     elif key[pygame.K_DOWN] == True:
#         player.move_ip(0,1)
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: 
#             run = False

#     pygame.display.update()
#     clock.tick(60)
    
# pygame.quit()