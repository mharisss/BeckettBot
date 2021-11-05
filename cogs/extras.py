import discord
from discord.ext import commands
from mac_vendor_lookup import AsyncMacLookup
import pyshorteners
from requests import get



class extras(commands.Cog):
    def init(self, client):
        self.client = client
    
    
#url shortner
    @commands.command()
    async def urls(self,ctx,arg):
      s = pyshorteners.Shortener()
      embed=discord.Embed(title="URL Shortener", color=0xff0505)
      embed.add_field(name="Your original URL:", value=arg, inline=False)
      embed.add_field(name="Your shortened value:", value=s.tinyurl.short(arg), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed)

    #mac address lookup
    @commands.command()
    async def mac(self,ctx,arg):
      mac = AsyncMacLookup()
      embed=discord.Embed(title="MAC address Lookup", color=0xff0505)
      embed.add_field(name="Your MAC address:", value=arg, inline=False)
      embed.add_field(name="Your identifd manufacturer:", value=await mac.lookup(arg), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed)
    
    @commands.command() #has a small limit-future api key invest?
    async def geo(self,ctx, arg): 
     loc = get('https://ipapi.co/' + arg +'/json')
     await ctx.author.send(loc.json())
    

 

def setup(client):
    client.add_cog(extras(client))