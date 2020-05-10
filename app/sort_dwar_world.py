from world_parser import world
from exceptions import UnknownModeError

default_answer = 'Cant find any Object'

dwar_world = world()

def sort_by_mode(mode, location):
    # there are 4 game mode But sort Only need 2 mode farm and fight
    # if mode is fight sort Function Returns Available Monsters in special location
    # if mode is farm it will return Farn Available Resource in special location
    if not in ('farm', 'fight'):
        raise UnknownModeError("%s Game mode Is Unknown" % mode)

    if mode == 'farm':
        res = [c.inst_resources for c in dwar_world] 
