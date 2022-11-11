import discord
from discord.ext import commands


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member=None):
        user = ctx.author
        if member == None:
            member == ctx.author
        userinfo_embed = discord.Embed(
            title="USER INFO",
            color=0xFFFFFF
        )
        userinfo_embed.add_field(name="USER NAME", value=f"<@!{user.id}>")
        userinfo_embed.add_field(name="DISCRIMINATOR", value=f"#{user.discriminator}", inline=False)

        
        await ctx.send(embed=userinfo_embed)






def setup(bot):
    bot.add_cog(userinfo(bot))
