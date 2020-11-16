import random
import discord
import threading
import os
import dotenv
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN') 
bot = commands.Bot(command_prefix='!', help_command=None) # help_command=None disables the default help command in discord.py and allows the creator to write their own help command

# bot initiation process
@bot.event
async def on_ready(): 
    channel = bot.get_channel(774970601013379092) # connects bots responses for the on_ready event to a specified discord channel
    await channel.send("bot is online") # print statement

# creates a help command that users can utilize to get further assistance with this bot
@bot.command()
async def help(ctx): 
    await ctx.send("""Available Commands Are:
                    ```!shutdown```\nshuts down the bots code, and is only usable by those with the HeadDev role or higher
                    ```!csharp, !html, !java, !javascript, !python```\nthese 5 commands are currently under construction. Once we have these commands up and running, they will be usuable once every 24 hours no matter who calls the command. each command will print a coding challenge per that command in it's perspective channel under the ```Coding_Challenges``` category
                    ```!roles```\nprints a list of all roles within the discord
                    ```!members```\nprints a list of all members within the discord
                    ```!rolesandnames```\nprints a list of all members within their perspective roles
                    The ```!shutdown, !roles, !members, !rolesandnames``` commands can only be used by staff members!""")

    
@bot.command()
async def csharp(ctx):
    channel = bot.get_channel(774683687018037249)
    await channel.send('Welcome To C#! Please bare with us as this command is still under construction :)')

@bot.command()
async def html(ctx):
    channel = bot.get_channel(774683714399371316) 
    await channel.send('Welcome To HTML! Please bare with us as this command is still under construction :)')

@bot.command()
async def java(ctx):
    channel = bot.get_channel(774683618307342417)
    await channel.send('Welcome To Java! Please bare with us as this command is still under construction :)')

@bot.command()
async def javascript(ctx):
    channel = bot.get_channel(774683653728501761) 
    await channel.send('Welcome to Java Script! Please bare with us as this command is still under construction :)')

@bot.command()
async def python(ctx):
    channel = bot.get_channel(774683556077109258)
    await channel.send('Welcome To Python! Please bare with us as this command is still under construction :)')


    
# administrative commands that only these specified roles have access to
@bot.command()
@commands.has_any_role('Owner','HeadDev','HeadAdmin','Admin') # creates a command that only users with the specified role can use
async def roles(ctx):
    channel = bot.get_channel(777217963136385057)
    await channel.send(", ".join([str(r.name) for r in ctx.guild.roles if not role.managed]))

@bot.command()
@commands.has_any_role('Owner','HeadDev','HeadAdmin','Admin')
async def members(ctx):
    channel = bot.get_channel(777248699402420234)
    await channel.send("\n ".join([member.display_name for member in ctx.guild.members if not member.bot]))

@bot.command()
@commands.has_any_role('Owner','HeadDev','HeadAdmin','Admin')
async def rolesandnames(ctx):
    channel = bot.get_channel(777217963136385057)
    for role in ctx.guild.roles[1:]:# guild role except the everyone role
        if not role.managed: # if the role wasn't managed (managed roles are only for bots)
            await channel.send(f"**{role.name}**:")
            for mem in role.members:
                if not mem.bot: # if the member is a non-bot user
                    await channel.send(mem.name)

@bot.command
@commands.has_any_role('Owner','HeadDev')
async def shutdown(ctx):
    channel = bot.get_channel(774970601013379092)
    await channel.send("Shutting Down, and Updating bot\nWhen bot comes back online, it will alert us in the discord")
    await bot.close()


@bot.command
@commands.has_any_role('Owner','HeadDev')
async def restart():
    bot.reload_extension(Main)
    channel = bot.get_channel(774970601013379092)
    await channel.send("Updating {bot.user.name}")

bot.run(TOKEN)