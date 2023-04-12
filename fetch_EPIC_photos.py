from dotenv import load_dotenv
import os
import requests
from general_functions import downloading_image


load_dotenv()
NASA_API = os.environ['NASA_API']
def splitting_date_of_image(image):
    date = image['date']
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    split_day = day.split(' ')[0]
    date = [year, month, split_day]
    return date


def fetch_EPIC_pictures():
    payload={

        'api_key' : NASA_API
        
    }
    
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pct_list = response.json()
    return pct_list


def downloading_EPIC_pictures(image_list):
    for img in image_list:
        date_of_image = splitting_date_of_image(img)
        downloading_image('https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?api_key={4}'.format(date_of_image[0], date_of_image[1], date_of_image[2], img['image'], NASA_API), 'images/{0}.jpg'.format(img['image']))

if __name__ == '__main__':
    image_list = fetch_EPIC_pictures()
    downloading_EPIC_pictures(image_list)