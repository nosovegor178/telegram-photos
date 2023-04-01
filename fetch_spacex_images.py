from dotenv import load_dotenv
import os
import requests
import general_functions

def fetch_spacex_launches(id, dir_name):
    if id == '':
        url = "https://api.spacexdata.com/v5/launches/latest"
    else:
        url = "https://api.spacexdata.com/v5/launches/{}".format(id)
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    response.raise_for_status()
    
    for link_num in range(5):
        downloading_image(links[link_num], '{0}/spacex_{1}.jpg'.format(dir_name, link_num))


if __name__ == "__main__":
    id = input('Введите ID запуска SpaceX. Если хотите увидеть последний запуск, то оставьте пустым.')
    dir = 'images'

    creating_folder(dir)
    fetch_spacex_launches(id, dir)
