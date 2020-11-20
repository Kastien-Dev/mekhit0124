import os
import random
import discord
import threading
import time
import asyncio
import json

from discord.ext import commands, tasks
from discord import Embed

with open('./config2.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix='!', help_command=None, shutdown_command=None, info_command=None, list_command=None, List_command=None)

class Startup: #finished     
    @bot.event
    async def on_ready():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send("I'm online! Thank you for waking me up! :smile:")
    @bot.event
    async def on_join():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(f"{user.name} has joined {bot.user.name}!")

    @bot.event
    async def on_leave():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(f"{user.name} has left {bot.user.name}!")

class Miscellaneous: # updatable
    @bot.command()
    async def buthelp(ctx): 
        hilp = discord.Embed(name="Bot Commands For General Users")
        hilp.add_field(name="Coding Challenges Bot", value="This bot is controlled by the dev team, and has no general commands at this time.")
        hilp.add_field(name="Doctor Giveaway Bot", value="This bot is set only controlled by the dev team, and has no general commands at this time.")
        hilp.add_field(name="Reference Bot", value="This bot is currently under construction. Please check back later.")
        hilp.add_field(name="Butler Bot", value="Type /buthelp to get this help menu")
        hilp.add_field(name="Disclaimer!", value=f"""***This can/will be changed at any given
        time. If you're ever unsure of what commands are available to you for {bot.user.name}
        then please refer back to the #available_commands channel for updated commands :)""", inline=False)

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=hilp)

class Info: #updatable
    @bot.command()
    async def info(ctx):

        info1 = discord.Embed(title="Butler Bot", value="""Hi and Welcome to this breif explination of what Butler can do :D
                              Butler is an all-around general use bot from making/removing channels in discord, to verifying
                              that users have agreed to your ToS. Type ```!help``` to see a live of available commands for
                              those who are general users, and type !helpadmin to see a list of available admin commands. The
                              commands are set up to only allow users to use certain commands that meet certain role requirements.
                              Any futher questions, or concerns, when it comes to Butler, please DM shellbyy#8025 on discord""")

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=info1)

    @bot.command()
    @commands.is_owner()
    async def hello(ctx):
        hellos = discord.Embed(title="Coding Challenges Bot", description="Date Created: 11/13/2020", color = 0x323e54)
        hellos.add_field(name="Release Date: ", value="To Be Determined!", inline=False)
        hellos.add_field(name="Team:", value="Mekasu, Kastien, KortaPo", inline=False)
        hellos.add_field(name="Bot Information", value="This bot is designed to output 1 random coding challenges for JS, Java, C#, HTML, and Python into specific discord channels. It is set to a 24 hour loop that resets itself.", inline=False)
        hellos.add_field(name="Help Menu", value="To learn how to use this bot, type ```!help```", inline=False)
        hellos.add_field(name="Admin Menu", value="To learn how to use the Admin Menu, type ```!admin```", inline=False)

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=hellos)





bot.run(TOKEN)