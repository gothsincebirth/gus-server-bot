import discord
from discord.ext import commands


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        # checks if the user is the bot owner
        if ctx.author.id != 420584160495796225:
            return await ctx.send(
                "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
        else:
            # creates the embed
            about_embed = discord.Embed(
                title="What is Gus?",
                description="Gus is a discord server created by user <@!701723208667234364> \n\n **Why Gus?** \n Well this server was originally created for general chatting but as it grew it branched out into other topics such as music and programming with a ton of other miscellaneous hobbies and interests such as anime, manga, cars and drawing and we've created chats for those topics incase you are only interested in one or mainly want to interact with people who have similar interests as yourself, and those chats are:  \n\n <#956890641047093318> - for those with interests of cars \n <#955918327560167474> - for those with an interest for programming \n <#975170809024897064> - for those who want to showcase their art \n <#864282615249764382> for music enjoyers who want to share songs or talk about music \n\n theres also a pfp category for those interested in chaging up their profile, the pfp catergory includes the chats \n\n <#889904955903868928> - for matching avatars \n <#915947414203027466> - for avatars and banners that match \n <#886525173652672512> - for random avatars \n <#889904903361798196> - for animated avatars \n <#886525195647602799> - for profile banners \n <#915951770210017300> - for anime avatars",
                # embed color
                color=0xFFFFFF)
            # embed footer
            about_embed.set_footer(text="React to this message to get verified")
            # sends embed
            await ctx.send(embed=about_embed)


def setup(bot):
    bot.add_cog(about(bot))
