# -*- coding: cp1252 -*-

import pygame
import random
import time
pygame.init()

clock=pygame.time.Clock()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
orange= (255, 127, 15)
bright_red=(255,0,0)
bright_green=(0,255,0)
light_blue=(124,255,250)
yellow= (255, 211, 79)
hot_yellow=(255, 250, 66)
pink= (255, 127, 205)
hot_pink= (255, 73, 185)

gravity=-0.5

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Bustergotchi")


titlescreen=pygame.image.load('titlescreen.png')
main_screenIMG=pygame.image.load("mainscreen.png")
electricity_screen=pygame.image.load("electricityscreen.png")
hauntedHouse=pygame.image.load("hauntedhouse.png")
beachscene=pygame.image.load('beachscene.png')
jhouse=pygame.image.load('jhouse.png')
food=pygame.image.load('foodcourt.png')
spookyending=pygame.image.load('spookyending.png')
pgeinvite=pygame.image.load('pgeinvite.png')
jacobcries=pygame.image.load('jacobcries.png')
jsprite=pygame.image.load('jsprite.png')
pge0=pygame.image.load('jwhip0.png')
pge1=pygame.image.load('jwhip1.png')
pgeouch=pygame.image.load('jwhipelec.png')
pgeworkguy=pygame.image.load('pgeworkguy.png')
lightbolt=pygame.image.load('lightning.png')
pika0= pygame.image.load('pika0.png')
pika1=pygame.image.load('pika1.png')
vial=pygame.image.load('vial.png')
needle=pygame.image.load('needle.png')
smiley=pygame.image.load('smiley.png')
smileymeh=pygame.image.load('smileymeh.png')
smileysad=pygame.image.load('smileysad.png')
yacht=pygame.image.load('luxury-yachts.png')
imOnABoat=pygame.image.load('luxyacht.png')
ghost_Buster=pygame.image.load('ghostBUSTER.png')
snorlax=pygame.image.load('takeNap.png')
highfood=pygame.image.load('highfood.png')
employee=pygame.image.load('employeeofthemonth.png')



happiness=50
poisoned=False
hasVial=False
highonlife=False
pgeCount=0
eatCount=0
cellphone=False

def happyMeter(happiness):
    if happiness<50:
        pygame.draw.rect(gameDisplay, red, (40, 25, happiness, 32))
        gameDisplay.blit(smileysad, (40, 25))
    elif happiness<75:
        pygame.draw.rect(gameDisplay, yellow, (40, 25, happiness, 32))
        gameDisplay.blit(smileymeh, (40, 25))
    elif happiness<100:
        pygame.draw.rect(gameDisplay, orange, (40, 25, happiness, 32))
        gameDisplay.blit(smileymeh, (40, 25))
    elif happiness>=100:
        pygame.draw.rect(gameDisplay, bright_green, (40, 25, happiness, 32))
        gameDisplay.blit(smiley, (40, 25))

def slaves_hit(pgeCount):
    if pgeCount>39:
        font=pygame.font.SysFont("comicsansms", 23)
        text=font.render("Employees Motivated: "+str(pgeCount), True, green)
        gameDisplay.blit(text, (20,60))
    else:
        font=pygame.font.SysFont("comicsansms", 23)
        text=font.render("Employees Motivated: "+str(pgeCount), True, black)
        gameDisplay.blit(text, (20,60))


class Hslave:
    def __init__(self, pgeslavex, pgeslavey, pgeslavewidth, pgeslaveheight):
        self.pgeslavex=pgeslavex
        self.pgeslavey=pgeslavey
        self.pgeslavewidth=pgeslavewidth
        self.pgeslaveheight=pgeslaveheight
        self.image=pgeworkguy
        self.rect=pygame.Rect(pgeslavex, pgeslavey,pgeslavewidth,pgeslaveheight)
        self.health=10


    def recoil(self, pgeBuster):
        slaveguy=pygame.Rect(self.pgeslavex, self.pgeslavey,self.pgeslavewidth,self.pgeslaveheight)
        if slaveguy.colliderect(pgeBuster):
            return True
            

    def draw(self, gameDisplay):
        gameDisplay.blit(self.image, (self.pgeslavex, self.pgeslavey))

