import discord
from discord.ext import commands

class boosters(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot

    @commands.command() 
    async def boosters(self, ctx):
        # checks if the user is the bot owner
        if ctx.author.id != 420584160495796225:
            return await ctx.send("Only the bot developer can use this command") # replies to the message if the user is not bot owner 
        else:
            # creates the embed
            BoosterEmbed = discord.Embed( 
                title="Thank you for choosing to boost Gus",
                description="**Because of the decision to boost Gus you are entilted to perks** \n\n `1` You get a custom role of your choice \n `2` Dyno byapss and image perms \n `3` Black and white color roles",
                # embed color
                color=0xFFFFFF
            )
            # sends embed
            await ctx.send(embed=BoosterEmbed)

def setup(bot):
    bot.add_cog(boosters(bot))