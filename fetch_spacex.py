import os

import requests
import urllib3

urllib3.disable_warnings()


def fetch_spacex_launch(folder):
    url = 'https://api.spacexdata.com/v3/launches/101'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    url_images = response.json()
    for number, url in enumerate(url_images['links']['flickr_images']):
        response = requests.get(url)
        filename = 'spacex' + str(number)
        with open(folder + '/' + filename + '.jpg', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    folder = 'images/spacex'
    if not os.path.exists(folder):
        os.makedirs(folder)
    fetch_spacex_launch(folder)
