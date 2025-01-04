import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMANDA INFO USUARI 1: Mostra tot el perfil de l'usuari
    @commands.command()
    async def showprofile(self, ctx, user_id: str = None):
        """Mostra el perfil complet d'un usuari pel seu ID o del mateix usuari que invoca."""
        # Si es proporciona un ID, intentem obtenir l'usuari amb fetch_user
        if user_id:
            try:
                # Obtenim l'usuari per ID global
                member = await self.bot.fetch_user(user_id)
            except discord.NotFound:
                await ctx.send("No user found with that ID.")
                return
            except discord.HTTPException as e:
                await ctx.send(f"An error occurred while fetching the user: {e}")
                return
        else:
            # Si no es proporciona un ID, utilitzem l'usuari que ha invocat la comanda
            member = ctx.author

        # Mostrar l'avatar de l'usuari
        avatar_url = member.avatar.url if member.avatar else None
        if avatar_url:
            await ctx.send(f"{member.name}'s [pfp]({avatar_url})")  # Enllaç a l'avatar amb la paraula "pfp"
        else:
            await ctx.send(f"{member.name} does not have an avatar.")

        # Comprovar si l'usuari té Nitro per accedir al banner
        if member.banner:
            await ctx.send(f"{member.name}'s [banner]({member.banner.url})")  # Enllaç al banner amb la paraula "banner"
        else:
            await ctx.send(f"{member.name} does not have a banner (Nitro required).")

def setup(bot):
    bot.add_cog(UserInfo(bot))
