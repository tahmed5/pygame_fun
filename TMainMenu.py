import pygame
import os

width, height = 800,600
pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Main Menu')

fps = pygame.time.Clock()
MainMenu = pygame.image.load('MainMenu.jpg')

def pacman():
    print('Pacman')

def run():
    os.system('main.py')
    pass

def space_invaders():
    print('SpaceInvaders')
    pass

def tetris():
    print('Tetris')
    pass

while True:    
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #x + width > mouse_x > x and y + height > mouse_y > y
    #pacman
    if 228 + 352 > mouse[0] > 228 and 55 + 60 > mouse[1] > 55:
        #display translucent logo with text
        if click[0] == 1:
            pacman()

    #tetris
    if 228 + 352 > mouse[0] > 228 and 171 + 104 > mouse[1] > 171:
        #display translucent logo with text
        if click[0] == 1:
            tetris()        
    #run   
    if 228 + 352 > mouse[0] > 228 and 305 + 105 > mouse[1] > 305:
        #display translucent logo with text
        if click[0] == 1:
            run()
            
    #spaceinvasders 
    if 228 + 352 > mouse[0] > 228 and 427 + 60 > mouse[1] > 427:
        #display translucent logo with text
        if click[0] == 1:
            space_invaders()    
        
    window.blit(MainMenu, [0,0])
    pygame.display.update()

    

    
    
    
