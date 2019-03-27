import pygame
import time
import random
pygame.init()

fire_sound =pygame.mixer.Sound("sound/tick.wav")
explosion_sound = pygame.mixer.Sound("sound/death.wav")
pygame.mixer.music.load("sound/bgm1.mp3")
pygame.mixer.music.play(-1)

white=(255,255,255)
black=(0,0,0) 

red=(200,0,0)
light_red=(255,0,0)

yellow=(200,200,0)
light_yellow=(255,255,0)

green=(0,155,0)
light_green=(0,255,0)


display_width=800
display_height=600

clock=pygame.time.Clock()



tankWidth=40
tankHeight=20
turretWidth=5
wheelWidth=5

ground_height=35

smallfont=pygame.font.SysFont("comicsansms",25)# object for font
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tanks")
pygame.display.update()

# icon=pygame.image.load("image/SnakeHead.png")
# pygame.display.set_icon(icon)
# img=pygame.image.load('image/SnakeHead.png')
# appleimg=pygame.image.load('image/apple.png')

 
AppleThickness=30
block_size=20
FPS=15# frame per second



def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):# function to type text on button i.e an rect
    teextSurf,textRect=text_objects(msg,color,size)
    textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))# center of the rectangle
    gameDisplay.blit(teextSurf,textRect)
# function for text to display to communicate with usee
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect=text_objects(msg,color,size)  #textSurface is  same as pygame Surface and giv tuple
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def tank(x,y,turPos):
    x=int(x)
    y=int(y)

    possibleTurrets=[(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-23,y-12),(x-20,y-14),(x-18,y-15),(x-15,y-17),(x-13,y-19),(x-11,y-21)]


    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))# convert to int as the pixels are not in float when we draw
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turretWidth)
   

    pygame.draw.circle(gameDisplay,black,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+15,y+20),wheelWidth)
    
    return possibleTurrets[turPos]

########################################3333
######************Enemy TAnk******************
def enemy_tank(x,y,turPos):
    x=int(x)
    y=int(y)

    possibleTurrets=[(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+23,y-12),(x+20,y-14),(x+18,y-15),(x+15,y-17),(x+13,y-19),(x+11,y-21)]


    pygame.draw.circle(gameDisplay,black,(x,y),int(tankHeight/2))# convert to int as the pixels are not in float when we draw
    pygame.draw.rect(gameDisplay,black,(x-tankHeight,y,tankWidth,tankHeight))
    pygame.draw.line(gameDisplay,black,(x,y),possibleTurrets[turPos],turretWidth)
   

    pygame.draw.circle(gameDisplay,black,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+15,y+20),wheelWidth)
    
    return possibleTurrets[turPos]


    # startX=20
    # for x in range(8):
    #     pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
    #     startX-=5


def game_controls():

    gcont=True

    while gcont:
        for  event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
          

        gameDisplay.fill(white)
        message_to_screen("Controls", green,-100,'large')
        message_to_screen("Fire: Spacebar",black,-30)
        message_to_screen("Move Turret: Up and Down arrows",black,10)
        message_to_screen("Move Tank: left and Right arrows",black,50)
        message_to_screen("Pause: p",black,90)


        button("play",150,500,100,50,green,light_green,action="play")
        button("Main",350,500,100,50,yellow,light_yellow,action="main")
        button("quit",550,500,100,50,red,light_red,action="quit")


        pygame.display.update()
        clock.tick(15)


def button(text,x,y,width,height,inactive_color,active_color,action=None):
    cur=pygame.mouse.get_pos()# to know the position of the mouse so if it is on button we can perform some action
    click=pygame.mouse.get_pressed()# to know when and where the mouse is pressed """Returns tuple"
    # print(click)  

    if x+width>cur[0]> x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None: # clicl[0] means left button click , click[1], and click[2] means scroll of mouse  and right click respectively
            if action=="quit":
                pygame.quit()
                quit()
            
            if action=="controls":
                game_controls()
            if action=="play":
                gameLoop()
            if action=="main":
                game_intro()

            
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)

