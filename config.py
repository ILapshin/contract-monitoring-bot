import os
import json

from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

WEB3_PROVIDER_URL = os.environ.get("WEB3_PROVIDER_URL")
CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")
DISTRIBUTOR_ADDRESS = os.environ.get("DISTRIBUTOR_ADDRESS")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
RECEIVER_CHANNEL_ID = os.environ.get("RECEIVER_CHANNEL_ID")

TIME_INTERVAL = int(os.environ.get("TIME_INTERVAL")) * 60 * 60

with open("./web3_service/ABI.json", "r") as f:
    ABI = json.load(f)
