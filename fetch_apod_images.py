from dotenv import load_dotenv
import os
import requests
from general_functions import downloading_image


load_dotenv()
NASA_API = os.environ['NASA_API']
def fetch_pictures_of_the_day():
    payload={

        'api_key' : NASA_API,
        'count' : 30
        
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.json()

def downloading_apod_image(images_list):
    for image in images_list:
        downloading_image(image['url'], 'images/nasa_apod_{}.jpg'.format(images_list.index(image)))

