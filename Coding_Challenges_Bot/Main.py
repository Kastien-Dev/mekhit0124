import random
import discord
import threading
import os
import time
import asyncio

from discord import role
from discord.ext import commands, tasks

TOKEN = ('NzcwMzExMDY3MTgzMzQ5Nzgy.X5buFg.b3nrwWNtXYA32HvG4NUb3jkUVfA') 
bot = commands.Bot(command_prefix='!', help_command=None, shutdown_command=None)

class Startup:
    # async def __init__(self, bot):
    #     self.bot = bot
        
    @bot.event
    async def on_ready(): 
        channel = bot.get_channel(776057663477252127)
        await channel.send("bot is online")

class GeneralCommands:
    # misc commands
    @bot.command()
    async def help(ctx): 
        halp = discord.Embed(title="Commands Anyone Can use are:", color=0x323e54)
        halp.add_field(name="!csharp", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!html", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!java", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!javascript", value="This Command Is Currently Under Construction!")
        halp.add_field(name="!python", value="This Command Is Currently Under Construction!")
        await ctx.send(embed=halp)

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

class AdminCommands:
    @bot.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin')
    async def help2(ctx):
        
        admins1 = discord.Embed(title="Admin Commands", description="These are the commands available to those who have the following roles: Owner, Head Dev, and Head Admin", color = 0x323e54)
        admins1.add_field(name="!shutdown", value="shuts down the bots code", inline=False)
        admins1.add_field(name="!roles", value="prints a list of all roles within the discord.", inline=False)
        admins1.add_field(name="!members", value="prints a list of all members within the discord", inline=False)
        admins1.add_field(name="!rolesandmembers", value="prints a list of all members within their perspective roles.")
        await ctx.send(embed=admins1)

    @bot.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin')
    async def hello(ctx):
        hellos = discord.Embed(title="Coding Challenges Bot", description="Inception Date: 11/13/2020", color = 0x323e54)
        hellos.add_field(name="Bot Information 2", value="Release Date: ", inline=False)
        hellos.add_field(name="Team:", value="Mekasu (Mee-kah-sue), Kastien (Kas-tee-in), KortaPo (Core-tah-po)", inline=False)
        hellos.add_field(name="Bot Information", value="This bot is designed to output 1 random coding challenges for JS, Java, C#, HTML, and Python into specific discord channels. It is set to a 24 hour loop that resets itself.", inline=False)
        hellos.add_field(name="Help Menu", value="To learn how to use this bot, type ```!help```", inline=False)
        hellos.add_field(name="Admin Menu", value="To learn how to use the Admin Menu, type ```!admin```", inline=False)
        await ctx.send(embed=hellos)

    # print's the roles within the discord
    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def members(ctx):
        roles = []
        for role in ctx.guild.roles:
            roles.append(role.name)
        await ctx.send(roles)

    # prints all the member's of the discord that are not bots
    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def Members(ctx):
        await ctx.send("\n ".join([member.display_name for member in ctx.guild.members if not member.bot]))

    # prints all the roles, and members within those roles that are not bots within the discord
    @bot.command()
    @commands.has_any_role('Owner','HeadDev','HeadAdmin')
    async def RolesandMembers(ctx):
        for role in ctx.guild.roles[1:]:# guild role except the everyone role
            if not role.managed: # if the role wasn't managed (managed roles are only for bots)
                await ctx.send(f"**{role.name}**:")
                for mem in role.members:
                    if not mem.bot: # if the member is a non-bot user
                        await ctx.send(mem.name)

    @bot.command()
    @commands.has_any_role('Owner','Head Dev')
    async def shutdown(ctx):
        await ctx.send(f"{ctx.author} is shutting down {bot.user.name}, and updating it.")
        await bot.logout()
        await asyncio.sleep()
        await bot.login(TOKEN, bot=True)
        await ctx.send(f"{bot.user.name} is back online!") 


bot.run(TOKEN)