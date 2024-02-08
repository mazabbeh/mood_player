from __future__ import annotations
import pyautogui as pg
from time import sleep

class beans:
    def __init__(self):
        self.state = self.going_down

    def going_down(self):
        if not pg.locateOnScreen('markerbottom.png', grayscale=True):
            pg.keyDown('up')
            self.state = self.going_up


    def going_up(self):
        if pg.locateOnScreen('markertop.png', grayscale=True):
            pg.keyUp('up')
            self.state = self.going_down


    def forever(self):
        sleep(10)
        pg.keyDown('down')
        while True:
            self.state()


glyder = beans()
glyder.forever()