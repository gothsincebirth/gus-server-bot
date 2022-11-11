import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        # creates embed
        ping_embed = discord.Embed(
            title="ping test",
            # gets bot ping
            description=f"{round(self.bot.latency * 1000)}ms",
            color=0xFFFFFF
        )
        # sends embed
        await ctx.reply(embed=ping_embed)


def setup(bot):
    bot.add_cog(ping(bot))
