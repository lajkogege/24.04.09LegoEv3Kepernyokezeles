#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok

oraimunka = Feladatok.Feladatok()
# oraimunka.scanner()
# oraimunka.elsoa1()
# oraimunka.elsoa2()
# oraimunka.elsob()
# oraimunka.elsoc()
#print(oraimunka.elsod())
oraimunka.elsoe()
#oraimunka.elsof()


oraimunka.csipog()