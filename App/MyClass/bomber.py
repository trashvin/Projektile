from App.library import *
from App.MyClass.base_object import BaseObject

import pygame
from pygame.locals import *


class Bomber(BaseObject):

    def __init__(self,screen,size, name = "Bomber"):
        super(Bomber,self).__init__(screen,size,name)

        bomber_img = os.path.join(get_image_dir(),"bomber.png")
        self.set_image_from_file(bomber_img,1)

    def is_out_of_screen(self):
        print(self.rect.x + self.size[0])
        if (self.rect.x + self.size[0]) < 0:
            return True
        else:
            return False

    def update(self):

        if self.moving == True:
            self.rect.x -= 20
        else:
            self.move(False)

        self.pos = (self.rect.x,self.rect.y)
        self.clock.tick(40)



