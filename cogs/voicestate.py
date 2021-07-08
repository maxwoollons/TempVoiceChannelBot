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
            print("none")
            return

        else:
            print("a")
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


    @commands.Cog.listener()
    async def on_ready(self):
        print("cog working")



    #@commands.command()
    #async def a(self,ctx):
        #await ctx.send("a")





def setup(client):
    client.add_cog(voicestate(client))

