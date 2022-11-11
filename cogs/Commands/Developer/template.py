import discord
from settings import bot_owner_id
from discord.ext import commands


class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def template(self, ctx):
        # checks if the user is the bot owner
        if ctx.author.id != bot_owner_id:
            return await ctx.send(
                "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
        else:
            # creates the embed
            template_embed = discord.Embed(
                title="Embed only the owner can send",
                description="[https://github.com/ka-chng/gus-server-bot](source)",
                # embed color
                color=0xFFFFFF)
            # embed footer
            template_embed.set_footer(text="This is an owner only command example")
            # sends embed
            await ctx.send(embed=template_embed)


def setup(bot):
    bot.add_cog(template(bot))
