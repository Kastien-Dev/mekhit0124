import os
import random
import discord
import threading
import time
import asyncio
import json

from discord import mentions
from discord.ext import commands, tasks

with open('./config.json', 'r') as f:
    TOKEN = json.load(f)['TOKEN']

bot = commands.Bot(command_prefix=';', help_command=None, shutdown_command=None, update_command=None, restart_command=None)

class Startup: #finished     
    @bot.event
    async def on_ready():
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send("I'm online! Thank you for waking me up! :smile:")

class ChallengeBotCommands: # need to finish
    @bot.command()
    async def csharp(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send('Welcome To C#! Please bare with us as this command is still under construction :)')
    # set to pull a random coding challenge from the C# database once every 24hrs

    @bot.command()
    async def html(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send('Welcome To HTML! Please bare with us as this command is still under construction :)')
    # set to pull a random coding challenge from the HTML database once every 24hrs

    @bot.command()
    async def java(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send('Welcome To Java! Please bare with us as this command is still under construction :)')
    # set to pull a random coding challenge from the Java database once every 24hrs

    @bot.command()
    async def javascript(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send('Welcome to Java Script! Please bare with us as this command is still under construction :)')
    # set to pull a random coding challenge from the JavaScript database once every 24hrs

    @bot.command()
    async def python(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send('Welcome To Python! Please bare with us as this command is still under construction :)')
    # set to pull a random coding challenge from the Python database once every 24hrs

class Miscellaneous: # updatable
    @bot.command()
    async def help(ctx): 
        halp = discord.Embed(title="Commands Anyone Can use are:", color=0x323e54)
        halp.add_field(name="!help", value="Prints the _help_ window")
        halp.add_field(name="Apologies", value="There are no common commands for members to use at this time.")
        halp.add_field(name="Disclaimer!", value=f"""***This can/will be changed at any given
        time. If you're ever unsure of what commands are available to you for {bot.user.name}
        then please refer back to the #available_commands channel for updated commands :)""")

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=halp)

class AdminCommands: # updateable
    @bot.command()
    # @commands.has_any_role('Owner', 'Head Dev', 'Head Admin')
    async def helpadmin(ctx):
        
        admins1 = discord.Embed(title="Coding Challenges Bot", description=f"These are the available admin commands for {bot.user.name}", color = 0x323e54)
        admins1.add_field(name="!hello", value="***_Owner and Head Dev Only_*** prints out the _About Me_ and the _other information_ about this bot. ONLY THE OWNER AND HEAD DEV MAY USE THIS COMMAND")
        admins1.add_field(name="!members", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all members within the discord", inline=False)
        admins1.add_field(name="!roles", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all roles within the discord.", inline=False)
        admins1.add_field(name="!rolesandmembers", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all members within their perspective roles.", inline=False)
        admins1.add_field(name="!shutdown", value="***_Owner, and Head Dev Only_*** shuts down the bots code", inline=False)
        admins1.add_field(name="Disclaimer!", value=f"""***This can/will be changed at any given
        time. If you're ever unsure of what commands are available to you for {bot.user.name}
        then please refer back to the #admin_commands channel for updated commands :)""")

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=admins1)

    @bot.command()
    # @commands.has_any_role('Owner', 'Head Dev')
    async def hello(ctx):
        hellos = discord.Embed(title="Coding Challenges Bot", description="Date Created: 11/13/2020", color = 0x323e54)
        hellos.add_field(name="Release Date: ", value="To Be Determined!", inline=False)
        hellos.add_field(name="Team:", value="Mekasu, Kastien, KortaPo", inline=False)
        hellos.add_field(name="Bot Information", value="This bot is designed to output 1 random coding challenges for JS, Java, C#, HTML, and Python into specific discord channels. It is set to a 24 hour loop that resets itself.", inline=False)
        hellos.add_field(name="Help Menu", value="To learn how to use this bot, type ```!help```", inline=False)
        hellos.add_field(name="Admin Menu", value="To learn how to use the Admin Menu, type ```!admin```", inline=False)

        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(embed=hellos)

    @bot.command()
    # @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def roles(ctx):
        roles = []
        for role in str.join.ctx.guild.roles[1:]:
            roles.append(role.name)
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send(", ".join(roles))

    @bot.command()
    # @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def Members(ctx):
        channel = await bot.fetch_channel(779323092542685205)
        await channel.send("\n ".join([member.display_name for member in ctx.guild.members if not member.bot]))

    @bot.command()
    # @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def RolesandMembers(ctx):
        for role in ctx.guild.roles[1:]:
            if not role.managed:
                channel = await bot.fetch_channel(779323092542685205)
                await channel.send(f"**{role.name}**:")
                for mem in role.members:
                    if not mem.bot:
                        channel = await bot.fetch_channel(779323092542685205)
                        await channel.send(mem.name)



bot.run(TOKEN)