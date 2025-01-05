import discord
from discord.ext import commands
import random
import os
import requests
from googletrans import Translator
from utils.weather import get_weather

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMANDA SLASH 1: Bromes
    @discord.app_commands.command(name="joke", description="Get a random joke from Jack")
    async def joke_slash(self, interaction: discord.Interaction):
        jokes = [
            "Why does a chicken coop only have two doors? Because if it had four it would be a sedan.",
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
            "How many apples can you grow on a tree? All of them.",
            "My manager told me to have a good day. So I didn't go into work.",
            "Where do sheep go on vacation? The Baaaa-hamas."
        ]
        await interaction.response.send_message(random.choice(jokes))

    # Comanda Slash: Temps (Weather)
    @discord.app_commands.command(name="weather", description="Get the weather for a city")
    async def slash_weather(self, interaction: discord.Interaction, city: str):
        try:
            weather_data = get_weather(city)
            response = (
                f"**Weather in {weather_data['city']}, {weather_data['country']}:**\n"
                f"- Description: {weather_data['description'].capitalize()}\n"
                f"- Temperature: {weather_data['temperature']}°C\n"
                f"- Humidity: {weather_data['humidity']}%\n"
                f"- Wind speed: {weather_data['wind_speed']} m/s"
            )
            await interaction.response.send_message(response)
        except ValueError as e:
            await interaction.response.send_message(str(e))
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}")

    # COMANDA SLASH 3: Traductor
    @discord.app_commands.command(name="translate", description="Translate text to another language")
    async def translate(self, interaction: discord.Interaction, language: str, *, text: str):
        translator = Translator()  # Crear una instància del traductor
        try:
            translated = translator.translate(text, dest=language)
            await interaction.response.send_message(f"**Original**: {text}\n**Translated to {language}**: {translated.text}")
        except Exception as e:
            await interaction.response.send_message(f"Sorry, I couldn't translate the text. Error: {e}")

    # COMANDA SLASH 4: Mostrar perfil de l'usuari
    @discord.app_commands.command(name="showprofile", description="Show a user's profile")
    async def showprofile_slash(self, interaction: discord.Interaction, user_id: str = None):
        # Si es proporciona un ID d'usuari
        if user_id:
            try:
                member = await self.bot.fetch_user(user_id)  # Obtenir l'usuari per ID
            except discord.NotFound:
                await interaction.response.send_message("No user found with that ID.")
                return
            except discord.HTTPException as e:
                await interaction.response.send_message(f"An error occurred while fetching the user: {e}")
                return
        else:
            # Si no es proporciona un ID, agafem l'usuari que invoca la comanda
            member = interaction.user
        
        # Obtenir l'avatar de l'usuari
        avatar_url = member.avatar.url if member.avatar else None
        if avatar_url:
            response_message = f"{member.name}'s [pfp]({avatar_url})"
        else:
            response_message = f"{member.name} does not have an avatar."
        
        # Comprovar si l'usuari té Nitro i obtenir el banner
        if member.banner:
            banner_url = member.banner.url
            response_message += f"\n{member.name}'s [banner]({banner_url})"
        else:
            response_message += f"\n{member.name} does not have a banner (Nitro required)."
        
        # Enviar la resposta només una vegada
        await interaction.response.send_message(response_message)

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
