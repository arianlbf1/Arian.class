import pygame

pygame.init()

#variables:
#Colours
white = (255, 255, 255)
#Screen size
hight = 500
width = 400
screen = pygame.display.set_mode((hight, width))
#other things
done = False

#Set the name of the window
name = "image"
pygame.display.set_caption(name)

#adding an image
mario = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\Mario.png')
pasta = pygame.image.load(r'C:\Users\youno\OneDrive\Desktop\pygame\pasta.png')

#change the size of an image
pasta = pygame.transform.scale(pasta, (200, 200))

#to center an image to the screen: (Screen size - hight/width of the image) / 2

#infinite loop
while not done:
    screen.fill(white)
    #the position of the images
    screen.blit(mario,(0, 0))
    screen.blit(pasta,(250, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Exit program
            done = True
    pygame.display.update()