class PGEBuster:
    def __init__(self, busterx, bustery):
        self.busterx=busterx
        self.bustery=bustery
        self.width=150
        self.height=115
        self.velocity=-0.5
        self.onGround=False
        self.i0=pge0
        self.i1=pge1
        self.currentImage=0
        self.timeNum=0
        self.timeTarget=10
        self.owieTime=0
        self.vulnerable=True

    def jump(self):
        if self.onGround==True:
            self.velocity=13

    def update(self, gravity):
        self.rect=pygame.Rect(self.busterx,self.bustery, self.width, self.height)
        self.timeNum+=1
        if self.bustery>420:
            self.bustery=(420)
            self.onGround=True

        if self.bustery<419:
            self.onGround=False
                
        if self.onGround==False:
            self.velocity+=gravity

        if (self.timeNum==self.timeTarget):
            if (self.currentImage==0):
                self.currentImage=1
            else:
                self.currentImage=0
            self.timeNum=0
        if self.vulnerable==False:
            self.owieTime+=1
            if self.owieTime>40:
                self.vulnerable=True
                self.owieTime=0


        self.bustery-=self.velocity

    def ouch(self):
        if self.vulnerable==True:
            self.vulnerable=False

    def render(self, gameDisplay):
        if self.vulnerable==False:
            gameDisplay.blit(pgeouch, (self.busterx, self.bustery))
        elif (self.currentImage==0):
            gameDisplay.blit(self.i0, (self.busterx,self.bustery))
        else:
            gameDisplay.blit(self.i1, (self.busterx,self.bustery))

class Jacob_Bust(object):
    def __init__ (self,x,y,w,h):
        self.image=jsprite
        self.rect=pygame.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.w=w
        self.h=h
        self.rect.x=x
        self.rect.y=y

    def handle_keys(self):
        key=pygame.key.get_pressed()
        dist=4
        if key[pygame.K_DOWN]:
            if self.y>display_height:
                self.y-=0
                self.rect.y-=0
            else:
                self.y += dist
                self.rect.y+=dist
        if key[pygame.K_UP]:
            if self.y<0:
                self.y+=0
                self.rect.y+=0
            else:
                self.y -= dist
                self.rect.y -= dist
        if key[pygame.K_RIGHT]:
            if self.x>display_width:
                self.x-=0
                self.rect.x-=0
            else:
                self.x += dist
                self.rect.x += dist
        if key[pygame.K_LEFT]:
            if self.x<0:
                self.x+=0
                self.rect.x+=0
            else:
                self.x -= dist
                self.rect.x -= dist
        if self.x<0:
            map_screen()
        if self.y+78>display_height:
            map_screen()
        if self.x+42>display_width:
            map_screen()
            
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Door(object):
    def __init__(self, x,y,w,h):
        self.rect=pygame.Rect(x,y,w,h)

class Pikaenemy(object):
    def __init__(self, pikax, pikay):
        self.pikax=pikax
        self.pikay=pikay
        self.p0=pika0
        self.p1=pika1
        self.currentImage=0
        self.timeNum=0
        self.timeTarget=10
        self.rect=pygame.Rect(self.pikax, self.pikay, 120, 90)
    def update(self):
        self.timeNum+=1
        if (self.timeNum==self.timeTarget):
            if (self.currentImage==0):
                self.currentImage=1
            else:
                self.currentImage=0
            self.timeNum=0

    def render(self, gameDisplay):
        if (self.currentImage==0):
            gameDisplay.blit(self.p0, (self.pikax,self.pikay))
        else:
            gameDisplay.blit(self.p1, (self.pikax,self.pikay))


def quitgame():
    pygame.quit()
    quit()

