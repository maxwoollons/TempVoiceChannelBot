import discord
from discord.client import Client
from discord.ext import commands
import requests



#https://official-joke-api.appspot.com/random_joke




client = commands.Bot(command_prefix = "=")

class cats(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
        


    @commands.command()
    async def cat(self, ctx):
        response = requests.get("https://thatcopy.pw/catapi/rest/")
        #joke = response.json()['setup'] + " " + response.json()['punchline']
        #print(joke)
        await ctx.send(response.json()['webpurl'])
        return




def setup(client):
    client.add_cog(cats(client))

