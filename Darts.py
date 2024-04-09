#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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
        self.eve3.screen.draw_circle(90,50,50,
        fill=True, color=Color.BLACK)

        #10 véletlen lövés
        
        wait(5000)

