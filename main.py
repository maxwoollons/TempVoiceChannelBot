from inspect import EndOfBlock
import discord
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands
from discord.ext.commands.core import command
import datetime #need to install this on the live server
import json






client = commands.Bot(command_prefix = "=",description='I am a VoiceChannel Bot, DM Sand#4193 for assistance')



#cogs
cogs = ['cogs.voicestate','cogs.jokes','cogs.cats','cogs.crypto']

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'could not load cog {cog}: {str(e)}')


#-----------------------------------------------


client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    server_amt = len(client.guilds)
    listning = "for =help | " + str(server_amt) + " servers"
    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listning))
    return



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
    if ctx.message.author.guild_permissions.administrator:
        global cat
        guild = ctx.message.guild
        
        print(guild)
        Voicey = "Voice Channels"
        await ctx.send("Starting Setup...")
        global cat
        channel = await guild.create_category(Voicey, overwrites=None, reason=None, position=None)
        cat = client.get_channel(channel.id)
        await guild.create_voice_channel("Join to Create", overwrites=None, category=cat, reason=None)
    else:
        return



    await ctx.send("Finished setup")
    return



@client.command()
async def help(ctx):
    em = discord.Embed(title = "Help", description = "This is the help menu. DM Sand#4193 for assistance or feedback.")
    em.add_field(name="Setup",value="=setup, =invite")
    em.add_field(name="Voice Channels",value="=lock, =unlock")
    em.add_field(name="Other",value="=servers, =created, =version, =joke, =cat, =crypto")
    await ctx.send(embed=em)
    return


@client.command()
async def invite(ctx):
    channel = await ctx.author.create_dm()
    await channel.send("Here is my invite link:")
    await channel.send("https://bit.ly/3huSe00")
    return



@client.command()
async def servers(ctx):
    servers = len(client.guilds)
    if servers <= 1:
        print("I am in "+ str(servers) + " server.")
        await ctx.send("I am in "+ str(servers) + " server.")
        return

    else:
        
        print("I am in "+ str(servers) + " servers.")
        await ctx.send("I am in "+ str(servers) + " servers.")
        return
    
    
    
@client.command()   #created
async def created(ctx):
    date = ctx.author.created_at
    format_date = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + "  DD/MM/YYYY"
    await ctx.send("Your account was created on " + format_date)
    return
    

@client.command()
async def version(ctx):
    await ctx.send("Bots current version is on v0.7")#change every update
    return
    





client.run('ODI2MDAyNzY0OTk1MTAwNzMy.YGGJBQ.DrTZuA9nSbskRgL2rAwQWlBkKfU')





#dev = ODYzMDExOTkxMTAyOTQ3MzI4.YOgsjA.VTg4NdfSTg_ivGxhqUUCHyzFD24
#live = ODI2MDAyNzY0OTk1MTAwNzMy.YGGJBQ.DrTZuA9nSbskRgL2rAwQWlBkKfU