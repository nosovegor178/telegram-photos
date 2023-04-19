from dotenv import load_dotenv
import os
import requests
import general_functions
import argparse


def fetch_pictures_of_the_day(directory, nasa_api_key):
    payload={
        'api_key' : nasa_api_key,
        'count' : 30
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()

    apod_images = response.json()

    for image in apod_images:
        general_functions.download_image(image['url'], nasa_api_key, os.path.join('{}'.format(directory),'nasa_apod_{}.jpg'.format(apod_images.index(image))))

if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory, where will placed pictures', default='images', nargs='?')
    args = parser.parse_args()
    
    os.makedirs(args.directory, exist_ok=True)
    fetch_pictures_of_the_day(args.directory, nasa_api_key)
