import requests

from config import BOT_TOKEN, RECEIVER_CHANNEL_ID
from bot_service import data_parsing


def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": RECEIVER_CHANNEL_ID,
        "text": data_parsing.prepare_message(),
        "parse_mode": "HTML",
    }

    requests.post(url, data=payload)
