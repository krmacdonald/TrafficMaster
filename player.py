import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/Images/mouse.png")
        self.image.set_colorkey((255, 255, 255))
        self.size = self.image.get_size()
        self.scaledimg = pygame.transform.scale(self.image, (int(self.size[0]/8), int(self.size[1]/8)))
        screen.blit(self.scaledimg, pygame.mouse.get_pos())

    def update(self, screen, coordinates):
        screen.blit(self.scaledimg, coordinates)
