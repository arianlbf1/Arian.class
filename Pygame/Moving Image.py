import pygame
import time

pygame.init()

#variables:
#Colours
white = (255, 255, 255)
#Screen size
hight = 500
width = 400
screen = pygame.display.set_mode((hight, width))
done = False
pasta_x = 200
pasta_y = 200
loop = 100

#Set the name of the window
name = "image"
pygame.display.set_caption(name)

#adding an image
mario = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\Mario.png')
pasta = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\pasta.png')

#change the size of an image
pasta = pygame.transform.scale(pasta, (100, 100))

#to center an image to the screen: (Screen size - hight/width of the image) / 2

#infinite loop
while not done:
    screen.fill(white)
    #the position of the images
    screen.blit(mario,(0, 0))

    while not loop == 0:
        time.sleep(0.1)
        screen.blit(pasta,(pasta_x, pasta_y))
        pasta_y += 1
        loop -= 1
        pygame.display.update()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Exit program
            done = True
    pygame.display.update()


