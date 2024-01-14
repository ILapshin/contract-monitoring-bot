# What Does This Service Do?

This is a telegram bot that monitors daily statistics for a smart contract like [this](https://etherscan.io/address/0xaBE235136562a5C2B02557E1CaE7E8c85F2a5da0) and sends it to the specified telegram channel every time interval (say four hours).

## Run Bot

0. Clone this repo.

1. Create and activate virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies via poetry:

```bash
poetry install
```

3. Set virtual variables as follows:

```
DB_HOST=[your database host]
DB_PORT=[your database port]
DB_NAME=[your database name]
DB_PASS=[your database passwors]
DB_USER=[your database username]

WEB3_PROVIDER_URL=[your RPC provider url]
CONTRACT_ADDRESS=[target contract address] # 0xaBE235136562a5C2B02557E1CaE7E8c85F2a5da0
DISTRIBUTOR_ADDRESS=[distributor address] # 0x9A0A9594Aa626EE911207DC001f535c9eb590b34

BOT_TOKEN=[your telegram bot token]
RECEIVER_CHANNEL_ID=[target telegram channel] @smartcontractmonitoring

TIME_INTERVAL=4 # in hours
```

> This service can only operate with PostgreSQL database!

4. Run service

```bash
python main.py
```

## Test Telegram Channel

[tg channel](https://t.me/smartcontractmonitoring)
