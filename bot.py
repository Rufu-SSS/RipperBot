import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import tracemalloc

tracemalloc.start()
# Carrega variables d'entorn
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intents i configuració del bot
intents = discord.Intents.default()
intents.message_content = True  # Permet llegir el contingut dels missatges
intents.members = True  # Si necessites interactuar amb membres
bot = commands.Bot(command_prefix="%", intents=intents)


# Carrega automàticament tots els cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename} successfully.")
            except Exception as e:
                print(f"Failed to load {filename}: {type(e).__name__}: {e}")



# Sincronitzar les slash commands
@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()  # Sincronitzar el comando tree
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

async def main():
    async with bot:
        await load_cogs()  # Carrega tots els cogs

asyncio.run(main())
