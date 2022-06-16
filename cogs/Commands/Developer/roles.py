import discord
from discord.ext import commands


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roles(self, ctx):
        # checks if the user is the bot owner
        if ctx.author.id != 420584160495796225:
            return await ctx.send(
                "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
        else:
            # creates embed
            roles_embed = discord.Embed(
                title="Interaction pings",
                description="""**<@&864470410082254850> [<:GUS_gusblush:916267298766073886>] \n `This role is mentioned whenever the chat is dead\n[expect a lot of pings if you select this role]` \n\n <@&864473433605275668> [<:GUS_giveheart:916267299789488158>] \n `This role is pinged for general game updates` \n\n <@&864475268475125770> [<:GUS_hahayeah:916267299974021140>] \n `This role is pinged for guild announcements` \n\n <@&908854988279791726> [<:fluster:916267299382628353>] \n `This role is pinged randomly and is for anything miscellaneous` \n\n <@&908856403370852425> [<:GUS_pls:864601522813272064>] \n `This role is pinged for guild updates such as theme updates or rule updates or anything that involves a change in the guild` \n\n <@&913726406108807199> [<:gusdynlove:864506291312656395>] \n `This role is pinged whenever a user joins the guild to alert users to welcome them` \n\n <@&931427855794049054> [<:kissy:916267299449741312>] \n `This role is pinged whenevr it is a users birthday` \n\n <@&933658436342800444> [<:GUS_tired:916268232627855410>] \n `This role is for people above the age of 18`**  \n\n <@&933658408958197790> [<:GUS_ybsmoke:961369488652115998>] \n `This role is for people under the age of 18`\n\n <@&951377461852127252> [<:GUS_gusblush:916267298766073886>] \n `This role is pinged to alert users of a partnership`""",
                color=0xFFFFFF
            )
        await ctx.send(embed=roles_embed)
        roles_embed_2 = discord.Embed(
            title="Video game pings",
            description="**<@&933672249452560414> [<:GUS_gasmask:916268232871137301>] \n `This role is pinged for valorant related media` \n\n <@&933672253642645515> [<:GUS_hmm:916267299235827743>] \n `This role is pinged for dead by daylight related media` \n\n <@&933684799581872169> [<:GUS_nuggetboia:864658695786201088>] \n `This role is pinged for counter strike related media` \n\n <@&933684805076406362> [<:GUS_stardewglacierjr:864659323241758740>] \n `This role is pinged for ninecraft related media` \n\n <@&933684806745743412> [<:GUS_stardewprof:864659323337310208>] \n `This role is pinged for terraria related media`**",
            color=0xFFFFFF
        )
        await ctx.send(embed=roles_embed_2)

        roles_embed_3 = discord.Embed(
            title="Chat Access roles",
            description="**<@&985599522669482044> [<:GUS_gawrguraangry:864658420313227284>] \n `This role will give you access to` <#956890641047093318> \n\n <@&933684791222599730> [<:GUS_gawrguraconfused:864658422624026704>] \n `This role will give you access to` <#933693952610168852> \n\n <@&908855768349040691> [<:GUS_gawrgurahug:864658422786949140>] \n `This role will give you access to` <#864282615249764382> \n\n <@&985597822575448154> [<:GUS_gawrguralove:864658422703849512>] \n `This role will give you access to` <#955918327560167474> \n\n <@&985597849800704020> [<:GUS_gawrgurareverse:864658422946594836>] \n `This role will give you access to` <#975170809024897064>**",
            color=0xFFFFFF
        )
        await ctx.send(embed=roles_embed_3)


def setup(bot):
    bot.add_cog(roles(bot))
