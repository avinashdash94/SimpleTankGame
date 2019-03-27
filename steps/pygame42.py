import pygame
import time
import random
pygame.init()

white=(255,255,255)
black=(0,0,0) 
red=(255,0,0)

green=(0,155,0)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
pygame.display.update()

icon=pygame.image.load("image/SnakeHead.png")
pygame.display.set_icon(icon)
img=pygame.image.load('image/SnakeHead.png')
appleimg=pygame.image.load('image/apple.png')
clock=pygame.time.Clock()
 
AppleThickness=30
block_size=20
FPS=15# frame per second
direction="right"

smallfont=pygame.font.SysFont("comicsansms",25)# object for font
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

def pause():
    paused=True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        # gameDisplay.fill(white)
        
        clock.tick(5)

def score(score):
    text=smallfont.render("Score: "+str(score),True, black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0   # to get appel at position of multiple of 10 as to same position of snake
    randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0 ## formula "round(x/10.0)*10.0"
    return randAppleX,randAppleY

def game_intro():
    intro=True

    while intro:
        for  event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
        green,
        -100,
        'large')
        message_to_screen("The objectgive of the game is to eat red apples",black,-30)
        message_to_screen("The more apples you eat ,the longer you get",black,10)
        message_to_screen("If you run into yourself,or the edges,youe die!",black,50)
        message_to_screen("Press C to play,P to pause  or Q to quit",black,180)
        pygame.display.update()
        clock.tick(15)

def snake(block_size,snakeList):#  creating snake 
    if direction=='right':
        head=pygame.transform.rotate(img,270)
    if direction=='left':
        head=pygame.transform.rotate(img,90)
    if direction=='up':
        head=img
    if direction=='down':
        head=pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_object(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

# function for text to display to communicate with usee
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect=text_object(msg,color,size)  #textSurface is  same as pygame Surface and giv tuple
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)



def gameLoop():
    global direction

    direction='right'
    gameExit=False
    gameOver=False

    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0

    snakeList=[]
    snakeLength=1


    randAppleX,randAppleY=randAppleGen()   

    while not gameExit:
        if gameOver==True:
            message_to_screen("Game over ",red,y_displace=-50,size="large")
            message_to_screen("Press C to play or Q to quit",black,50,size='medium')
            pygame.display.update()

        while gameOver==True:
            # gameDisplay.fill(white)
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=False
                    gameExit=True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    pause()
        # setting boundaries
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
        
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
        
        # pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))

        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)    

        if len(snakeList)>snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        
        snake(block_size,snakeList) # snake() called  to  created  snake 
        score(snakeLength-1)
        pygame.display.update()

        # if lead_x==randAppleX and lead_y==randAppleY:           
        #     randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0   # to get appel at position of multiple of 10 as to same position of snake
        #     randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0 ## formula "round(x/10.0)*10.0"
        #     snakeLength+=1
# ###############privouse versin of same block
#         if lead_x>=randAppleX and lead_x<=randAppleX+AppleThickness:
#             if lead_y>=randAppleY and lead_y<=randAppleY+AppleThickness:
#                 randAppleX=round(random.randrange(0,display_width-block_size))#/10.0)*10.0   # to get appel at position of multiple of 10 as to same position of snake
#                 randAppleY=round(random.randrange(0,display_height-block_size))#/10.0)*10.0 ## formula "round(x/10.0)*10.0"
#                 snakeLength+=1
###############new version of pice of code
        
        if lead_x>randAppleX and lead_x<randAppleX+AppleThickness or lead_x+block_size>randAppleX and lead_x+block_size<randAppleX+AppleThickness:
            # print("X cross over")
            if lead_y>randAppleY and lead_y<randAppleY+AppleThickness :
               randAppleX,randAppleY=randAppleGen()
               snakeLength+=1
            elif lead_y+block_size>randAppleY and lead_y+block_size< randAppleY+AppleThickness:
                randAppleX,randAppleY=randAppleGen()
                snakeLength+=1
                
            
        clock.tick(FPS)

    pygame.quit()
    quit()
game_intro()
gameLoop() 
