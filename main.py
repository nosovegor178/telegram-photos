from dotenv import load_dotenv
import os
import requests
from urllib.parse import urlparse


def creating_folder(dir_name):
    if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def downloading_image(image_url, path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def fetch_pictures_of_the_day():
    payload={

        'api_key' : NASA_API,
        'count' : 30
        
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.json()

def convert_image(image_path):
    path_to_image = os.path.split(image_path)
    basename = os.path.splitext(path_to_image[1])
    extension = urlparse(basename[1])
    return(extension[2])


def splitting_date_of_image(image):
    date = image['date']
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    split_day = day.split(' ')[0]
    date = [year, month, split_day]
    return date

def downloading_apod(images_list):
    for image in images_list:
        downloading_image(image['url'], 'images/nasa_apod_{}.jpg'.format(images_list.index(image)))


def fetch_EPIC_pictures():
    payload={

        'api_key' : NASA_API
        
    }
    
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    list = response.json()
    return list


def downloading_EPIC_pictures(image_list):
    for img in image_list:
        date = splitting_date_of_image(img)
        downloading_image('https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?api_key={4}'.format(date[0], date[1], date[2], img['image'], NASA_API), 'images/{0}.jpg'.format(img['image']))


if __name__ == '__main__':
    load_dotenv()
    directory = 'images'
    NASA_API = os.environ['NASA_API']
    img_list = fetch_EPIC_pictures()

    creating_folder(directory)
    downloading_EPIC_pictures(img_list)