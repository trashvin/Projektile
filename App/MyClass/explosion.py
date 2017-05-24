from App.MyClass.base_object import *

class Explosion(BaseObject):

    def __init__(self,screen,size,name = "Explosion"):
        super(Explosion,self).__init__(screen,size,name)

        self.set_image_from_file("explosion_sm.png",1)
        self.show = False
        self.duration = 3

    def update(self):

        if self.show == True:
            pass