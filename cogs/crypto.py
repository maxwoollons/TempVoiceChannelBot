import discord
from discord.client import Client
from discord.ext import commands
import requests



#https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=AUD




client = commands.Bot(command_prefix = "=")

class crypto(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
        


    @commands.command()
    async def crypto(self, ctx):
        response = requests.get("https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=AUD")
        #joke = response.json()['setup'] + " " + response.json()['punchline']
        #print(joke)
        #await ctx.send(response.json()['coins'][0]['id'])
        n1 = response.json()['coins'][0]['id']
        n2 = response.json()['coins'][1]['id']
        n3 = response.json()['coins'][2]['id']
        n4 = response.json()['coins'][3]['id']
        n5 = response.json()['coins'][4]['id']
        n1p = "$" + str(round(response.json()['coins'][0]['price'],5)) + "\n  Daily Change: " + str(response.json()['coins'][0]['priceChange1d']) + "%"
        n2p = "$" + str(round(response.json()['coins'][1]['price'],5)) + "\n  Daily Change: " + str(response.json()['coins'][1]['priceChange1d']) + "%"
        n3p = "$" + str(round(response.json()['coins'][2]['price'],5)) + "\n  Daily Change: " + str(response.json()['coins'][2]['priceChange1d']) + "%"
        n4p = "$" + str(round(response.json()['coins'][3]['price'],5)) + "\n  Daily Change: " + str(response.json()['coins'][3]['priceChange1d']) + "%"
        n5p = "$" + str(round(response.json()['coins'][4]['price'],5)) + "\n Daily Change: " + str(response.json()['coins'][4]['priceChange1d']) + "%"
        
        #embed
        em = discord.Embed(title = "Crypto Prices (AUD)", description = "Live crypto price update of the top 5 coins.", color=0xe3cc35)
        em.set_thumbnail(url="https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5ea6d49e165a170006a5d625%2F960x0.jpg%3Ffit%3Dscale")
        em.add_field(name=n1,value=n1p)
        em.add_field(name=n2,value=n2p)
        em.add_field(name=n3,value=n3p)
        em.add_field(name=n4,value=n4p)
        em.add_field(name=n5,value=n5p)
        await ctx.send(embed=em)
        return     



def setup(client):
    client.add_cog(crypto(client))

