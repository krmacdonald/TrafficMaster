import pygame
import player


print(pygame.ver)
pygame.init()
monitors = pygame.display.get_desktop_sizes()
resolutionx, resolutiony = monitors[0]
screen = pygame.display.set_mode((resolutionx, resolutiony))
clock = pygame.time.Clock
running = True
mousePosition = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)
mouseSprite = pygame.image.load("Resources/Images/mouse.png")
imagerect = mouseSprite.get_rect()
playerMouse = player.Player(screen)


while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(playerMouse.scaledimg, pygame.mouse.get_pos())
    
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        if keys[pygame.K_ESCAPE]:
            running = False
        if mouse[0]:
            pygame.draw.rect(screen, "red", pygame.rect.Rect(100, 100, 300, 300))
        
    
    pygame.display.flip()

pygame.quit()
