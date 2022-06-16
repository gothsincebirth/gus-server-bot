import discord
from discord.ext import commands
from afks import afks


class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx, *, reason="No reason provided"):
        member = ctx.author
        if member.id in afks.keys():
            afk.pop(member.id)
        else:
            try:
                await member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        is_afk_embed = discord.Embed(title='User AFK', description=f"{member.mention} has gone AFK", color=0xFFFFFF)
        is_afk_embed.add_field(name="AFK Reason", value=reason)
        await ctx.send(embed=is_afk_embed)


def setup(bot):
    bot.add_cog(afk(bot))
