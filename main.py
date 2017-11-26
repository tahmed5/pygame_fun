import pygame
import random
import sys
import time

width,height = 800,600
pygame.init()
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
gameloop = True
board = pygame.display.set_mode((width,height)) #Creates the board
pygame.display.set_caption("Robot Game") #Used to set the title of the board window
smoothx,smoothy = 0,0 # SmoothX and SmoothY will be added to the player coordinates to allow constant motion when a user clicks one of the arrow keys
fps = pygame.time.Clock() #A pygame function that is used to control the amount of cycles per second
level = 1
scoreboard = 0
num_scrap = 0


class user:    
    def __init__(self,x,y):
        self.lives = 3 #Amount of lives the user has 
        self.x = x #Players x coordinate
        self.y = y #Players y coordinate
        self.width = 10 #Player Sprite Width
        self.height = 10 #Player Sprite Height
        
    def draw(self):
        #This restricts the user from leaving the board as it constantly updates the user coordinates to the edge values
        if self.x <= 0:
            self.x = 0 + (self.width/2)
        if self.x >= width - self.width:
            self.x = width - (self.width)
        if self.y <= 0:
            self.y = 0 + (self.height/2)
        if self.y >= height - self.height:
            self.y = height - (self.height)
        #Applies smoothx and smoothy to the player coordinates so the player can move when a user holds down a key
        self.x += smoothx
        self.y += smoothy
        pygame.draw.rect(board,white,(self.x,self.y,self.width,self.height)) #Displays the user sprite

    def lives(self):
        #Used to check and update the lives of a user
        if self.lives != 0: #If the lives of the player are not 0 it minuses one as this function is triggered when a collision occurs with a bot
            self.lives -= 1
        #This will send each bot to the remove_bots method in the robot class
        for bot in bots:
            robot.remove_bots(bot)
        if self.lives == 0:
            gameloop = False #Stop the gameloop if the user no longer has any lives
        lives_remaining()        
        
        

player = user(int(width/2),int(height/2)) #Creates a user instance

class robot:
    def __init__(self):
        self.id = 'robot'
        #x and y are randomly generated
        x = list(range(0, width))
        y = list(range(0,height))
        safe_x = []
        safe_y = []
        for number in x:
            if number not in range(300,600):
                safe_x.append(number)
        for number in y:
            if number not in range(150,450):
                safe_y.append(number)
        self.x = random.choice(safe_x) #x is assigned from outside the safe radius)
        self.colour = red # Sets the colours of bots to red        
        self.y = random.choice(safe_y)#y is assigned from outside the safe radius
        self.ground = False # Ground is used to make a bot stationary when it turns into a scrap pile
        self.width = 10
        self.height = 10

    def draw_bots(self):
        #Displays the bots
        pygame.draw.rect(board,self.colour,(self.x,self.y,self.width,self.height))
    
    def remove_bots(self):
        #Removes the bots when the player collides with a robot and then it calls the function generate_bots to replace them with new ones
        del bots[:]
        generate_bots()
        
    def pathfinding(self):
        #Compares the x values and y values with the player and moves towards it accordingly
        #E.G playerx = 5 botx = 2 if playerx > botx botx +=1
        if self.x <= 0:
            self.x = 0 + (self.width/2)
        if self.x >= width - self.width:
            self.x = width - (self.width)
        if self.y <= 0:
            self.y = 0 + (self.height/2)
        if self.y >= height - self.height:
            self.y = height - (self.height)   
        if self.ground != True:
            if player.x > self.x:
                self.x += 2
            if player.x < self.x:
                self.x -= 2
            if player.y > self.y:
                self.y += 2
            if player.y < self.y:
                self.y -= 2
                
    def scrap_pile(self,other):
        global num_scrap
        self.ground = True #Makes the bot stationary
        self.colour = blue #Makes the scrap pile blue
        if other in bots:
            bots.remove(other)  #Removes one of the bots when two collide together so one scrap pile is created     
        pygame.draw.rect(board,blue,(self.x,self.y,self.width,self.height)) #Outputs the scrap pile
        self.id = 'scrap'

        
