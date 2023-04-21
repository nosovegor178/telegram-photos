import requests
import general_functions
import argparse
import os
from dotenv import load_dotenv


def fetch_spacex_launches(launch_id, dir_name, nasa_api_key):
    url = "https://api.spacexdata.com/v5/launches/{}".format(launch_id)

    response = requests.get(url)
    response.raise_for_status()

    links_of_photos = response.json()['links']['flickr']['original']
    for picture_counter in links_of_photos:
        general_functions.download_image(
            links_of_photos[links_of_photos.index(picture_counter)],
            nasa_api_key,
            os.path.join('{}'.format(dir_name),
                         'spacex_{}.jpg'.format(
                            links_of_photos.index(picture_counter))))


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'id',
        help='''id of the launch, if you won`t specify,
        you will take photos of last launch''',
        default='latest',
        nargs='?')
    parser.add_argument(
        'directory',
        help='directory, where will placed pictures',
        default='images',
        nargs='?')
    args = parser.parse_args()
    os.makedirs(args.directory, exist_ok=True)
    fetch_spacex_launches(args.id, args.directory, nasa_api_key)
