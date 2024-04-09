#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopper óra
        self.ido = StopWatch()


    def csipog(self):
        self.ev3.speaker.beep()

    def darts1(self):
        #Rajzoljuk ki egy kör alakú céltáblát, majd véletlen lövöldözöóünk ré
        #Kijelző méretei: 0-177*0-122, bal felső sarok(0,0)
        #képernyő törlése
        self.ev3.screen.clear()
        #körünk
        self.ev3.screen.draw_circle(90,60,60,
        fill=True, color=Color.BLACK)
        szamlalo=0

        #10 véletlen lövés
        db=0
        for loves in range (0,10,1):
            x=random.randint(0,177)
            y=random.randint(0,127)
            #eltaláltuk a céltáblát? majd lövés kirajzolása
            if(90-x)**2+(60-y)**2<=50**2:
                #talált
                self.ev3.screen.draw_circle(x,y,2,
                fill=True, color=Color.WHITE)
                db+=1
            else:
                #nem talált
                self.ev3.screen.draw_circle(x,y,2,
                fill=True, color=Color.BLACK)
            self.csipog()
            wait(100)

        #találatok száma kiirása
        szoveg="Talált: "+ str(db)+"."
        self.ev3.screen.draw_text(80,100,szoveg, text_color=Color.WHITE, background_color=BLACK) 
        wait(5000)

    def darts2a(self):
        #animáljuk a golyó mozgását, letörlés modszerével
        #tábla kirajzolása
        self.ev3.screen.draw_box(172,40,177,80,  fill=True, color=Color.BLACK)
        
        #bal szélére véletlenszerüen megjelnitjük a golyót
        r=5
        y=random.randint(0+r, 127-r)
        self.ev3.screen.draw_circle(0+r,y,r, fill=True, color=Color.BLACK)
        
        wait(5000)
