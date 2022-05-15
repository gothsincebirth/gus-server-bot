import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot

    @commands.command() 
    async def ping(self, ctx):
        # creates embed
        PingEmbed = discord.Embed(
            title="ping test",
            # gets bot ping
            description=f"{round(self.bot.latency * 1000)}ms"
        ) 
        # sends embed
        await ctx.reply(embed=PingEmbed)

def setup(bot):
    bot.add_cog(ping(bot))