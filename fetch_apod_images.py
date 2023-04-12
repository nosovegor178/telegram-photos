from dotenv import load_dotenv
import os
import requests
from general_functions import downloading_image
import argparse


load_dotenv()
NASA_API = os.environ['NASA_API']
def fetch_pictures_of_the_day(directory):
    payload={

        'api_key' : NASA_API,
        'count' : 30
        
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.json()

def downloading_apod_image(images_list):
    for image in images_list:
        downloading_image(image['url'], '{1}/nasa_apod_{0}.jpg'.format(images_list.index(image)), directory)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory, where will placed pictures', default='images', nargs='?')
    args = parser.parse_args()
    
    creating_folder(args.directory)
    pictures_list = fetch_pictures_of_the_day(args.directory)
    downloading_apod_image(pictures_list)
