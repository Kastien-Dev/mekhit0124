import os
import random
import discord
import threading
import time
import asyncio
import json

from discord.ext import commands, tasks

with open('./config.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix='!', help_command=None, shutdown_command=None)

class Startup:        
    @bot.event
    async def on_ready(): 
        channel = bot.get_channel(774970601013379092)
        await channel.send("bot is online")


bot.run(TOKEN)