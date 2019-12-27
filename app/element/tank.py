import os,sys
import random

from app.library import *
from app.element.base_object import BaseObject

import pygame
from pygame.locals import *

class Tank(BaseObject):

    def __init__(self,screen,size, name = "Tank"):
        super(Tank,self).__init__(screen,size,name)

        self.move_distance = random.randint(50,700)

        tank_img = os.path.join(get_image_dir(),"tanker.png")
        self.set_sound_from_file("tank_moving.wav")
        self.set_image_from_file(tank_img,1)

        self.cannon_exit_velocity = 1000
        self.cannon_angle = 2

    def set_attack_param(self,move_distance):
        self.move_distance = move_distance

    def set_cannon_angle(self,angle):
        self.cannon_angle = angle

    def send_bomb(self):
        return (self.rect.x == self.move_distance)

    def is_hit(self,bomb):
        if bomb.rect.y >= self.rect.y - 20:
            return True
        else:
            return False

    def fire_cannon(self):
        if self.moving == False and self.rect.x >= self.move_distance:
            return True
        else:
            return False


    def update(self):

        if self.moving == True:
            if self.rect.x < self.move_distance :
                self.rect.x += 5


            else:
                self.move(False)
                self.moving == False

        self.pos = (self.rect.x,self.rect.y)




