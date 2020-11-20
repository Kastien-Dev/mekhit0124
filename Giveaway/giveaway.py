import os
import random
import discord
import threading
import time
import asyncio
import json

from discord.ext import commands, tasks

with open('./config3.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix='/', help_command=None, shutdown_command=None)
      
class Startup: #finished     
    @bot.event
    async def on_ready():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send("I'm online! Thank you for waking me up! :smile:")



bot.run(TOKEN)