import os, sys

def get_image_dir():
    curr_dir = os.getcwd()
    print(curr_dir)
    return os.path.join(curr_dir,"Images")

def get_sound_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"Sound")