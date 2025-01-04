import discord
from discord.ext import commands
from utils.translation import translate_text
from utils.weather_api import get_weather

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMANDA GENERAL 3: Mira el temps
    @commands.command()
    async def weather(self, ctx, *, city: str):
        result = get_weather(city)
        await ctx.send(result)

    # COMANDA UTILITAT 1: Traducció de text
    @commands.command()
    async def translate(self, ctx, language: str, *, text: str):
        result = translate_text(language, text)
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Utility(bot))
