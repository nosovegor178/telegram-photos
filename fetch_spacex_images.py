import general_functions
import argparse
import os
import requests


def fetch_spacex_launches(launch_id, dir_name):
    payload = {
    }
    url = "https://api.spacexdata.com/v5/launches/{}".format(launch_id)
    response = requests.get(url)
    response.raise_for_status()
    links_of_photos = response.json()['links']['flickr']['original']
    for picture_number, picture_counter in enumerate(links_of_photos):
        general_functions.download_image(
            links_of_photos[picture_number],
            payload,
            os.path.join(dir_name,
                         'spacex_{}.jpg'.format(picture_number)))


if __name__ == '__main__':
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
    fetch_spacex_launches(args.id, args.directory)
