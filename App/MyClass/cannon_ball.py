import pygame
from pygame.locals import *

from App.MyClass.base_object import BaseObject
from App.library import *

class CannonBall(BaseObject):

    def __init__(self,screen,size,name = "Cannon Ball"):
        super(CannonBall,self).__init__(screen,size,name)
        self.set_image_from_file("cannon_ball.png",1)

        self.velocity = 0
        self.angle = 0
        self.ptime = 0
        self.init_h = 0
        self.target = None
        self.target_distance = 0
        self.source = None

    def is_hit(self,laser):
        print((self.pos),(laser.target))
        if self.pos == laser.target :
            return True
        else:
            return False



    def set_source_target(self,source,target):
        self.target = target
        self.source = source
        self.set_pos(source.pos)

        self.target_distance = self.target.rect.x - self.source.rect.x + 150
        self.velocity = get_projectile_initial_v(math.radians(45),self.target_distance)

    def set_source(self,source):
        self.source = source
        self.set_pos(source.pos)

    def update(self):

        if self.moving == True and self.rect.y > 0:
            self.ptime += 1/5
            curr_pos = get_projectile_xy(self.velocity,math.radians(45),self.ptime,self.init_h)
            #self.init_h += curr_pos[1]
            self.rect.x = curr_pos[0] + self.source.rect.x + self.source.size[0]
            self.rect.y = abs( self.source.rect.y -curr_pos[1])

        self.pos = (self.rect.x, self.rect.y)



