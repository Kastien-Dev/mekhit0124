import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=',', help_command=None)

TOKEN = 'Nzc4ODA1NDQ2NTQ2MTYxNjc1.X7XVFw.iU4jO5A5k94mQl9G4cbgbuqvBuI'

@bot.event
async def on_ready():
    channel = bot.get_channel(776771830005497861)
    await channel.send(f"{bot.user.name} is online!")



bot.run(TOKEN)