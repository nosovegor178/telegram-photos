import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def creating_folder(dir_name):
    if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def downloading_image(image_url, path):
    load_dotenv()
    NASA_API_KEY = os.environ['NASA_API_KEY']
    payload={
        'api_key' : NASA_API_KEY
    }
    response = requests.get(image_url, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def convert_image(image_path):
    path_to_image = os.path.split(image_path)
    basename = os.path.splitext(path_to_image[1])
    extension = urlparse(basename[1])
    return(extension[2])