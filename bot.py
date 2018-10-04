# created by Short-round
# Work with Python 3.6
import discord
from boto.s3.connection import S3Connection
import os


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Hi,'):
        msg = 'Fuck you, Dad! I do what I want!'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
