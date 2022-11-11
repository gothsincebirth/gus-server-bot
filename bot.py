import discord
from dotenv import load_dotenv # dotenv required for the .env file used to store our token
from discord.ext import commands
from settings import bot_owner_id
import os # os required for dotenv 

load_dotenv()
intents = discord.Intents().all() # setting up intents
bot = commands.Bot(command_prefix=">", intents=intents) # bot prefix

# cog setup
for fn in os.listdir("./cogs/Commands/Developer"): 
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.Commands.Developer.{fn[: -3]}")

for fn in os.listdir("./cogs/Commands/General"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.Commands.General.{fn[: -3]}")

for fn in os.listdir("./cogs/Events"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.Events.{fn[: -3]}")

for fn in os.listdir("./cogs/Commands/Moderation"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.Commands.Moderation.{fn[: -3]}")
# end of cog setup

# developer cog commands
@bot.command()
async def load(ctx, extension):
    if ctx.author.id != bot_owner_id:
        return await ctx.send(
            "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        bot.load_extension(extension)
        load_cog_embed = discord.Embed(title="Cog loaded", color=0xFFFFFF)
        await ctx.send(embed=load_cog_embed)


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id != bot_owner_id:
        return await ctx.send(
            "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        bot.unload_extension(extension)
        unload_cog_embed = discord.Embed(title="Cog unloaded", color=0xFFFFFF)
        await ctx.send(embed=unload_cog_embed)


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id != bot_owner_id:
        return await ctx.send(
            "Only the bot developer can use this command")  # replies to the message if the user is not bot owner
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        bot.reload_extension(extension)
        reload_cog_embed = discord.Embed(title="Cog Reloaded", color=0xFFFFFF)
        await ctx.send(embed=reload_cog_embed)
# end of developer cog commands

# load token
bot.run(os.getenv('TOKEN'))
