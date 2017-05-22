import pygame
from pygame.locals import *

from App.MyClass.base_object import BaseObject

class CannonBall(BaseObject):

    def __init__(self,screen,size,name = "Cannon Ball"):
        super(CannonBall,self).__init__(screen,size,name)
        self.set_image_from_file("cannon_ball.png",1)

        self.target_distance = 0
        self.target_height = 0
        self.velocity = 0
        self.angle = 0

    def is_hit(self,laser):
        return False

    def set_target(self,distance,height):
        self.target_distance = distance
        self.target_height = height

    def set_cannon_param(self,velocity,angle):
        self.angle = angle
        self.velocity = velocity

    def update(self):
        if self.moving == True:
            self.rect.x += 30

        self.pos = (self.rect.x, self.rect.y)
        self.clock.tick(40)


