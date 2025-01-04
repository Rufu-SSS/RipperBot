import os
from dotenv import load_dotenv
from discord import Intents

load_dotenv()

# Variables d'entorn
TOKEN = os.getenv("TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Intents del bot
INTENTS = Intents.default()
INTENTS.message_content = True
