import discord
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason="No reason provided"):
        log_channel = 965394557078474783
        guild = ctx.guild
        ban_embed = discord.Embed(
            description=f"{member.mention} has been banned",
            color=0xFFFFFF
        )
        ban_embed.add_field(name="Reason: ", value=reason, inline=False)
        ban_embed.set_thumbnail(url=f"{self.bot.icon}")
        await ctx.reply(embed=ban_embed)
        await log_channel.send(embed=ban_embed)
        await guild.ban(user=member)


def setup(bot):
    bot.add_cog(ban(bot))
