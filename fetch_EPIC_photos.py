from dotenv import load_dotenv
import os
import requests
import general_functions
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


def fetch_EPIC_pictures(directory):
    payload={
        'api_key' : NASA_API_KEY
    }
    
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    EPIC_pictures = response.json()

    for picture in EPIC_pictures:
        date_of_image = split_date_of_image(picture)
        year = date_of_image[0]
        month = date_of_image[1]
        day = date_of_image[2]
        picture_url = 'https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png'.format(year, month, day, picture['image'])
        path_for_downloading = os.path.join('{}'.format(directory),'{}.jpg'.format(picture['image']))
        general_functions.downloading_image(picture_url, path_for_downloading)

if __name__ == '__main__':
    load_dotenv()   
    NASA_API_KEY = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory, where will placed pictures', default='images', nargs='?')
    args = parser.parse_args()

    
    general_functions.creating_folder(args.directory)
    fetch_EPIC_pictures(args.directory)
