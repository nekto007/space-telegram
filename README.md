# space-telegram

Используйте `fetch_spacex.py` и `fetch_nasa.py` для загрузки фотографий космоса.
`space_image_bot.py` - для постинга изображений в телеграм-канал. Автопостинг через DELAY секунд

# Как установить

Для `fetch_nasa.py` требуется получите API_KEY здесь: https://api.nasa.gov/

Для постинга фотографий вам понадобится:
1. Вы можете создать своего бота в `@BotFather` и после этого получить token
2. Придумать и создать свой телеграмм канал `@your_channel_name` и добавить в него ранее созданного бота с правами Администратора

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

ЗАполните файл configs / settings.py на основе` settings.py.example`,
затем добавьте свои ключи API и текущую монету. 

**The configuration file consists of the following fields:**

-   **NASA_API_KEY** - NASA API KEY. Требуется для получения фотографий с серверов Nasa
-   **CHANNEL_ID** - ID Telegram канала. Параметр нужен для того, чтобы telegram bot знал в какой канал отправлять фотографии.
-   **DELAY** - Задержка между публикациями фотографий в telegram канал. По умолчанию стоит 60 секунд.

#### Environment Variables

Все параметры, представленные в файле `config / settings.py`, также можно настроить с помощью переменных среды. 

```
NASA_API_KEY = 'WUtBdFbQRbu6e6b0Y8Mgkауа1g8vZZb7RHEPsD0'
BOT_API_KEY = '181972ау2121:AAHS1jFSdvyuавыавzmtUbX4aRJzHj4qtKMDELFA'
CHANNEL_ID = '-1003384007922'
DELAY = 60
```

# Пример использования

### Для сбора фотографий

```
python fetch_spacex.py
```
или
```
python fetch_nasa.py
```

### Для отправки изображений в Телеграмм-канал

```
python spaсe_image_bot.py
```

# Цель проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DVMN.org](https://dvmn.org)
