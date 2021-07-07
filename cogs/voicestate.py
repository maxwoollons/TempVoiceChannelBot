from discord
from discord.ext import commands


#new channel on join
@client.event
async def on_voice_state_update(member, before, after):
    print("aaa")
    guild = client.get_guild(803394988187582464)
    print(member,before,after)
    if after.channel and after.channel.id == 862285957699993600: #2
        category_channel = guild.get_channel(819838582767484998)
        channel = await guild.create_voice_channel(member.name + "" + "'s Channel", overwrites=None, category=category_channel, reason=None)
        voice_channel = client.get_channel(channel.id)    
        await member.move_to(voice_channel)
        return
        
    else:
        return


#delete on 0 users
@client.event
async def on_voice_state_update(member, before, after): #delete channel if it is empty
    if before.channel == None:
        print("none")
        return

    else:
        #print("a")
        channel = client.get_channel(before.channel)
        bmember_count = len(before.channel.voice_states)
        #print(before.channel.voice_states)
        #print(bmember_count)#before
        if bmember_count == 0 and before.channel.id != 862285957699993600:#1
            print("Delete")
            await before.channel.delete()
            return

        else:
            print("not empty yet")
            return