def button(msg, x,y,w,h,ic, ac, action=None):#ic and ac stand for inactive/active color
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(gameDisplay, ac, (x,y, w,h))
            if click[0]==1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

        smallText=pygame.font.SysFont("None",20)
        textSurf, textRect=text_objects(msg, smallText, black)
        textRect.center=( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

def text_objects(text, font, color):
    textSurface=font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def lightning(lightningx, lightningy):
    gameDisplay.blit(lightbolt, (lightningx, lightningy))

def sadDay():
    if happiness<0:
        jacobCries()

def happyDay():
    if happiness>99 and highonlife==True and pgeCount>39:
        text="*ring ring* press A to answer"
        largeText=pygame.font.SysFont(None, 30)
        TextSurf, TextRect=text_objects(text, largeText, red)
        TextRect=(250, 150)
        gameDisplay.blit(TextSurf,TextRect)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    phoneCall()

def phoneCall():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    map_screen()

        gameDisplay.blit(pgeinvite, (0,0))
        clock.tick(15)
        pygame.display.update()

def ghostgameover():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
        gameDisplay.blit(spookyending, (0,0))
        clock.tick(60)
        pygame.display.update()

def jacobCries():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()

        gameDisplay.blit(jacobcries, (0,0))
        clock.tick(60)
        pygame.display.update()

def onAYacht():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
                
        gameDisplay.blit(imOnABoat, (0,0))
        clock.tick(15)
        pygame.display.update()

def takeNap():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
                    
        gameDisplay.blit(snorlax, (0,0))
        clock.tick(15)
        pygame.display.update()

def ghostBUSTER():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
                    
        gameDisplay.blit(ghost_Buster, (0,0))
        clock.tick(15)
        pygame.display.update()

def munchies():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
        gameDisplay.blit(highfood, (0,0))
        clock.tick(15)
        pygame.display.update()

def employee_Month(pgeCount):
    if pgeCount>99:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game_intro()
        gameDisplay.blit(employee, (0,0))
        clock.tick(15)
        pygame.display.update()

def game_intro():
    intro=True
    x=(display_width*0.385)
    y=(display_height*0.05)

    global happiness
    global poisoned
    global hasVial
    global highonlife
    global pgeCount
    global eatCount
    global cellphone
    
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    map_screen()

        gameDisplay.blit(titlescreen, (0,0))
        happiness=50
        poisoned=False
        hasVial=False
        highonlife=False
        pgeCount=0
        eatCount=0
        cellphone=False

        button ("Buster time", 600, 50, 150, 75, pink, hot_pink,map_screen)
        button ("Buster out", 600, 125, 150, 75, yellow, hot_yellow,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def map_screen():
    running=True
    jacob = Jacob_Bust (400,400,42,78)
    doormonay=Door (121,89,112,162)
    doorghost=Door (579,86,120,123)
    doorfood=Door (64,410,166,142)
    doorbeach=Door (588,436,156,114)
    doorhouse=Door (350,270,126,89)

    ptimer=0
    global happiness
    global poisoned
    global cellphone
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if jacob.rect.colliderect(doormonay):
            electricity()
        if jacob.rect.colliderect(doorghost):
            haunted_house()
        if jacob.rect.colliderect(doorbeach):
            beach()
        if jacob.rect.colliderect(doorhouse):
            jbhouse()
        if jacob.rect.colliderect(doorfood):
            foodCourt()

        if jacob.rect.collidepoint(410,185):
            jbhouse()
        if jacob.rect.collidepoint(385,220):
            jbhouse()
        if jacob.rect.collidepoint(360,245):
            jbhouse()
        if jacob.rect.collidepoint(440,220):
            jbhouse()
        if jacob.rect.collidepoint(457,245):
            jbhouse()

        if poisoned==True:
            ptimer+=1
            if ptimer==10:
                gameDisplay.fill(red)
            if ptimer==60:
                happiness-=2
                ptimer=0

        if highonlife==True:
            if happiness>99:
                cellphone=True
                


        jacob.handle_keys()
        gameDisplay.blit(main_screenIMG, (0,0))

        jacob.draw(gameDisplay)
        happyMeter(happiness)
        sadDay()
        happyDay()
        pygame.display.update()
        clock.tick(60)
        
def electricity():
    pge=True

    busterx=200
    bustery=400
    pgeBuster=PGEBuster(busterx, bustery)
    Bustermove=0
    
    pgeslavex=display_width
    pgeslavey=display_height*0.70
    pgeslavewidth=50
    pgeslaveheight=50
    slave=Hslave(pgeslavex, pgeslavey, pgeslavewidth, pgeslaveheight)


    lightningx=random.randrange(0, display_width)
    lightningy=display_height

    pikax=display_width
    pikay=display_height*0.80
    pikachew=Pikaenemy(pikax, pikay)
    pikaspeed=10

    ptimer=0
    global happiness
    global poisoned
    global pgeCount
    
    while pge:
        gameDisplay.blit(electricity_screen, (0,0))
        slaves_hit(pgeCount)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    Bustermove=5
                if event.key==pygame.K_LEFT:
                    Bustermove=-5
                if event.key==pygame.K_a:
                    pgeBuster.jump()
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    Bustermove=0

        pgeBuster.render(gameDisplay)
        pgeBuster.update(gravity)
        if pgeBuster.busterx<0:
            map_screen()
        if pgeBuster.bustery<0:
            pgeBuster.bustery=0
        if pgeBuster.busterx+pgeBuster.width>display_width:
            pgeBuster.busterx=display_width-pgeBuster.width

        if pgeBuster.busterx+100>pikachew.pikax and pgeBuster.busterx<(pikachew.pikax+56) and pgeBuster.bustery+pgeBuster.height>pikachew.pikay:
            if pgeBuster.vulnerable==True:
                happiness-=15
                pgeBuster.ouch()
        
        pgeBuster.busterx+=Bustermove

        pikachew.render(gameDisplay)
        pikachew.update()
        pikachew.pikax-=pikaspeed
        if pikachew.pikax<0:
            pikachew.pikax=display_width
            pikaspeed=random.randrange(3,11)

        if slave.pgeslavex<700:
            if slave.recoil(pgeBuster)==True:
                slave.pgeslavex=display_width
                happiness+=3
                pgeCount+=1

        slave.draw(gameDisplay)
        slave.pgeslavex-=4
        if slave.pgeslavex<0:
            slave.pgeslavex=display_width

        lightningy+=8
        lightning(lightningx, lightningy)
        if lightningy>display_height:
            lightningy=0
            lightningx=random.randrange(0,display_width)
        if pgeBuster.busterx+100>lightningx and pgeBuster.busterx<lightningx+78 and pgeBuster.bustery<lightningy+144 and pgeBuster.bustery>lightningy:
            if pgeBuster.vulnerable==True:
                happiness-=15
                pgeBuster.ouch()

        if poisoned==True:
            ptimer+=1
        if ptimer==10:
            gameDisplay.fill(red)
        if ptimer==60:
            happiness-=2
            ptimer=0

        happyMeter(happiness)
        sadDay()
        employee_Month(pgeCount)
        clock.tick(60)
        pygame.display.update()
    

def haunted_house():
    x=300
    y=500
    jacob = Jacob_Bust (x,y,42,78)
    global happiness
    global poisoned

    ptimer=0

    largeText=pygame.font.SysFont(None, 25)
    
    t0= "This is the haunted manor..." 
    t1= "Jacob doesnt like scary places..."
    t2= "You have a feeling of dread..."
    t3= "WHAT WAS THAT?"

    h0= "You feel a rush of determination."
    h1= """ "When there's something strange" """
    h2= """ "in your neighborhood. Who you gonna call?" """
    h3= """ "Ghost BUSTER!" """
    text= t0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(hauntedHouse, (0,0))
        happyMeter(happiness)
        jacob.handle_keys()
        
        if jacob.y<470 and jacob.x<365 and jacob.y>370 or jacob.y<470 and jacob.y>370 and jacob.x>380:
            jacob.y+=4
        if jacob.y<300:
            jacob.y+=4
        if jacob.y<310 and jacob.x>355 and jacob.x<380:
            if highonlife == False:
                ghostgameover()
            elif highonlife == True:
                ghostBUSTER()
        if jacob.y+78<590:
            jacob.y+=3

        if highonlife==False:
            ptimer+=1
            if ptimer==60:
                happiness-=2
                ptimer=0

        if poisoned==True:
            ptimer+=1
            if ptimer==10:
                gameDisplay.fill(red)
            if ptimer==60:
                happiness-=2
                ptimer=0

        if highonlife==False:
            if jacob.y<500:
                text=t0
            if jacob.y<470:
                text=t1
            if jacob.y<400:
                text=t2
            if jacob.y<340:
                text=t3

        if highonlife==True:
            if jacob.y<500:
                text=h0
            if jacob.y<470:
                text=h1
            if jacob.y<400:
                text=h2
            if jacob.y<340:
                text=h3

        TextSurf, TextRect=text_objects(text, largeText, white)
        TextRect=(400, 150)
        gameDisplay.blit(TextSurf,TextRect)

        jacob.draw(gameDisplay)
        sadDay()
        pygame.display.update()
        clock.tick(60)

def beach():
    x=200
    y=510
    jacob = Jacob_Bust (x,y,42,78)
    onABoat=pygame.Rect(545, 430, 300, 20)

    largeText=pygame.font.SysFont(None, 30)
    text=""" "Just what I needed." Press Y to cure allergies. """
    recoverytext="You feel a sudden rush of determination"
    
    global happiness
    global poisoned
    global hasVial
    global highonlife
    ptimer=0
    rush=False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    if poisoned==True:
                        if hasVial==True:
                            if jacob.x>550 and jacob.x<630 and jacob.y>500:
                                happiness+=50
                                rush=True
                                highonlife=True
                                poisoned=False
                                hasVial=False
                
                
        gameDisplay.blit(beachscene, (0,0))
        happyMeter(happiness)

        if poisoned==True:
            ptimer+=1
            if ptimer==10:
                gameDisplay.fill(red)
            if ptimer==60:
                happiness-=2
                ptimer=0

        if poisoned==True:
            if hasVial==True:
                gameDisplay.blit(needle, (600, 550))
            if jacob.x>550 and jacob.x<630 and jacob.y>500:
                TextSurf, TextRect=text_objects(text, largeText, white)
                TextRect=(180, 25)
                gameDisplay.blit(TextSurf,TextRect)


        if jacob.y<400:
            jacob.y+=4

        if rush==True:
            TextSurf, TextRect=text_objects(recoverytext, largeText, white)
            TextRect=(220, 25)
            gameDisplay.blit(TextSurf,TextRect)

        if happiness>99:
            if pgeCount>39:
                if highonlife==True:
                    if cellphone==True:
                        gameDisplay.blit(yacht, (420, 180))
                        if jacob.rect.colliderect(onABoat):
                            onAYacht()
            

        if rush==True:
            poisoned=False
            hasVial=False
                
        jacob.handle_keys()
        jacob.draw(gameDisplay)
        sadDay()
        pygame.display.update()
        clock.tick(60)

def jbhouse():
    x=210
    y=250
    jacob = Jacob_Bust (x,y,42,78)
    
    largeText=pygame.font.SysFont(None, 40)

    global happiness
    global poisoned
    global hasVial
    global eatCount
    ptimer=0

    vialText="Uh oh. Missing a syringe..."
    text=None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    map_screen()
                if event.key == pygame.K_a:
                    if poisoned==True:
                        if jacob.x>315 and jacob.y>240 and jacob.y<300:
                            hasVial=True
                            text= vialText
                if event.key == pygame.K_m:
                    map_screen()
        
        gameDisplay.blit(jhouse, (0,0))
        happyMeter(happiness)

        if jacob.y<160 and jacob.x<210 and jacob.x+42>190:
            map_screen()

        if poisoned==True:
            ptimer+=1
            if ptimer==10:
                gameDisplay.fill(red)
            if ptimer==60:
                happiness-=2
                ptimer=0

        if poisoned==True:
            if hasVial==False:
                gameDisplay.blit(vial, (375, 300))

        if jacob.x<100:
            jacob.x=100
        if jacob.x+42>370:
            jacob.x=370-42
        if jacob.y<160:
            jacob.y=160
        if jacob.y+78>390:
            jacob.y=390-78

        if eatCount>5:
            takeNap()

        TextSurf, TextRect=text_objects(text, largeText, white)
        TextRect=(240, 25)
        gameDisplay.blit(TextSurf,TextRect)
            

        jacob.handle_keys()
        jacob.draw(gameDisplay)
        sadDay()
        pygame.display.update()
        clock.tick(60)

def foodCourt():
    x=display_width-78
    y=270
    jacob=Jacob_Bust(x, y, 42, 78)
    french=pygame.Rect(650, 240, 100, 15)
    hotdog=pygame.Rect(450, 240, 100, 15)
    mex=pygame.Rect(250, 240, 100, 15)
    sushi=pygame.Rect(50, 240, 100, 15)

    largeText=pygame.font.SysFont(None, 40)

    french_1="Oui Oui. Sacrebleu!" 
    french_2="Welcome to the Snooty Snail."
    french_3="Only rich people can eat here!"
    french_4="Do you want some whine?"
    french_5="Whine? Press Y or N"
    french_y="Sacrebleeuuu!!"
    french_n="Stupid American!"


    hotdog_1= "*BUUUUUURRRRPP*"
    hotdog_2= "*scratch* *scratch*"
    hotdog_3= "Wanna buy a Freedom Dog?"
    hotdog_4= "Hotdog? Press Y or N"
    hotdog_y= "I love my country!"
    hotdog_n= "You commie scum."

    taco_1= "Hola, amigo!"
    taco_2= "Donde esta su biblioteca?"
    taco_3= "Mi gato de rosa estoy entonces."
    taco_4= "Taco? Press Y or N"
    taco_y= "Gracias, amigo."
    taco_n= "Mis hijos se morirán de hambre."

    sushi_1= "Konichiwa."
    sushi_2= "Desu nobe lolita."
    sushi_3= "Oni-chan no dosu, amene."
    sushi_4= "Sushi? Press Y or N"
    sushi_y= "You suddenly dont feel so good."
    sushi_n= "Arigatou gozaimasu."

    sofull= "Ugh. So full. I need a nap..."
    nomnom= "hotdoghotdoghotdoghotdoghotdoghot"
    text=None

    global happiness
    global poisoned
    global eatCount
    ptimer=0
    

    while True:
        gameDisplay.blit(food, (0,0))
        happyMeter(happiness)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    if jacob.rect.colliderect(french):
                        if text==french_1:
                            text=french_2
                        elif text==french_2:
                            text=french_3
                        elif text==french_3:
                            text=french_4
                        elif text==french_4:
                            text=french_5
                        else: text=french_1

                if event.key==pygame.K_a:
                    if jacob.rect.colliderect(hotdog):
                        if text==hotdog_1:
                            text=hotdog_2
                        elif text==hotdog_2:
                            text=hotdog_3
                        elif text==hotdog_3:
                            text=hotdog_4
                        else: text=hotdog_1

                if event.key==pygame.K_a:
                    if jacob.rect.colliderect(mex):
                        if text==taco_1:
                            text=taco_2
                        elif text==taco_2:
                            text=taco_3
                        elif text==taco_3:
                            text=taco_4
                        else: text= taco_1

                if event.key==pygame.K_a:
                    if jacob.rect.colliderect(sushi):
                        if text==sushi_1:
                            text=sushi_2
                        elif text==sushi_2:
                            text=sushi_3
                        elif text==sushi_3:
                            text=sushi_4
                        else: text= sushi_1

            if text==french_5:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        happiness+=10
                        eatCount+=1
                        text= french_y
                    if event.key==pygame.K_n:
                        text= french_n

            if text==hotdog_4:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        happiness += 5
                        eatCount+=1
                        text= hotdog_y
                    if event.key==pygame.K_n:
                        text= hotdog_n

            if text==taco_4:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        happiness += 5
                        eatCount+=1
                        text= taco_y
                    if event.key==pygame.K_n:
                        text= taco_n

            if text==sushi_4:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        happiness+= 10
                        eatCount+=1
                        poisoned=True
                        text= sushi_y
                    if event.key==pygame.K_n:
                        text= sushi_n

        if jacob.y<250:
            jacob.y+=4
            jacob.rect.y+=4
        if jacob.y>270:
            jacob.y-=4
            jacob.rect.y-=4

        TextSurf, TextRect=text_objects(text, largeText, white)
        TextRect=(305, 450)
        gameDisplay.blit(TextSurf,TextRect)

        if poisoned==True:
            ptimer+=1
            if ptimer==10:
                gameDisplay.fill(red)
            if ptimer==60:
                happiness-=2
                ptimer=0


        jacob.handle_keys()
        jacob.draw(gameDisplay)

        if happiness>99:
            if eatCount>5:
                text=sofull

        if highonlife==True:
            text=nomnom
            if jacob.rect.colliderect(hotdog):
                munchies()
            

        sadDay()
        pygame.display.update()
        clock.tick(60)

game_intro()
