from dotenv import load_dotenv
import fetch_apod_images
import fetch_EPIC_photos
import fetch_spacex_images
import space_photos_bot
from general_functions import creating_folder
import os


if __name__ == '__main__':
    load_dotenv()
    directory = 'images'
    NASA_API = os.environ['NASA_API']
    creating_folder(directory)
    