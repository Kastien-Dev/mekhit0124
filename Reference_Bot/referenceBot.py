import os
import random
import discord
import threading
import time
import asyncio
import json

from discord.ext import commands, tasks
from googleapiclient.discovery import build

with open('./config.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix='!', help_command=None, shutdown_command=None)


my_api_key = 'AIzaSyAMv-E2s_88zC-ZiIe50XwDsd__STsLKto'
my_cse_id = '6d091e6cdf9452610'

class Startup:

    @bot.event
    async def on_ready():
        channel = bot.get_channel(776771830005497861)
        await channel.send("bot is online!")

class Main:

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res

bot.run(TOKEN)