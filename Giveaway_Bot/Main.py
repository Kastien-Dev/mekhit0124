import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=',', help_command=None)

TOKEN = ''

@bot.event
async def on_ready():
    channel = bot.get_channel(776771830005497861)
    await channel.send(f"{bot.user.name} is online!")



bot.run(TOKEN)