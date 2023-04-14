from dotenv import load_dotenv
import requests
import general_functions
import argparse
import os


def fetch_spacex_launches(launch_id, dir_name):
    url = "https://api.spacexdata.com/v5/launches/{}".format(launch_id)

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    
    for picture_counter in range(5):
        general_functions.downloading_image(links[picture_counter], os.path.join('{}'.format(dir_name),'spacex_{}.jpg'.format(picture_counter)))

if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id of the spacex launch, if you wil not specify, you will take photos of last launch', default='latest', nargs='?')
    parser.add_argument('directory', help='directory, where will placed pictures', default='images', nargs='?')
    
    args = parser.parse_args()
    general_functions.creating_folder(args.directory)
    fetch_spacex_launches(args.id, args.directory)
