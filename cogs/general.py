import discord
from discord.ext import commands
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}! How are you?")

    @commands.command()
    async def joke(self, ctx):
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
        "How many apples can you grow on a tree? All of them.", 
        "My manager told me to have a good day. So I didn't go into work.",
        "Where do sheep go on vacation? The Baaaa-hamas.",
        ...
        ]
        await ctx.send(random.choice(jokes))

   # Afegir altres comandes generals aquí (per exemple, per mostrar un missatge de benvinguda o informació bàsica)
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")

   # Dir literalment hola
    @commands.command(name="hi")
    async def hi(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(General(bot))
