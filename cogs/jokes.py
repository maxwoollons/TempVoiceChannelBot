import discord
from discord.client import Client
from discord.ext import commands
import requests



#https://official-joke-api.appspot.com/random_joke




client = commands.Bot(command_prefix = "=")

class jokes(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
        


    @commands.command()
    async def joke(self, ctx):
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        #joke = response.json()['setup'] + " " + response.json()['punchline']
        #print(joke)
        await ctx.send(response.json()['setup'])
        await ctx.send(response.json()['punchline'])
        return




def setup(client):
    client.add_cog(jokes(client))

