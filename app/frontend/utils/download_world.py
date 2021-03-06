import os
import requests
import pathlib
from time import sleep
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def download_world(filename='./world.txt'):
   if os.path.isdir("locations"):
       print("Files are Alreade downloaded")
       return False
   else:
       url = 'http://w1.dwar.ru/images/data/locale/ru/xml_map/{xml_name}'
       with open(filename, mode='r') as fp:
           names = fp.read().split()
           print(len(names))
       currdir_abs_path = pathlib.Path().absolute()
           
       for name in names:
           try:
               response = requests.get(url.format(xml_name=name))
               if response.status_code == 200:
                   os.mkdir('locations') 
                   with open(f'locations/{name}', 'wb') as fp:
                       print("Downloading", response.content)
                       
                       fp.write(response.content)
               else:
                   print("Wrong Status Code")
           except requests.exceptions.ConnectionError as e:
               print(e)
               print("Please <Check insternet Connection>")
               sys.exit()
       print("Download Finished Succesfully")
