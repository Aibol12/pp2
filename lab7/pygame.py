import pygame as pg 
import math
import sys
import datetime
pg.init()
topleft=(88,0)
toppleft=(-9,0)
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)
clock=pg.time.Clock()
x=250
y=250
pos=(x,y)
fps=100
def center(surf, image, topleft, angle):

    rotated_image = pg.transform.rotate(image, -1*angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)
screen=pg.display.set_mode((1280,960))
img=pg.image.load("ffon.jpg")
aaa=pg.image.load("left.png")
aab=pg.image.load("right.png")
pg.display.set_caption("Clock")
Signal=True
while Signal:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            Signal=False
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_d:
                pg.mixer.music.queue("second.mp3")
            if event.key==pg.K_a:
                pg.mixer.music.queue("first.mp3")
            if event.key==pg.K_w:
                pg.mixer.music.pause()
            if event.key==pg.K_s:
                pg.mixer.music.unpause()
            if event.key==pg.K_RIGHT:
                if not x>=1250:
                    x+=20
            if event.key==pg.K_LEFT:
                if not x<=30:
                    x-=20
            if event.key==pg.K_UP:
                if not y<=75:
                    y-=20
            if event.key==pg.K_DOWN:
                if not y>=850:
                    y+=20
    screen.blit(img,(0,0))
    current_time=datetime.datetime.now()
    minute=current_time.minute
    second=current_time.second
  
    center(screen,aaa,toppleft,6*(minute+second/60))
    center(screen,aab,topleft,second*6) 
    ball=pg.draw.circle(screen,Blue,(x,y),25)
    pg.display.flip()

pg.quit()