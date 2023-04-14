from dotenv import load_dotenv
import os
import requests
import general_functions
import argparse


def fetch_pictures_of_the_day(directory):
    payload={
        'api_key' : NASA_API_KEY,
        'count' : 30
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()

    apod_images = response.json()

    for image in apod_images:
        general_functions.downloading_image(image['url'], os.path.join('{}'.format(directory),'nasa_apod_{}.jpg'.format(apod_images.index(image)))

if __name__ == '__main__':
    load_dotenv()
    NASA_API_KEY = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory, where will placed pictures', default='images', nargs='?')
    args = parser.parse_args()
    
    general_functions.creating_folder(args.directory)
    pictures_list = fetch_pictures_of_the_day(args.directory)
