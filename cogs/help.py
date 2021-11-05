import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure



class help(commands.Cog):
    def init(self, client):
        self.client = client
      
    

    if has_permissions(administrator=True): # allows admins to view thier verison of the command list via direct message REQUIRES FURTHER TESTING

      @commands.group(invoke_without_command=True)
      async def help(self,ctx):
       admin=  ('1. attend\n' )
       crypt= ('1. rot13\n 2. md5\n 3. sha1\n 4. sha224\n 5. sha256\n 6. sha384\n 7. sha512\n 8. epoch\n 9. base64\n 10. base64d')
       password= ('1. passlist\n 2. passgen')
       cheat= ('1. sql\n 2. xsr\n 3. xsss\n 4. ports\n')
       extras= ('1. mac\n 2. urls\n 3. geo')
       stats=  ('1. stats\n')
       embed=discord.Embed(title='Help', description='Use !help <command> for extended command fucntion', color=ctx.author.color)
       embed.add_field(name = 'Admin Tools', value= admin, inline = True)
       embed.add_field(name = 'Cryptography', value = crypt, inline = True)
       embed.add_field(name = 'Passwords', value = password, inline = True)
       embed.add_field(name = 'Cheat sheets', value = cheat, inline = True)
       embed.add_field(name = 'Bot Stats', value = stats, inline = True)
       embed.add_field(name = 'Extras', value = extras, inline = True)
       embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
       await ctx.author.send(embed=embed)

    else:
      
      @commands.group(invoke_without_command=True)
      async def help(self,ctx):
       crypt= ('1. rot13\n 2. md5\n 3. sha1\n 4. sha224\n 5. sha256\n 6. sha384\n 7. sha512\n 8. epoch\n 9.base64\n 10. base64d')
       password= ('1. passlist\n 2. passgen')
       cheat= ('1. sql\n 2. xsr\n 3. xsss\n 4. ports\n')
       stats= ('1. mac\n 2. urls')  
       stats=  ('1. stats\n')
       embed=discord.Embed(title='Help', description='Use !help <command> for extended command fucntion',color=ctx.author.color)
       embed.add_field(name = 'Cryptography', value = crypt, inline = True)
       embed.add_field(name = 'Passwords', value = password, inline = True)
       embed.add_field(name = 'Cheat sheets', value = cheat, inline = True)
       embed.add_field(name = 'Bot Stats', value = stats, inline = True)
       embed.add_field(name = 'Extras', value = stats, inline = True)
       embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
       await ctx.author.send(embed=embed)

    
    @help.command()
    async def rot13(self,ctx):
      em = discord.Embed(title="!rot13",description="returns rot13 value of string or vice versa",color=ctx.author.color)
      em.add_field(name ="!rot13", value= "!rot13 [arg]")
      await ctx.send(embed=em)

   
    @help.command()
    async def md5(self,ctx):
      em = discord.Embed(title="!md5",description="returns md5 value of string",color=ctx.author.color)
      em.add_field(name ="!md5", value= "!md5 [arg]")
      await ctx.send(embed=em)
    
    @help.command()
    async def sha1(self,ctx):
      em = discord.Embed(title="!sha1",description="returns sha1 value of string",color=ctx.author.color)
      em.add_field(name ="!sha1", value= "!sha1 [arg]")
      await ctx.send(embed=em)

    
    @help.command()
    async def sha224(self,ctx):
      em = discord.Embed(title="!sha224",description="returns sha224 value of string",color=ctx.author.color)
      em.add_field(name ="!sha224", value= "!sha224 [arg]")
      await ctx.send(embed=em)


    @help.command()
    async def sha256(self,ctx):
      em = discord.Embed(title="!sha1",description="returns sha256 value of string",color=ctx.author.color)
      em.add_field(name ="!sha256", value= "!sha256 [arg]")
      await ctx.send(embed=em)


    @help.command()
    async def sha384(self,ctx):
      em = discord.Embed(title="!sha384",description="returns sha384 value of string",color=ctx.author.color)
      em.add_field(name ="!sha384", value= "!sha384 [arg]")
      await ctx.send(embed=em)


    @help.command()
    async def sha512(self,ctx):
      em = discord.Embed(title="!sha512",description="returns sha512 value of string",color=ctx.author.color)
      em.add_field(name ="!sha512", value= "!sha512 [arg]")
      await ctx.send(embed=em)
    

    @help.command()
    async def epoch(self,ctx):
      em = discord.Embed(title="!epoch",description="returns epoch value in human format",color=ctx.author.color)
      em.add_field(name ="!epoch", value= "!epoch [epoch time stamp]")
      await ctx.send(embed=em)

    @help.command()
    async def base64(self,ctx):
      em = discord.Embed(title="!base64",description="encodes argument to base64",color=ctx.author.color)
      em.add_field(name ="!base64", value= "!base64 [arg]")
      await ctx.send(embed=em)

    @help.command()
    async def base64d(self,ctx):
      em = discord.Embed(title="!base64d",description="decodes base64 string to ascii",color=ctx.author.color)
      em.add_field(name ="!base64d", value= "!base64d [arg]")
      await ctx.send(embed=em)
    
    
    @help.command()
    async def attend(self,ctx):
      em = discord.Embed(title="!attend [arg]",description="Only admins can use this! Returns all active members in general voice channel",color=ctx.author.color)
      em.add_field(name ="!attend [channel_id] eg: !attend 1234", value= "!attend")
      await ctx.send(embed=em)
    

    @help.command()
    async def geo(self,ctx):
      em = discord.Embed(title="!geo",description="Geo locates given ip address",color=ctx.author.color)
      em.add_field(name ="!geo", value= "!geo [ip-address]")
      await ctx.send(embed=em)

    #passwords

    @help.command()
    async def passgen(self,ctx):
      em = discord.Embed(title="!passgen",description="Generates a strong password for you",color=ctx.author.color)
      em.add_field(name ="!Passgen", value= "!passgen")
      await ctx.send(embed=em)
    
    @help.command()
    async def passlist(self,ctx):
      em = discord.Embed(title="!passlist",description="Give a link for password lists",color=ctx.author.color)
      em.add_field(name ="!passlist", value= "!passlist")
      await ctx.send(embed=em)

    #cheat sheets
    @help.command()
    async def sql(self,ctx):
      em = discord.Embed(title="!sql",description="Returns a sql injection cheat sheet",color=ctx.author.color)
      em.add_field(name ="!sql", value= "!sql")
      await ctx.send(embed=em)

    @help.command()
    async def xsr(self,ctx):
      em = discord.Embed(title="!xsr",description="Returns reflective xss scripts",color=ctx.author.color)
      em.add_field(name ="!xsr", value= "!xsr")
      await ctx.send(embed=em)

    @help.command()
    async def xsss(self,ctx):
      em = discord.Embed(title="!xsss",description="Returns stored xsss scripts",color=ctx.author.color)
      em.add_field(name ="!xsss", value= "!xsss")
      await ctx.send(embed=em)
    
    @help.command()
    async def ports(self,ctx):
      em = discord.Embed(title="!ports",description="Returns common ports list",color=ctx.author.color)
      em.add_field(name ="!ports", value= "!ports")
      await ctx.send(embed=em)


    #extras
    @help.command()
    async def mac(self,ctx):
      em = discord.Embed(title="!mac",description="Returns Mac address manufacturer",color=ctx.author.color)
      em.add_field(name ="!Mac", value= "!mac [Mac-address]")
      await ctx.send(embed=em)

    @help.command()
    async def urls(self,ctx):
      em = discord.Embed(title="!urls",description="Shortens given url",color=ctx.author.color)
      em.add_field(name ="!urls", value= "!urls [your url here]")
      await ctx.send(embed=em)

    #stats
    @help.command()
    async def stats(self,ctx):
      em = discord.Embed(title="!stats",description="Gives the stats of BeckettBot",color=ctx.author.color)
      await ctx.send(embed=em)

def setup(client):
    client.add_cog(help(client))



    