import discord
from discord.ext import commands
from settings import guild_name

class on_ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name=f"Looking over {guild_name}", type=3)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
        print(f"{self.bot.user} is moderating over {guild_name}")

def setup(bot):
    bot.add_cog(on_ready(bot))
