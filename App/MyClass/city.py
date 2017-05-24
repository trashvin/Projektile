import os,sys

from App.library import *
from App.MyClass.base_object import BaseObject

import pygame
from pygame.locals import *


class City(BaseObject):

    def __init__(self,screen,size, name = "City"):
        super(City,self).__init__(screen,size,name)

        city_img = os.path.join(get_image_dir(),"city.png")
        self.set_image_from_file(city_img,1)

    def is_hit(self,cannon_ball):

        if self.rect.x + 150 <= cannon_ball.rect.x and cannon_ball.moving == True:
            return True
        else:
            return False

    def is_defense_breached(self,attacker):

        if attacker.rect.x >= self.rect.x - 100 :
            return True
        else:
            return False





