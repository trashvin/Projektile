from App.MyClass.base_object import *

class Explosion(BaseObject):

    def __init__(self,screen,size,name = "Explosion"):
        super(Explosion,self).__init__(screen,size,name)

        self.set_image_from_file("explosion_sm.png",1)
        self.show = False
        self.time = 0

    def restart_timer(self):
        self.time= 0

    def is_expired(self):
        return (self.time > 0.5)

    def update(self):
        self.time += 1/40
