import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('>>'))

intents = discord.Intents(messages=True)

cogfiles = [
    f"Commands.{filename[:-3]}" for filename in os.listdir("./Commands") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)
        
cogfiles = [
    f"Events.{filename[:-3]}" for filename in os.listdir("./Events") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)


bot.run(os.getenv('TOKEN')) 