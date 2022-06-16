import discord
from discord.ext import commands
from discord.utils import get
from afks import afks


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

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick=remove(message.author.display_name))
            except:
                pass
            no_afk_embed = discord.Embed(title="Welcome back",
                                         description=f"I've removed your AFK, <@!{message.author.id}>", color=0xFFFFFF)
            await message.channel.send(embed=no_afk_embed)

            for id, reason in afks.items():
                member = get(message.guild.members, id=id)
                if (message.refrence and member == (await message.channel.fetch_message(
                        message.refrence.message_id)).author) or member.id in message.raw_mentions:
                    is_afk_embed = discord.Embed(
                        description=f"{member.name} is currently AFK \n\n **Reason:** {reason}", color=0xFFFFFF)
                    await message.channel.send(embed=is_afk_embed)


def setup(bot):
    bot.add_cog(events(bot))
