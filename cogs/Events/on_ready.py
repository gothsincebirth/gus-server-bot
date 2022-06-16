import discord
from discord.ext import commands


class on_ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="Looking over gus!", type=3)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
        print(f"{self.bot.user} is moderating over gus")

def setup(bot):
    bot.add_cog(on_ready(bot))
