import pygame
import random

width,height = 800,600
pygame.init()
black = (0,0,0)
white = (255,255,255)
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
        self.x += smoothx
        self.y += smoothy
        pygame.draw.rect(board,white,(self.x,self.y,self.width,self.height))

class robot:
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = random.randint(0, height)
        self.width = 10
        self.height = 10

    def generate_bots(self):
        pygame.draw.rect(board,red,(self.x,self.y,self.width,self.height))

    def pathfinding(self):
        if player.x > self.x:
            self.x += 5
        if player.x < self.x:
            self.x -= 5
        if player.y > self.y:
            self.y += 5
        if player.y < self.y:
            self.y -= 5

    def collision_detection(self, other):
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y >= other.y:
            pass
        if other.x + other.width >= self.x + self.width >= other.x and other.y + other.height >= self.y >= other.y:
            pass
        if other.x + other.width >= self.x >= other.x and other.y + other.height >= self.y + self.height >= other.y:
            pass
        if other.x + other.width >= self.x + self.width>= other.x and other.y + other.height >= self.y  + self.height >= other.y:
            pass
        
smoothx,smoothy = 0,0

bots = [robot() for x in range(2)]

    
fps = pygame.time.Clock()

player = user(0,0)


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
                robot.collision_detection(bot,x)
                
    player.draw()
    pygame.display.flip()


pygame.quit()
            
