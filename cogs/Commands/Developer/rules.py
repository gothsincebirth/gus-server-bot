import discord
from discord.ext import commands


class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx):
        # checks if the user is the bot owner
        if ctx.author.id != 420584160495796225:
            return await ctx.send(
                "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
        else:
            # creates the embed
            rules_embed = discord.Embed(
                title="Chat Rules",
                description="""** `1` No discrimination of any level
            `2` Common sense is required
            `3` No threatning of any level that includes DOXING, DDOSING
            `4` No spamming chats
            `5` Respect all chats and their purposes
            `6` No sending any form of media that users might find offensive or triggering
            `7` Follow Discord TOS
            `8` Follow Discord GUIDELINES
            `9` Respect everyone in the server
            `10` No political or religious talk in chat
            `11` No promoting content without consent
            `12` No sharing private information without consent
            `13` No targetting a group of individuals
            `14` No hate speech or trolling**
            """,
                # embed color
                color=0xFFFFFF)
            # footer
        rules_embed.set_footer(
            text="Staff members have the right to punish any users even if the offense is not listed on the rules")
        # sends the embed 
        await ctx.send(embed=rules_embed)
        # creates second embed
        rules_embed_2 = discord.Embed(
            # embed color
            color=0xFFFFFF
        )
        # second embed image
        rules_embed_2.set_image(
            url="https://media.discordapp.net/attachments/923546020049219625/975161751739990036/aesthetic-anime-gif-12-737423972.gif?width=384&height=213")
        # sends second embed
        await ctx.send(embed=rules_embed_2)


def setup(bot):
    bot.add_cog(rules(bot))
