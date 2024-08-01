import requests
from projectclubs.settings import TELEGRAM_BOT_TOKEN


def send_message_to_user(chat_id, message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(url, data)

    return response.json()
