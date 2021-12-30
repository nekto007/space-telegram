import os
from datetime import datetime
from os.path import (
    split,
)

import requests
import urllib3

from config import settings

urllib3.disable_warnings()


def fetch_nasa_images(folder):
    url = 'https://api.nasa.gov/planetary/apod'
    parameters = {'api_key': settings.NASA_API_KEY, 'count': 20}
    response = requests.get(url, params=parameters, verify=False)
    response.raise_for_status()
    for data in response.json():
        image_url = data['url']
        response = requests.get(image_url)
        filename = os.path.basename(image_url)
        with open(f'{folder}/{filename}', 'wb') as file:
            file.write(response.content)


def fetch_nasa_epic_images(folder):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    parameters = {'api_key': settings.NASA_API_KEY}
    response = requests.get(url, params=parameters, verify=False)
    response.raise_for_status()
    for data in response.json():
        date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        year = date.year
        month = date.month
        day = date.day
        image_name = data["image"]
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
        parameters = {'api_key': settings.NASA_API_KEY}
        response = requests.get(image_url, params=parameters)
        filename = os.path.basename(image_name)
        with open(f'{folder}/{filename}', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    folder = 'images'
    os.makedirs(folder, exist_ok=True)
    fetch_nasa_images(folder)
    fetch_nasa_epic_images(folder)
