import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carregar variables d'entorn
load_dotenv()

# Configurar el bot
intents = discord.Intents.default()
intents.members = True  # Necessari per a comandes que involucren membres
intents.message_content=True
bot = commands.Bot(command_prefix="%", intents=intents)  # Prefix per a comandes tradicionals

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


# Càrrega dels cogs en l'inici

# Iniciar el bot amb el token del fitxer .env
async def main():
    async with bot:
        await load_cogs()

# Carregar cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')  # Confirmació que el bot està en línia
    await load_cogs()

bot.run(os.getenv("TOKEN"))