class collision:
    def __init__():
        super().__init__()
        
    def bot_collision_detection(self, other):
        collision_detected = False
        #checks each region of the bot to see if it collided with another bot
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x + self.width >= other.x and other.y + other.height >= self.y >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y + self.height >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x + self.width>= other.x and other.y + other.height >= self.y  + self.height >= other.y:
            collision_detected = True
        if collision_detected == True:
            robot.scrap_pile(self,other)
            
    def user_collision_detection(self, other):
        #checks each region of the bot to see if it collided with another bot
        collision_detected = False
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x + self.width >= other.x and other.y + other.height >= self.y >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y + self.height >= other.y:
            collision_detected = True
        if other.x + other.width >= self.x + self.width>= other.x and other.y + other.height >= self.y  + self.height >= other.y:
            collision_detected = True
        if collision_detected == True:
            user.lives(self)

def generate_bots():
    player.x, player.y =int(width/2),int(height/2) #updates the player position back to the centre 
    global bots
    if level == 1:
        bots = [robot() for x in range(5)] #Creates 5 bot instances when level is 0
    if level == 2:
        bots = [robot() for x in range(10)] #Creates 10 bot instances when level is 1
    if level == 3:
        bots = [robot() for x in range(15)] #Creates 10 bot instances when level is 1
    if level == 4:
        bots = [robot() for x in range(20)] #Creates 10 bot instances when level is 1


generate_bots()

font = pygame.font.SysFont('Verdana', 15) #Assigns the font verdana when displaying the score


def score(score):
    #Displays the Score
    text = font.render('Score: ' + str(score), True, white)
    board.blit(text, [0,0])

def save_score():
    #Write a file into the student shared area with their username and score   
    pass

def display_lives():
    #Displays the Lives
    text = font.render('Lives: ' + str(player.lives), True, white)
    board.blit(text, [0, 15])

countdownfont = pygame.font.SysFont('Verdana', 15)

def countdown():
    for x in range(3, 0, -1):
        board.fill(black)
        text = countdownfont.render('Level ' + str(level), True, white)
        numbers = countdownfont.render('Starting In ' + str(x), True, white)
        board.blit(text, [width/2- 50, height/2 - 50])
        board.blit(numbers, [width/2- 70, height/2 - 25])
        pygame.display.flip()        
        time.sleep(1)

def lives_remaining():
    board.fill(black)
    text = font.render('Lives Remaining: ' + str(player.lives), True, white)
    board.blit(text, [width/2- 90, height/2 - 50])
    pygame.display.flip()        
    time.sleep(3)

countdown()        
    
    
#MAIN GAME LOOP
while gameloop == True:
    num_scraps = 0
    fps.tick(60) #Sets FPS to 60
    for event in pygame.event.get(): #Checks each event
        if event.type == pygame.QUIT: #If one of the events are quit (when the user clicks the X in the top right corner) the window closes
            pygame.quit()
        if event.type == pygame.KEYDOWN: #Checks for a keypress
            if event.key == pygame.K_UP:
                smoothy -= 5 #reduces the y by 5 so player moves up
            if event.key == pygame.K_DOWN:
                smoothy += 5 #increases the y by 5 so player moves down
            if event.key == pygame.K_LEFT:
                smoothx -= 5 #reduces the x by 5 so player moves left
            if event.key == pygame.K_RIGHT:
                smoothx += 5 #increases the x by 5 so player moves right

        if event.type == pygame.KEYUP:
            #If the user stop pressing one of the arrow keys it sets all the smooth values to 0 so it stops increasing the x or y coordinate
            if event.key == pygame.K_UP:
                smoothy = 0
            if event.key == pygame.K_DOWN:
                smoothy = 0 
            if event.key == pygame.K_LEFT:
                smoothx = 0
            if event.key == pygame.K_RIGHT:
                smoothx = 0
        
    board.fill(black) #Fills the board with black
    for bot in bots:
        #For every bot it draws it and runs the pathfinding function to move towards the user
        robot.draw_bots(bot)
        robot.pathfinding(bot)
        #Checks for collisions between bots and bots as well as user and bots
        for x in bots:
            if bot != x:
                collision.bot_collision_detection(bot,x)
                collision.user_collision_detection(player,x)
    scoreboard += 1 #Adds one to the scoreboard each time
    score(scoreboard)
    display_lives()
    for bot in bots:
        if bot.id == 'scrap':
            num_scraps += 1
    if num_scraps == len(bots):
        level += 1
        generate_bots()
        countdown()
                
    player.draw()
    pygame.display.update()

print('Thank You For Playing')
save_score()
pygame.quit()
            
