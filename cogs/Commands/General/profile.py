import discord
from discord.ext import commands


class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member: discord.Member=None):
        user = ctx.author
        if member == None:
            member == ctx.author
        profile_embed = discord.Embed(
            title="USER PROFILE",
            color=0xFFFFFF
        )
        profile_embed.add_field(name= "",value="",inline=False)
        
        await ctx.send(embed=profile_embed)


def setup(bot):
    bot.add_cog(profile(bot))
