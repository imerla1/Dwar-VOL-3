import os
import xml.etree.cElementTree as et
from collections import namedtuple
import pathlib

def world():

    locations_dir =  os.path.join(pathlib.Path().absolute(), 'locations')
    if os.path.isdir(locations_dir):
        base_url = 'http://w1.dwar.ru/hunt_conf.php?mode=hunt_farm&area_id={}&instance_id=0'
        world = []
        data = namedtuple('instance', 'inst_name inst_id inst_url inst_resources monsters')
        for location in os.listdir(locations_dir):
            tree = et.parse(os.path.join(locations_dir, location)) if location.endswith('xml') else False
            if tree:
                root = tree.getroot()
                for child in root.findall('area/location'):
                    
                    location_name = child.getchildren()[0].text
                    location_id = child.attrib['id']
                    location_url = base_url.format(location_id)
                    all_resource = []
                    
                    for obj in child.getchildren():
                        if obj.tag == 'object':
                            for res in obj.getchildren():
                                if res.tag == 'item':
                                    all_resource.append(res.text)
                    if not all_resource
                        inst = data(location_name, location_id, location_url, None, None)
                    # world.append(inst)
        return world
    else:
        print("locations directory doesnt exist Please first run download_world.py")

x = world()
print(x)