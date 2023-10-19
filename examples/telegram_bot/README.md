# Telegram Bot
Simple Telegram bot to showcase how to connect a Telegram bot using the token. 

## Pre-configuration
Before starting, a Telegram bot token from the Telegram Bot Father should be generated (check the [tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) on how to generate a token).

Once a token is obtained, make sure to add it to your config.ini file: 

```ini
[telegram_platform]
telegram.token = YOUR-BOT-TOKEN
```

## Run Bot
To start, simply execute:
```bash
python ./telegram_bot.py
```

The bot will then be available as the bot user your token is associated with. 