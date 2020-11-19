import discord
from discord.ext import commands
from googleapiclient.discovery import build

my_api_key = 'AIzaSyAMv-E2s_88zC-ZiIe50XwDsd__STsLKto'
my_cse_id = '6d091e6cdf9452610'

bot = commands.Bot(command_prefix='.', help_command=None)

TOKEN = ''

@bot.event
async def on_ready():
    channel = bot.get_channel(776771830005497861)
    await channel.send("bot is online!")

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

bot.run(TOKEN)