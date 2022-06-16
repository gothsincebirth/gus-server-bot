import discord
from discord.ext import commands


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        if member = None:
            member =





def setup(bot):
    bot.add_cog(userinfo(bot))