def pause():
    paused=True
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
        gameDisplay.fill(white)
        message_to_screen("Paused",black,-100,size="large")
        message_to_screen("Press C to continue or Q to quit.",black,25)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text=smallfont.render("Score: "+str(score),True, black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0   # to get appel at position of multiple of 10 as to same position of snake
    randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0 ## formula "round(x/10.0)*10.0"
    return randAppleX,randAppleY


def barrier(xlocation, randomHeight,barrier_width):
   
    pygame.draw.rect(gameDisplay,black,[xlocation,display_height-randomHeight,barrier_width,randomHeight])

def explosion(x,y,size=50):
    pygame.mixer.Sound.play(explosion_sound )
    explode =True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        startPoint = x,y

        colorChoices=[red,light_red, yellow,light_yellow]

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = x+ random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y+ random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),random.randrange(1,5))
            magnitude += 1
            
            pygame.display.update()
            clock.tick(100)

        explode = False




############################################333333
def fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width, randomHeight ,enemyTankX,enemyTankY):
    pygame.mixer.Sound.play(fire_sound)
    fire=True
    damage = 0

    startingShell=list(xy)

    print("Fire!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red,(startingShell[0],startingShell[1]),5)

       
        startingShell[0] -=(12-turPos)*2


        # y= x**2
        startingShell[1] +=int( (((startingShell[0] -xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos )))
        
        if startingShell[1] > display_height - ground_height:
            print("Last shell :",startingShell[0],startingShell[1])# let  317 ,612
            hit_x=int((startingShell[0]*display_height - ground_height)/startingShell[1])# x/600(which is display_hight)=317/612
            hit_y=int(display_height - ground_height)
            print("Impact: ",hit_x,hit_y)
            if enemyTankX + 10 > hit_x > enemyTankX - 15:
                print("Critical Hit!")
                damage  = 25
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                print("Hard Hit!")
                damage  = 18
            elif enemyTankX + 25 > hit_x > enemyTankX - 15:
                print("Medium Hit!")
                damage  = 10
            elif enemyTankX + 35 > hit_x > enemyTankX - 15:
                print("Light Hit!")
                damage  = 5

            explosion(hit_x,hit_y)
            fire=False
        
        check_x_1=startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell :",startingShell[0],startingShell[1])# let  317 ,612
            hit_x=int((startingShell[0]))# x/600(which is display_hight)=317/612
            hit_y=int(startingShell[1] )
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire=False


        pygame.display.update()
        clock.tick(60)
    return damage
#######################3333
##******enemy Tank Fire************
        
def e_fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width,randomHeight,ptankx,ptanky):
    pygame.mixer.Sound.play(fire_sound)
    damage=0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        # print(currentPower)

        fire = True
        startingShell = list(xy)


        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)

            startingShell[0] += (12 - turPos)*2
            startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50))**2) - (turPos+turPos/(12-turPos)))

            if startingShell[1] > display_height-ground_height:
                hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
                hit_y = int(display_height-ground_height)
                #explosion(hit_x,hit_y)
                if ptankx+15 > hit_x > ptankx - 15:
                    print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                #explosion(hit_x,hit_y)
                fire = False
    

    
    fire = True
    startingShell = list(xy)
    print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)


        startingShell[0] += (12 - turPos)*2



        # y = x**2

        gun_power = random.randrange(int(currentPower*0.90), int(currentPower*1.10))

        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height-ground_height:
            print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y = int(display_height-ground_height)
            print("Impact:", hit_x,hit_y)
            
            
            if ptankx + 10 > hit_x > ptankx - 15:
                print("Critical Hit!")
                damage  = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("Hard Hit!")
                damage  = 18
            elif ptankx + 25 > hit_x > ptankx - 15:
                print("Medium Hit!")
                damage  = 10
            elif ptankx + 35 > hit_x > ptankx - 15:
                print("Light Hit!")
                damage  = 5

            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False
            

        pygame.display.update()
        clock.tick(60)
    return damage

