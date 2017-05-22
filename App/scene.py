import pygame
from pygame.locals import *
from App.MyClass.tank import *
from App.MyClass.city import *
from App.MyClass.bomber import *
from App.MyClass.laser_defense import *
from App.MyClass.bomb import *
from App.MyClass.cannon_ball import *

class Scene():

    #statc constants
    WIDTH = 1200
    HEIGHT = 600

    def __init__(self,name):
        self.name = name
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.screen.fill([123,123,123])
        pygame.display.set_caption(self.name)
        pygame.mixer.init(4410, -16, 2, 2048)

        self.bg_image = os.path.join(get_image_dir(),"background.png")

    def set_background(self):
        bg_image = pygame.transform.scale( pygame.image.load(self.bg_image).convert(),(self.WIDTH,self.HEIGHT))
        self.screen.blit(bg_image,(0,0))

    def start(self):
        city_sprites = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        bomb = Bomb(self.screen,(30,60),"Bomb")

        tank = Tank(self.screen,(70,40))
        tank.set_pos((20,443))

        city = City(self.screen,(300,300),"City")
        city.set_pos((850,180))

        bomber = Bomber(self.screen,(120,60))
        bomber.set_pos((1300,100))

        laser_launcher = LaserDefense(self.screen,(90,50),"Laser Launcher")
        laser_launcher.set_pos((950,430))

        cannon_ball = CannonBall(self.screen,(15,15),"Cannon Ball")


        city_sprites.add(city)
        #city_sprite.add(laser_launcher)
        #tank_sprite.add(tank)
        #tank_sprite.add(bomber)
        all_sprites.add(bomber)
        all_sprites.add(laser_launcher)

        #all_sprites.add(cannon_ball)

        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        tank.move(True)
                elif event.type == QUIT:
                    running == False

            self.set_background()
            city_sprites.draw(self.screen)

            temp_surface = pygame.Surface((self.WIDTH,self.HEIGHT))
            temp_surface.fill([0,0,0])
            temp_surface.set_colorkey([0,0,0])

            if tank.fire_cannon() == True and cannon_ball.moving == False:
                cannon_ball.set_pos((tank.rect.x+70,tank.rect.y + 5))
                cannon_ball.move(True)
                all_sprites.add(cannon_ball)

            if tank.send_bomb() == True:
                bomber.move(True)

            if bomber.rect.x <= tank.move_distance and bomb.dropped == False:
                bomb.set_pos((bomber.rect.x,bomber.rect.y+30))
                bomb.move(True)
                bomb.set_dropped(True)
                all_sprites.add(bomb)

            if tank.is_hit(bomb) == True:
                bomb.move(False)
                all_sprites.remove(tank)
                all_sprites.remove(bomb)

            if city.is_hit(cannon_ball) == True:
                city_sprites.remove(city)
                all_sprites.remove(laser_launcher)
                all_sprites.remove(cannon_ball)

            all_sprites.clear(self.screen,temp_surface)
            all_sprites.update()
            all_sprites.draw(self.screen)

            all_sprites.add(tank)

            pygame.display.update()

