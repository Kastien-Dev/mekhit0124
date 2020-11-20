import os
import discord
import json

from discord.ext import commands, tasks


with open('./config4.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix=',', help_command=None, shutdown_command=None)


my_api_key = 'AIzaSyAMv-E2s_88zC-ZiIe50XwDsd__STsLKto'
my_cse_id = '6d091e6cdf9452610'

class Startup: #finished     
    @bot.event
    async def on_ready():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send("I'm online! Thank you for waking me up! :smile:")

class Main:


# https://discordpy.readthedocs.io/en/latest/ use this link for references


bot.run(TOKEN)