import requests
import general_functions
from dotenv import load_dotenv
import argparse
import os


def split_date_of_image(image):
    date = image['date']
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    split_day = day.split(' ')[0]
    date = [year, month, split_day]

    return date


def fetch_EPIC_pictures(directory, nasa_api_key):
    payload = {
        'api_key': nasa_api_key
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_pictures = response.json()

    for picture in epic_pictures:
        date_of_image = split_date_of_image(picture)
        year = date_of_image[0]
        month = date_of_image[1]
        day = date_of_image[2]
        picture_url = '''https://api.nasa.gov/EPIC/archive/natural/
                         {0}/{1}/{2}/png/{3}.png'''.format(
                            year, month, day, picture['image'])
        path_for_downloading = os.path.join(
            '{}'.format(directory),
            '{}.jpg'.format(picture['image']))
        general_functions.download_image(
            picture_url,
            nasa_api_key,
            path_for_downloading)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('directory',
                        help='directory, where will placed pictures',
                        default='images', nargs='?')
    args = parser.parse_args()
    os.makedirs(args.directory, exist_ok=True)
    fetch_EPIC_pictures(args.directory, nasa_api_key)
