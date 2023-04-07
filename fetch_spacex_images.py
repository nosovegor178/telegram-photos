from dotenv import load_dotenv
import requests
from general_functions import downloading_image


load_dotenv()
def fetch_spacex_launches(id, dir_name):
    if id == '':
        url = "https://api.spacexdata.com/v5/launches/latest"
    else:
        url = "https://api.spacexdata.com/v5/launches/{}".format(id)
    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    
    for link_num in range(5):
        downloading_image(links[link_num], '{0}/spacex_{1}.jpg'.format(dir_name, link_num))


