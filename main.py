from inspect import EndOfBlock
import discord
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands
from discord.ext.commands.core import command









client = commands.Bot(command_prefix = "!",description='I am a VoiceChannel Bot, DM Sand#4193 for assistence')


#cogs
cogs = ['cogs.voicestate']

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'could not load cog {cog}: {str(e)}')


#-----------------------------------------------



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Out for !help"))


#new channel on join
@client.event
async def on_voice_state_update(member, before, after):
    global cat
    #print("aaa")
    guild = member.guild
    channel = discord.utils.get(member.guild.channels, name="Join to Create")
    channel_id = channel.id
    #print(channel_id)
    #print(member,before,after)
    if after.channel and after.channel.id == channel_id: #2
        category_channel = discord.utils.get(guild.categories, name="Voice Channels")
        channel = await guild.create_voice_channel(member.name + "" + "'s Channel", overwrites=None, category=category_channel, reason=None)
        voice_channel = client.get_channel(channel.id)    
        await member.move_to(voice_channel)
        return
        
    else:
        return



@client.command()
async def lock(ctx):
    channel = client.get_channel(ctx.author.voice.channel)
    #print(ctx.author.voice.channel)
    #print(channel)
    await ctx.author.voice.channel.set_permissions(ctx.guild.default_role,connect=False)
    await ctx.send("Locked")
    return


@client.command()
async def unlock(ctx):
    channel = client.get_channel(ctx.author.voice.channel)
    #print(channel)
    await ctx.author.voice.channel.set_permissions(ctx.guild.default_role,connect=True)

    await ctx.send("Unlocked")
    return



@client.command()
async def setup(ctx):   
    global cat
    guild = ctx.message.guild
    print(guild)
    Voicey = "Voice Channels"
    await ctx.send("Starting Setup...")
    global cat
    channel = await guild.create_category(Voicey, overwrites=None, reason=None, position=None)
    cat = client.get_channel(channel.id)
    await guild.create_voice_channel("Join to Create", overwrites=None, category=cat, reason=None)



    await ctx.send("Finished setup")
    return






client.run('ODI2MDAyNzY0OTk1MTAwNzMy.YGGJBQ.DrTZuA9nSbskRgL2rAwQWlBkKfU')