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

bot = commands.Bot(command_prefix='!', help_command=None, shutdown_command=None, update_command=None, restart_command=None)

class Startup:        
    @bot.event
    async def on_ready(): 
        channel = await bot.fetch_channel(774970601013379092)
        await channel.send("bot is online")

class ChallengeBotCommands:
    @bot.command()
    async def csharp(ctx):
        await ctx.send('Welcome To C#! Please bare with us as this command is still under construction :)')

    @bot.command()
    async def html(ctx):
        await ctx.send('Welcome To HTML! Please bare with us as this command is still under construction :)')

    @bot.command()
    async def java(ctx):
        await ctx.send('Welcome To Java! Please bare with us as this command is still under construction :)')

    @bot.command()
    async def javascript(ctx):
        await ctx.send('Welcome to Java Script! Please bare with us as this command is still under construction :)')

    @bot.command()
    async def python(ctx):
        await ctx.send('Welcome To Python! Please bare with us as this command is still under construction :)')

class Miscellaneous:
    @bot.command()
    async def help(ctx): 
        halp = discord.Embed(title="Commands Anyone Can use are:", color=0x323e54)
        halp.add_field(name="!help", value="Prints he _help_ window")
        halp.add_field(name="!csharp", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!html", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!java", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!javascript", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!python", value="This Command Is Currently Under Construction!")
        halp.add_field(name="Disclaimer!", value=f"***This can/will be changed at any given time. If you're ever unsure of what commands are available to you for {bot.user.name} then please refer back to the {bot.fetch_channel(779245084600303646).mention} channel for updated commands :)")

        await ctx.send(embed=halp)

class AdminCommands:
    @bot.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin')
    async def helpadmin(ctx):
        
        admins1 = discord.Embed(title="Coding Challenges Bot", description=f"These are the available admin commands for {bot.user.name}", color = 0x323e54)
        admins1.add_field(name="!hello", value="***_Owner and Head Dev Only_*** prints out the _About Me_ and the _other information_ about this bot. ONLY THE OWNER AND HEAD DEV MAY USE THIS COMMAND")
        admins1.add_field(name="!members", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all members within the discord", inline=False)
        admins1.add_field(name="!roles", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all roles within the discord.", inline=False)
        admins1.add_field(name="!rolesandmembers", value="***_Owner, Head Dev, and Head Admin Only_*** prints a list of all members within their perspective roles.", inline=False)
        admins1.add_field(name="!shutdown", value="***_Owner, and Head Dev Only_*** shuts down the bots code", inline=False)
        admins1.add_field(name="Disclaimer!", value=f"***This can/will be changed at any given time. If you're ever unsure of what commands are available to you for {bot.user.name} then please refer back to the {bot.fetch_channel(779245262924677130).mention} channel for updated commands :)")
        await ctx.send(embed=admins1)

    @bot.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def hello(ctx):
        hellos = discord.Embed(title="Coding Challenges Bot", description="Inception Date: 11/13/2020", color = 0x323e54)
        hellos.add_field(name="Bot Information 2", value="Release Date: ", inline=False)
        hellos.add_field(name="Team:", value="Mekasu (Mee-kah-sue), Kastien (Kas-tee-in), KortaPo (Core-tah-po)", inline=False)
        hellos.add_field(name="Bot Information", value="This bot is designed to output 1 random coding challenges for JS, Java, C#, HTML, and Python into specific discord channels. It is set to a 24 hour loop that resets itself.", inline=False)
        hellos.add_field(name="Help Menu", value="To learn how to use this bot, type ```!help```", inline=False)
        hellos.add_field(name="Admin Menu", value="To learn how to use the Admin Menu, type ```!admin```", inline=False)
        await ctx.send(embed=hellos)

    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def roles(ctx):
        roles = []
        for role in str.join.ctx.guild.roles[1:]:
            roles.append(role.name)
        await ctx.send(", ".join(roles))

    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def Members(ctx):
        await ctx.send("\n ".join([member.display_name for member in ctx.guild.members if not member.bot]))

    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def RolesandMembers(ctx):
        for role in ctx.guild.roles[1:]:
            if not role.managed:
                await ctx.send(f"**{role.name}**:")
                for mem in role.members:
                    if not mem.bot:
                        await ctx.send(mem.name)

    @bot.command()
    @commands.is_owner()
    async def update(ctx):
        channel = await bot.fetch_channel(774970601013379092)
        await channel.send(f"{ctx.author} has killed {bot.user.name}")
        try:
            bot.clear()
        except:
            pass
        finally:
            channel = await bot.fetch_channel(774970601013379092)
            await channel.send(f"{ctx.author} has brought {bot.user.name} back to life!")
            os.system("/home/shellbyy/Desktop/mekhit0124/Coding_Challenges_Bot/ python3 main.py /c")


bot.run(TOKEN)