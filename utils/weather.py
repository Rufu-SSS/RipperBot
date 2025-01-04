import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, city: str):
        api_key = os.getenv("WEATHER_API_KEY")
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric", "lang": "en"}
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            await ctx.send(f"Weather in {city_name}, {country}: {temp}°C, {desc.capitalize()}")
        else:
            await ctx.send(f"Could not retrieve weather for {city}. Error: {data.get('message')}")

async def setup(bot):
    await bot.add_cog(Weather(bot))
