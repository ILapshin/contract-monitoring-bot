import time

from web3_service import service
from database.database import Base, engine
from bot_service import data_fetching
from config import TIME_INTERVAL
from bot_service import bot


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    while True:
        data_fetching.fetch_events()
        bot.send_message()
        time.sleep(TIME_INTERVAL)
