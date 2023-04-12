from dotenv import load_dotenv
import requests
from general_functions import downloading_image
import argparse


load_dotenv()
def fetch_spacex_launches(id, dir_name):
    url = "https://api.spacexdata.com/v5/launches/{}".format(id)

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    
    for link_num in range(5):
        downloading_image(links[link_num], '{0}/spacex_{1}.jpg'.format(dir_name, link_num))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id of the spacex launch, if you wil not specify, you will take photos of last launch', default='latest', nargs='?')
    parser.add_argument('directory', help='directory, where placed pictures', default='images', nargs='?')
    args = parser.parse_args()
    fetch_spacex_launches(args.id, args.directory)

# 5eb87d47ffd86e000604b38a