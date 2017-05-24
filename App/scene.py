import pygame
from pygame.locals import *
from App.MyClass.tank import *
from App.MyClass.city import *
from App.MyClass.bomber import *
from App.MyClass.laser_defense import *
from App.MyClass.bomb import *
from App.MyClass.cannon_ball import *
from App.MyClass.explosion import *

from App.constant import *

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
        pygame.font.init()

        title_font_type = os.path.join(get_font_dir(),"hammerhead.ttf")
        self.title_font = pygame.font.Font(title_font_type,30)
        self.bg_image = os.path.join(get_image_dir(),"background.png")
        self.clock = pygame.time.Clock()
        self.frame_rate = 40

    def set_background(self):
        bg_image = pygame.transform.scale( pygame.image.load(self.bg_image).convert(),(self.WIDTH,self.HEIGHT))
        self.screen.blit(bg_image,(0,0))

    def start(self):


        city_sprites = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        bomb = Bomb(self.screen,(20,40),"Bomb")

        explosion_sm = Explosion(self.screen,(50,50),"Small Explosion")
        explosion_md = Explosion(self.screen,(150,150),"Medium Explosion")
        explosion_bg = Explosion(self.screen,(300,300), "Big Explosion")

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
                        self.set_background()
                        running = False
                    if event.key == K_SPACE:
                        tank.move(True)
                    if event.key == K_r:
                        self.start()
                elif event.type == QUIT:
                    running == False

            self.set_background()
            self.screen.blit(put_text("projektile", self.title_font, CLR_WHITE), (10, 10))
            city_sprites.draw(self.screen)

            temp_surface = pygame.Surface((self.WIDTH,self.HEIGHT))
            temp_surface.fill([0,0,0])
            temp_surface.set_colorkey([0,0,0])

            if tank.fire_cannon() == True and cannon_ball.moving == False:
                cannon_ball.set_source_target(tank,city)
                cannon_ball.move(True)
                all_sprites.add(cannon_ball)

            if city.is_defense_breached(cannon_ball) == True and all_sprites.has(cannon_ball) and laser_launcher.available == True:
                laser_launcher.set_target(cannon_ball)
                laser_launcher.fire_laser = True
                if cannon_ball.is_hit(laser_launcher) == True:
                    explosion_sm.set_pos(cannon_ball.pos)
                    all_sprites.remove(cannon_ball)
                    all_sprites.add(explosion_sm)
                    bomber.move(True)


            #if city.is_hit() == True:
            #    bomber.move(True)

            if bomber.rect.x <= tank.move_distance and bomb.dropped == False:
                bomb.set_pos((bomber.rect.x+10,bomber.rect.y+30))
                bomb.move(True)
                bomb.set_dropped(True)
                all_sprites.add(bomb)

            if tank.is_hit(bomb) == True:
                bomb.move(False)
                explosion_md.set_pos((bomb.pos[0]-50,bomb.pos[1]-50))
                #tank.explode(bomb)
                all_sprites.add(explosion_md)
                all_sprites.remove(tank)
                all_sprites.remove(bomb)

            if city.is_hit(cannon_ball) == True:
                explosion_bg.set_pos(city.pos)
                city_sprites.remove(city)
                all_sprites.remove(laser_launcher)
                all_sprites.remove(cannon_ball)
                all_sprites.add(explosion_bg)

            all_sprites.clear(self.screen,temp_surface)
            all_sprites.update()
            all_sprites.draw(self.screen)

            all_sprites.add(tank)

            pygame.display.update()
            self.clock.tick(self.frame_rate)
