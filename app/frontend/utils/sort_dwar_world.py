from world_parser import world
from exceptions import UnknownModeError

default_answer = 'Cant find any Object'

dwar_world = world()

def sort_by_mode(mode, location):
    # there are 4 game mode But sort Only need 2 mode farm and fight
    # if mode is fight sort Function Returns Available Monsters in special location
    # if mode is farm it will return Farn Available Resource in special location
    if mode not in ('farm', 'fight'):
        raise UnknownModeError("%s Game mode Is Unknown" % mode)

    
    monsters = [loc.monsters for loc in dwar_world if loc.inst_name==location]
    resources = [loc.inst_resources for loc in dwar_world if loc.inst_name==location]
    if mode == 'farm':
        return type(resources)
    if mode == 'fight':
        return type(monsters)