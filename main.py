import discord
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands




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


@client.event
async def on_voice_state_update(member, before, after):
    guild = client.get_guild(803394988187582464)
    print(member,before,after)
    if after.channel.id == 819838583380508693:
        category_channel = guild.get_channel(819838582767484998)
        channel = await guild.create_voice_channel(member.name + "" + "'s Channel", overwrites=None, category=category_channel, reason=None)
        voice_channel = client.get_channel(channel.id)    
        await member.move_to(voice_channel)
        if after.channel.id == "None":
            print("a")
    else:
        return

    





client.run('ODI2MDAyNzY0OTk1MTAwNzMy.YGGJBQ.DrTZuA9nSbskRgL2rAwQWlBkKfU')