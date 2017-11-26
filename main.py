import pygame
import random

width,height = 800,600
pygame.init()
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
gameloop = True
board = pygame.display.set_mode((width,height))
pygame.display.set_caption("Robot Game")


class user:
    def __init__(self,x,y):
        self.bots = []
        self.bots.append(self)
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        
    def draw(self):
        if self.x <= 0:
            self.x = 0 + (self.width/2)
        if self.x >= width - self.width:
            self.x = width - (self.width)
        if self.y <= 0:
            self.y = 0 + (self.height/2)
        if self.y >= height - self.height:
            self.y = height - (self.height)            
        print(self.x)
        print(self.y)
        self.x += smoothx
        self.y += smoothy
        pygame.draw.rect(board,white,(self.x,self.y,self.width,self.height))

player = user(int(width/2),int(height/2))

class robot:
    def __init__(self):
        x = list(range(0, width))
        y = list(range(0,height))
        for i in range(10):
            x.pop(player.x - i)
            x.pop(player.x + i)
        for i in range(10):
            y.pop(player.y - i)
            y.pop(player.y + i)        
            
        self.x = random.choice(x)
        self.colour = red        
        self.y = random.choice(y)
        self.ground = False
        self.width = 10
        self.height = 10

    def generate_bots(self):
        pygame.draw.rect(board,self.colour,(self.x,self.y,self.width,self.height))

    def pathfinding(self):
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
        self.ground = True
        self.colour = blue
        if other in bots:
            bots.remove(other)        
        pygame.draw.rect(board,blue,(self.x,self.y,self.width,self.height))

        
class collision:
    def __init__():
        super().__init__()
        
    def bot_collision_detection(self, other):
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y >= other.y:
            robot.scrap_pile(self,other)
        if other.x + other.width >= self.x + self.width >= other.x and other.y + other.height >= self.y >= other.y:
            robot.scrap_pile(self,other)
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y + self.height >= other.y:
            robot.scrap_pile(self,other)
        if other.x + other.width >= self.x + self.width>= other.x and other.y + other.height >= self.y  + self.height >= other.y:
            robot.scrap_pile(self,other)
            
    def user_collision_detection(self, other):
        global gameloop
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y >= other.y:
            gameloop = False
        if other.x + other.width >= self.x + self.width >= other.x and other.y + other.height >= self.y >= other.y:
            gameloop = False
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y + self.height >= other.y:
            gameloop = False
        if other.x + other.width >= self.x + self.width>= other.x and other.y + other.height >= self.y  + self.height >= other.y:
            gameloop = False
        
smoothx,smoothy = 0,0

bots = [robot() for x in range(10)]

    
fps = pygame.time.Clock()



while gameloop == True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                smoothy -= 5
            if event.key == pygame.K_DOWN:
                smoothy += 5
            if event.key == pygame.K_LEFT:
                smoothx -= 5
            if event.key == pygame.K_RIGHT:
                smoothx += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                smoothy = 0
            if event.key == pygame.K_DOWN:
                smoothy = 0 
            if event.key == pygame.K_LEFT:
                smoothx = 0
            if event.key == pygame.K_RIGHT:
                smoothx = 0
        
    board.fill(black)
    for bot in bots:
        robot.generate_bots(bot)
        robot.pathfinding(bot)
        for x in bots:
            if bot != x:
                collision.bot_collision_detection(bot,x)
                collision.user_collision_detection(player,x)
    
                
    player.draw()
    pygame.display.flip()

print('Thank You For Playing')
pygame.quit()
            
