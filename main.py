import os

import openai

from bot import DiscordBot
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

bot = DiscordBot(discord_token, openai_api_key)

bot.run()
