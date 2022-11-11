import discord
from discord.ext import commands
from discord.utils import get


def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk


class events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Events have been loaded')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            missing_arg_embed = discord.Embed(title="You are missing required arguments", color=0xFFFFFF)
            await ctx.send(embed=missing_arg_embed)

        elif isinstance(error, commands.errors.CommandNotFound):
            command_not_found_embed = discord.Embed(title="Command not found", color=0xFFFFFF)
            await ctx.send(embed=command_not_found_embed)

        elif isinstance(error, commands.errors.BadArgument):
            bad_data_embed = discord.Embed(title="Data type passed is invalid", color=0xFFFFFF)
            await ctx.send(embed=bad_data_embed)

        elif isinstance(error, commands.errors.CheckFailure):
            no_permissions_embed = discord.Embed(title="You are missing the required permissions to use this command",
                                                 color=0xFFFFFF)
            await ctx.send(embed=no_permissions_embed)
        else:
            raise error



def setup(bot):
    bot.add_cog(events(bot))
