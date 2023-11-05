import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def setup_hook():
    for filename in os.listdir('events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')

    for filename in os.listdir('commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
    

bot.run(token)
