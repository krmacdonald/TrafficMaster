import pygame
print(pygame.ver)
pygame.init
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock
running = True
mousePosition = pygame.mouse.get_pos

while running:
    screen.fill("black")
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.circle(screen, "red", (mouseX, mouseY), 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

roaddata = [[]]
trafficTypes = ["Road", "Stoplight", "Pedestrian Crossing", "Stop Sign"]
import roads

def printLanes():
    for i in roaddata:
        print(i)

def randomRoadData():
    for i in roaddata:
        for j in i:
            j.Randomize()