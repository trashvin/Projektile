import pygame
from App.MyClass.base_object import *

import random

class LaserDefense(BaseObject):

    def __init__(self,screen,size,name="Lase Defense"):
        super(LaserDefense,self).__init__(screen,size,name)

        laser_defense_img = os.path.join(get_image_dir(), "laser_launcher.png")
        self.set_image_from_file(laser_defense_img, 1)
        self.fire_laser = False
        self.laser_on = False
        self.target =(0,0)
        self.available = True
    def set_target(self,target):
        self.target = target.pos

        val = random.randint(1, 1000)
        if val % 3 == 0:
            self.target = target.pos
        else:
            self.target = (target.pos[0] + 20, target.pos[1] + 20)

    def update(self):

        if self.fire_laser == True:

            print(self.target)
            pygame.draw.aaline(self.screen, [200, 200, 133], (self.rect.x + 20, self.rect.y), self.target)
            pygame.draw.aaline(self.screen, [200, 200, 133], (self.rect.x + 20, self.rect.y + 2), self.target)
            pygame.draw.aaline(self.screen,[200,200,200],(self.rect.x + 20,self.rect.y + 2),self.target)
            pygame.draw.aaline(self.screen, [200, 200, 133], (self.rect.x + 20, self.rect.y + 2), self.target)

            self.fire_laser = False
            self.available = False