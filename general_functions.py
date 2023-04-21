import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def download_image(image_url, nasa_api_key, path):
    payload = {
        'api_key': nasa_api_key
    }
    response = requests.get(image_url, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_image_expansion(image_path):
    path_to_image = os.path.split(image_path)
    basename = os.path.splitext(path_to_image[1])
    extension = urlparse(basename[1])
    return extension[2]


if __name__ == '__main__':
    load_dotenv()
