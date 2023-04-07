import os
import requests
from urllib.parse import urlparse


def creating_folder(dir_name):
    if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def downloading_image(image_url, path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def convert_image(image_path):
    path_to_image = os.path.split(image_path)
    basename = os.path.splitext(path_to_image[1])
    extension = urlparse(basename[1])
    return(extension[2])