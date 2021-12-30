import os

import requests
import urllib3

urllib3.disable_warnings()


def fetch_spacex_launch(folder):
    url = 'https://api.spacexdata.com/v3/launches/101'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    images_url = response.json()
    for number, url in enumerate(images_url['links']['flickr_images']):
        response = requests.get(url)
        filename = f'spacex{number}'
        with open(f'{folder}/{filename}.jpg', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    folder = 'images'
    os.makedirs(folder, exist_ok=True)
    fetch_spacex_launch(folder)
