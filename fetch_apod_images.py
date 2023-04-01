from dotenv import load_dotenv
import os
import requests
import general_functions


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

if __name__ == '__main__':
    load_dotenv()
    NASA_API = os.environ['NASA_API']

    creating_folder('images')
    downloading_apod_image(fetch_pictures_of_the_day())