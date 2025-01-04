from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} messages deleted.", delete_after=3)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason="No reason provided"):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked. Reason: {reason}")

async def setup(bot):
    await bot.add_cog(Admin(bot))
