import discord
import datetime
from discord.ext import commands
import codecs
import hashlib
import base64

class cryptography(commands.Cog):
    def init(self, client):
        self.client = client

    
    @commands.command() ##rot13 encryption/decryption
    async def rot13(self,ctx,*,arg): 
      embedrot13=discord.Embed(title="Rot13 encryption/decryption", color=0xff0505)
      embedrot13.add_field(name="Your original text:", value=arg, inline=False)
      embedrot13.add_field(name="Your encrypted/decrypted text:", value=((codecs.encode(arg, "rot_13"))), inline=False)
      embedrot13.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embedrot13)

#reformat below to above 
    @commands.command()
    async def md5(self,ctx,*,arg):
      result=hashlib.md5(arg.encode())
      embed=discord.Embed(title="MD5 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your MD5 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.send('Your md5 encryption:')
      await ctx.author.send(embed=embed)
    
    @commands.command()
    async def sha1(self,ctx,*,arg):
      result=hashlib.sha1(arg.encode())
      embed=discord.Embed(title="Sha1 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your Sha1 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed)  
    
    @commands.command()
    async def sha224(self,ctx,*,arg):
      result=hashlib.sha224(arg.encode())
      embed=discord.Embed(title="Sha224 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your Sha224 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 

    @commands.command()
    async def sha256(self,ctx,*,arg):
      result=hashlib.sha256(arg.encode())
      embed=discord.Embed(title="Sha256 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your sha256 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 

    @commands.command()
    async def sha384(self,ctx,*,arg):
      result=hashlib.sha384(arg.encode())
      embed=discord.Embed(title="Sha384 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your Sha384 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 

    @commands.command()
    async def sha512(self,ctx,*,arg):
      result=hashlib.sha512(arg.encode())
      embed=discord.Embed(title="Sha512 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your Sha512 value:", value=result.hexdigest(), inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 
    
#epoch unix time stamp converter  FIX THIS!
    @commands.command()
    async def epoch(self,ctx,*,arg):
      result = datetime.datetime.fromtimestamp(int(arg))
      embed=discord.Embed(title="Unix Epoch decryption", color=0xff0505)
      embed.add_field(name="Your Epoch value:", value=arg, inline=False)
      embed.add_field(name="Your real-time value:", value=result, inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 
      
      
#base 64
    @commands.command()
    async def base64(self,ctx,*,arg):
      mes = arg
      mb = mes.encode('ascii')
      result = base64.b64encode(mb)
      embed=discord.Embed(title="Base64 encryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your Base64 value:", value=result, inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed) 


    @commands.command()
    async def base64d(self,ctx,*,arg):
      mes = arg
      b64b = mes.encode('ascii')
      message_bytes = base64.b64decode(b64b)
      message = message_bytes.decode('ascii')
      embed=discord.Embed(title="Base64 decryption", color=0xff0505)
      embed.add_field(name="Your original text:", value=arg, inline=False)
      embed.add_field(name="Your decrypted value:", value=message, inline=False)
      embed.set_footer(text="Hope this achives your goals")
      await ctx.author.send(embed=embed)
       
def setup(client):
    client.add_cog(cryptography(client))