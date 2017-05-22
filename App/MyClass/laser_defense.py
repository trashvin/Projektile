from App.MyClass.base_object import *

class LaserDefense(BaseObject):

    def __init__(self,screen,size,name="Lase Defense"):
        super(LaserDefense,self).__init__(screen,size,name)

        laser_defense_img = os.path.join(get_image_dir(), "laser_launcher.png")
        self.set_image_from_file(laser_defense_img, 1)
