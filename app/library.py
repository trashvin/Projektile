import os, sys
import math
from app.constant import *

def get_image_dir():
    curr_dir = os.getcwd()
    print(curr_dir)
    return os.path.join(curr_dir,"resource/image")

def get_sound_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"resource/sound")

def get_font_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"resource/font")

def put_text(text,font,color):
    return font.render(text,True,color)

def get_projetile_VX(initial_v,angle):
    angle_rad = math.radians(angle)
    return ((initial_v) * math.cos(angle_rad))

def get_projectile_VY(initial_v,angle):
    angle_rad = math.radians(angle)
    return ((initial_v) * math.sin(angle_rad))

def get_projectile_dist_x(velocity_x,time):
    return velocity_x * time

def get_projectile_dist_y(initial_v,time,angle):
    return ((initial_v * math.sin(angle) * time) - ( 0.5 * G_CONSTANT * time *time))

def get_projectile_initial_v(angle, distance):
    return math.sqrt( (distance * G_CONSTANT)/(math.sin(2 * angle)))


def get_projectile_xy(initial_v,initial_angle,time,initial_h = 0):
    y = get_projectile_dist_y(initial_v,time,initial_angle)
    x = initial_v * math.cos(initial_angle) * time
    return (x,y)


