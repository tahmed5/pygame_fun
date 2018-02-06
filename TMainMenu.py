import PyInstaller
import pygame
import os
import subprocess
'''import profile'''
import importlib.util

width, height = 1000,800
pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Main Menu')

fps = pygame.time.Clock()

MainMenu = pygame.image.load('MainMenuDesign.jpg')
snake_img = pygame.image.load('SNAKE.png')
snake_low = pygame.image.load('SNAKELOW.png')
pacman_img = pygame.image.load('PACMAN.png')
pacman_low =pygame.image.load('PACMANLOW.png')
run_img = pygame.image.load('RUN.png')
run_low = pygame.image.load('RUNLOW.PNG')
tetris_img = pygame.image.load('TETRIS.png')
tetris_low = pygame.image.load('TETRISLOW.png')
spaceinvaders_img = pygame.image.load('SPACEINVADERS.png')
spaceinvaders_low = pygame.image.load('SPACEINVADERSLOW.png')

#editted by Miles Burne 1/2/18 to add reciver functionality in the launching and closing of tetris and pacman
import getpass #to get the user's name

#ADDED
#function to recieve the file on the other end, needs an input of the game name ("pacman","tetris")
#FUNCTION TAKES LOWER CASE NAMES

def reciever(game):
    username = (getpass.getuser()).lower() #I found an issue where if the user logs in with caps enabled, the username will be all caps in program. Not a big deal but may as well solve it.
    user_profile = profile.User_Profile(username) #getting user profile
    filename = (str(username)+"_"+str(game)+".esp") #getting filename
    f = open(filename, "r")
    content = f.read()
    content = content.split("\n") #file now split into number of records
    content.pop(len(content)-1) #removing the '\n' character
    for x in content:
        x = x.split(",") #now split into [score, game]
        user_profile.update_score(x[0])# updating the score
        user_profile.add_game_record(game)
        user_profile.save()
     
    

def pacman():
    reciever('pacman')
    

def run():
    spec = importlib.util.spec_from_file_location("main.py", "Z:\My Documents\Sixth Form\Computer Science\main.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.MyClass()
    '''subprocess.call('main.py', shell = True)'''
    '''os.system('main.py')'''

def space_invaders():
    print('SpaceInvaders')

def tetris():
    subprocess.call('main.py', shell = True)
    reciever('tetris')


def snake():
    pass

def menu_animation():
    finished_animation = False
    shift = 400
    while shift > -20:
        window.blit(MainMenu,[0,0])
        window.blit(run_img, [100 - shift,346])
        window.blit(spaceinvaders_img, [589 + shift,324])
        window.blit(tetris_img,[600 + shift,512])
        window.blit(snake_img, [92 - shift,525])
        window.blit(pacman_img, [298,649 + shift])
        pygame.display.update()
        shift -= 20
    
    
def main():
    menu_animation()
    y = 0
    while True:
        window.blit(MainMenu,[0,0]) 
        hover = False
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #x + width > mouse_x > x and y + height > mouse_y > y
        #run

        if 100 + 352 > mouse[0] > 100 and 346 + 85 > mouse[1] > 346:
            window.blit(run_low, [100,346])
            hover = True
            if click[0] == 1:
                run()

        #tetris
        if 600 + 282 > mouse[0] > 600 and 512 + 94 > mouse[1] > 512:
            window.blit(tetris_low, [600,512])
            hover = True
            if click[0] == 1:
                tetris()        
        #pacman   
        if 298 + 405 > mouse[0] > 298 and 649 + 69 > mouse[1] > 649:
            window.blit(pacman_low, [298,649])
            hover = True
            if click[0] == 1:
                pacman()
        
        #spaceinvasders 
        if 589 + 306 > mouse[0] > 589 and 324 + 137 > mouse[1] > 324:
            window.blit(spaceinvaders_low, [589,324])
            hover = True
            if click[0] == 1:
                space_invaders()
                
        #snake
        if 92 + 373 > mouse[0] > 92 and 525 + 71 > mouse[1] > 525:
            window.blit(snake_low, [92,525])
            hover = True
            if click[0] == 1:
                snake()
    
        if hover != True:
            window.blit(run_img, [100,346])
            window.blit(spaceinvaders_img, [589,324])
            window.blit(tetris_img,[600 ,512])
            window.blit(snake_img, [92 ,525])
            window.blit(pacman_img, [298,649])
     
        pygame.display.update()
                
            
        

    
main()
    
    
    
