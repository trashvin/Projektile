from app.library import *
from app.element.base_object import BaseObject

import pygame
from pygame.locals import *


class Bomb(BaseObject):

    def __init__(self,screen,size, name = "Bomb"):
        super(Bomb,self).__init__(screen,size,name)

        self.clock = pygame.time.Clock()
        self.dropped = False
        bomb_img = os.path.join(get_image_dir(),"bomb.png")
        self.set_image_from_file(bomb_img,1)

    def set_dropped(self,dropped):
        self.dropped = dropped

    def update(self):

        if self.moving == True:
            self.rect.y += 20
        else:
            self.move(False)

        self.pos = (self.rect.x,self.rect.y)
        self.clock.tick(40)

    def drop(self,pos):
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]





