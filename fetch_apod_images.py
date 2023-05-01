from dotenv import load_dotenv
import os
import requests
import general_functions
import argparse


def fetch_pictures_of_the_day(directory, nasa_api_key):
    count_of_images = 30
    payload = {
        'api_key': nasa_api_key,
        'count': count_of_images
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    apod_images = response.json()
    for image_number, image in enumerate(apod_images):
        path_to_image = os.path.join(directory,
                                     'nasa_apod_{}.jpg'.format(image_number))
        general_functions.download_image(image['url'],
                                         payload,
                                         path_to_image)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('directory',
                        help='directory, where will placed pictures',
                        default='images',
                        nargs='?')
    args = parser.parse_args()
    os.makedirs(args.directory, exist_ok=True)
    fetch_pictures_of_the_day(args.directory, nasa_api_key)
