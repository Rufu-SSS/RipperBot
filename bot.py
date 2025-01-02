import discord # type: ignore
import time
from discord.ext import commands # type: ignore
from dotenv import load_dotenv # type: ignore
from bs4 import BeautifulSoup # type: ignore
from googletrans import Translator #type: ignore
import os
import requests # type: ignore
import random # Per la comanda de bromes

# Carrega les variables d'entorn des del fitxer .env
load_dotenv()

# Obté el token del bot
TOKEN = os.getenv("TOKEN")
# Crea una instància del traductor
translator = Translator()

# Configura els intents del bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Permite escuchar eventos de miembros
intents.guilds = True

# Crea la instància del bot i tris el prefix que es farà servir
bot = commands.Bot(command_prefix="%", intents=intents)

# COMANDA GENERAL 1: Parlar amb el bot (una sola resposta)
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! How are you?")

# COMANDA GENERAL 2: Dir bromes i acudits
@bot.command()
async def joke(ctx):
    jokes = [
    "Why does a chicken coop only have two doors? Because if it had four it would be a sedan.", #Normaletes
    "Did you hear about the archaeologist that got fired? His career is in ruins.",
    "I was going to tell a sodium joke, then i thought, 'Na.'",
    "What's the easiest building to lift? A lighthouse.",
    "What did the buffalo say to her son on the first day of school? “Bison.",
    "What do you call it when a cow grows facial hair? A moo-stache.",
    "What did the beach say when the tide came in? Long time no sea.",
    "Why did the man bring his watch to the bank? He wanted to save time.",
    "What should you do if your puppy isn't feeling well? Take him to the dog-tor.",
    "What's the best way to make a bandstand? Take away their chairs.",
    "I told a bad chemistry joke once. I got no reaction.",
    "Why did the cow go to Hollywood? To be in the moo-vies.",
    "What did one wall say to the other? I'll meet you at the corner.",
    "What's the best way to catch a fish? Ask someone to throw it to you.",
    "How did the piano get locked out of its car? It lost its keys.",
    "Why did the orchestra get struck by lightning? It had a conductor.",
    "How do you make an eggroll? You push it.",
    "How many apples can you grow on a tree? All of them.", #Terriblement dolentes que son bones
    "My manager told me to have a good day. So I didn't go into work.",
    "Where do sheep go on vacation? The Baaaa-hamas.",
    ...
    ]
    await ctx.send(random.choice(jokes))

# COMANDA GENERAL 3: Mira el temps
@bot.command()
async def weather(ctx, *, city: str):
    api_key = os.getenv("WEATHER_API_KEY")  # Load the API key from the environment
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Set up the query URL
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Temperature in Celsius
        "lang": "en"  # Language in English
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:  # Successful query
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        await ctx.send(
            f"**Weather in {city_name}, {country}:**\n"
            f"- Description: {description.capitalize()}\n"
            f"- Temperature: {temperature}°C\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind speed: {wind_speed} m/s"
        )
    else:  # Error (city not found or API problem)
        error_message = data.get("message", "Unknown error")
        await ctx.send(f"Could not retrieve the weather for {city}. Error: {error_message}")

    

# COMANDA UTILITAT 1: Tradueix paraules
@bot.command()
async def translate(ctx, language: str, *, text: str):
    try:
        translated=translator.translate(text, dest=language)
        await ctx.send(f"**Original**: {text}\n**Translated to {language}**: {translated.text}")
    except Exception as e:
        await ctx.send(f"Sorry, I couldn't translate the text. Error: {e}") 

# COMANDA INFO USUARI 1: Mostra tot el perfil de l'usuari
@bot.command()
async def showprofile(ctx, user_id: str=None):
    # Si es proporciona un ID, intentem obtenir-lo amb fetch_user
    if user_id:
        try:
            # Intentem obtenir l'usuari per ID global
            member = await bot.fetch_user(user_id)
        except discord.NotFound:
            await ctx.send("No user found with that ID.")
            return
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred while fetching the user: {e}")
            return
    else:
        # Si no es proporciona un ID, utilitzem el membre que ha invocat la comanda
        member = ctx.author
    
    # Obtenir i mostrar l'avatar de l'usuari
    avatar_url = member.avatar.url if member.avatar else None
    if avatar_url:
        await ctx.send(f"{member.name}'s [pfp]({avatar_url})")  # Enllacem a l'avatar amb la paraula "pfp"
    else:
        await ctx.send(f"{member.name} does not have an avatar.")
    
    # Comprovar si l'usuari té Nitro per accedir al banner
    if member.banner:
        await ctx.send(f"{member.name}'s [banner]({member.banner.url})")  # Enllacem al banner amb la paraula "banner"
    else:
        await ctx.send(f"{member.name} does not have a banner (Nitro required).")





# COMANDA ADMIN 1: Esborra n quantitat de missatges d'un canal de text
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} Messages were deleted", delete_after=5)

# COMANDA ADMIN 2: Expulsa un usuari o bot del servidor
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked. Reason: {reason}")

# COMANDA D'AJUDA: Mostra la llista de comandes i digues que fan
bot.remove_command("help") # Elimina la comanda integrada d'ajuda
@bot.command()
async def help(ctx):
    help_message = """
**GENERAL COMMANDS**:
- `%hello`: Say hello to the bot.
- `%joke`: Hear a random joke.
- `%weather [city]`: Get the weather in a specific city.

**USER INFO COMMANDS**:
- `%showprofile [user_id]´: Show an user's pfp and banner (if they have one).

**UTILITY COMMANDS**:
- `%translate [language] [text]`: Translate text to the specified language.

**ADMIN COMMANDS**:
- `%clear [amount]`: Delete a specific number of messages in the current channel.
- `%kick [member] [reason]`: Kick a user from the server.

**HELP COMMAND**:
- '%help': Show this help message.
"""
    await ctx.send(help_message)

# Executa el bot
bot.run(TOKEN)

# L'enllaç per invitar el bot es el següent (actualment): 
# https://discord.com/oauth2/authorize?client_id=1324025663925260383&permissions=1239098534918&integration_type=0&scope=bot+applications.commands


