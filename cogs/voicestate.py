import discord
from discord.client import Client
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

class voicestate(commands.Cog):
    def __init__(self, client):
    
        self.client = client

    print("This is in the cog")



    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after): #delete channel if it is empty
        if before.channel == None:
            #print("none")
            return

        else:
            #print("a")
            channel = client.get_channel(before.channel)
            bmember_count = len(before.channel.voice_states)
            #print(before.channel.voice_states)
            #print(bmember_count)#before
            channell = discord.utils.get(member.guild.channels, name="Join to Create")
            channel_id = channell.id
            guild = member.guild
            category_channel = discord.utils.get(guild.categories, name="Voice Channels") #category of setup
            #print(category_channel)
            if bmember_count == 0 and before.channel.id != channel_id and category_channel == before.channel.category:#1
                #print("Delete")
                await before.channel.delete()
                return

            else:
                print("not empty yet or is not supposed to be deleted")
                return




    #@commands.command()
    #async def a(self,ctx):
        #await ctx.send("a")





def setup(client):
    client.add_cog(voicestate(client))

