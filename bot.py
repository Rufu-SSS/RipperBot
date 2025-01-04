import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega variables d'entorn
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intents i configuració del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents)

# Carrega automàticament tots els cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

async def main():
    async with bot:
        await load_cogs()  # Carrega tots els cogs
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