def power(level):
    text=smallfont.render("Power :"+str(level)+"%", True,black)
    gameDisplay.blit(text,[display_width/2,0])

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
        message_to_screen("Welcome to Tanks", green,-100,'large')
        message_to_screen("The objective is to shoot and destroy",black,-30)
        message_to_screen("The enemy tank before they destroy you",black,10)
        message_to_screen("The more enemies you destroy,the harder they get",black,50)
        # message_to_screen("Press C to play,P to pause  or Q to quit",black,180)


        button("play",150,500,100,50,green,light_green,action="play")
        button("control",350,500,100,50,yellow,light_yellow,action="controls")
        button("quit",550,500,100,50,red,light_red,action="quit")


        pygame.display.update()
        clock.tick(15)

def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

##################################3
####******GAme Over ********
def game_over():

    game_over = True

    while game_over:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Game Over",green,-100,size="large")
        message_to_screen("You died.",black,-30)



        button("play Again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")


        pygame.display.update()

        clock.tick(15)

######################33
###*** you win *******8
def you_win():

    win = True

    while win:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("You Won!!",green,-100,size="large")
        message_to_screen("Congratulations!!",black,-30)



        button("play Again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")


        pygame.display.update()

        clock.tick(15)

##################################

def health_bars(player_health,enemy_health):
    
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health >75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else: 
        enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680,25,player_health,25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20,25,enemy_health,25))



def gameLoop():
   
    gameExit=False
    gameOver=False
    FPS=15

    player_health = 100
    enemy_health = 100


    
    barrier_width=50

    mainTankX=display_width*0.9
    mainTankY=display_height*0.9
    tankMove=0
    currentTurPos=0
    changeTur=0

    enemyTankX = display_width*0.1
    enemyTankY = display_height * 0.9

    fire_power = 50
    power_change=0

    xlocation=(display_width/2)+random.randint(-0.1*display_width,0.1*display_width)
    randomHeight=random.randrange(display_height*0.1,display_height*0.6)
    

    while not gameExit:
          
        while gameOver==True:
            # gameDisplay.fill(white)
            message_to_screen("Game over ",red,y_displace=-50,size="large")
            message_to_screen("Press C to play or Q to quit",black,50,size='medium')
            pygame.display.update()
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
                    tankMove=-5
                elif event.key==pygame.K_RIGHT:
                    tankMove=5
                
                elif event.key==pygame.K_UP:# used to move toure of tank i.e bullet fireing hndel
                    changeTur=1
                elif event.key==pygame.K_DOWN:# used to move toure of tank i.e bullet fireing hndel
                   changeTur=-1
                elif event.key==pygame.K_p:
                    pause()
                elif event.key==pygame.K_SPACE:

                    # Hero Tank  calling
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width, randomHeight ,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0,2)

                    for x in range(random.randrange(0,10)):#random range come 
                        if display_width* 0.3 > enemyTankX > display_width * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == "r":
                                enemyTankX -= 5
                            
                            
                            gameDisplay.fill(white) 
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos) 
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)

                            fire_power += power_change
                            power(fire_power)

                            
                            barrier(xlocation,randomHeight,barrier_width)
                            gameDisplay.fill(green,rect=[0, display_height - ground_height,display_width,ground_height])
                            pygame.display.update() 
                            clock.tick(FPS)




                    ####enemy Tank PAramenter 
                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,barrier_width, randomHeight,mainTankX,mainTankY)
                    player_health  -= damage
                
                elif event.key== pygame.K_a:
                    power_change=-1
                elif event.key == pygame.K_d:
                    power_change=1


            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tankMove=0
                
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    changeTur=0
                
                if event.key== pygame.K_a or event.key == pygame.K_d:
                    power_change=0

      
        
        mainTankX+=tankMove 
        currentTurPos+=changeTur 

        if currentTurPos>8:
            currentTurPos=8
        elif currentTurPos<0:
            currentTurPos=0
        
        if mainTankX- (tankWidth/2) < xlocation + barrier_width:
            mainTankX+=5
        
        gameDisplay.fill(white) 
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos) 
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)

        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1

        power(fire_power)

        
        barrier(xlocation,randomHeight,barrier_width)
        gameDisplay.fill(green,rect=[0, display_height - ground_height,display_width,ground_height])
        pygame.display.update()  

        if player_health < 1:
            game_over() 
        elif enemy_health < 1:
            you_win()  
        clock.tick(FPS)

    pygame.quit()
    quit()
game_intro()
gameLoop() 
