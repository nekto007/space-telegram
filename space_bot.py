import logging
from time import sleep
import telegram
import os

from config import settings

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

images_folder = 'images'
delay = 60


def send_images_to_telegram_channel(delay):
    bot = telegram.Bot(token=settings.BOT_API_KEY)

    for image in os.listdir(images_folder):
        with open('images/{}'.format(image), 'rb') as f_image:
            bot.sendPhoto(settings.CHANNEL_ID, f_image)
        sleep(delay)


def main():
    while True:
        send_images_to_telegram_channel(delay)


if __name__ == "__main__":
    main()
