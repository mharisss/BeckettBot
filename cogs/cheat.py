import discord
from discord.ext import commands


class cheatsheet(commands.Cog):
    def init(self, client):
        self.client = client
##SQL I cheat sheet download
    @commands.command()
    async def sql(self,ctx):
      await ctx.author.send(file=discord.File('/home/runner/BeckettBot/cheat_sheets/SQLI_login_cheatsheet.txt'))
#XSS cheat sheet download
    @commands.command()#persistent scripts
    async def xsr(self,ctx):
      await ctx.author.send(file=discord.File('/home/runner/BeckettBot/cheat_sheets/XSSR_cheatsheet.txt'))
    
    @commands.command()#reflective scripts
    async def xsss(self,ctx):
      await ctx.author.send(file=discord.File('/home/runner/BeckettBot/cheat_sheets/XSSS_cheatsheet.txt'))
##list of common ports
    @commands.command()
    async def ports(self,ctx):
      await ctx.author.send(file=discord.File('/home/runner/BeckettBot/cheat_sheets/ports.txt'))
def setup(client):
    client.add_cog(cheatsheet(client))