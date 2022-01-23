import os
import discord
from server import keep_running

TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is online'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if '69' in msg:
        await message.channel.send('nice')

keep_running()
client.run(os.getenv('TOKEN'))
