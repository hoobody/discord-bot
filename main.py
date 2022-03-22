import discord

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

token = "OTU1NjMxMTk5NzE0NDQzMjk0.Yjke6A.bgvRD-EfcOK7y84iq6YICXFR9pg"
client.run(token)