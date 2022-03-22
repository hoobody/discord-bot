from lib2to3.pgen2 import token
import discord
import sys

tokenFile = open("token.txt")
token = tokenFile.readline()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(token)
tokenFile.close()