import pygame
import time
pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('image')
coin1 = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\coin1.jpg')
coin2 = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\coin2.jpg')
coin3 = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\coin3.jpg')
done = False

while not done:
    screen.fill(white)
    #(screen size - side size)/2
    time.sleep(1)
    pygame.display.update()
    screen.blit(coin1,(141, 141))
    time.sleep(0.5)
    pygame.display.update()
    screen.blit(coin2,(141, 141))
    time.sleep(0.5)
    pygame.display.update()
    screen.blit(coin3,(141, 141))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()

