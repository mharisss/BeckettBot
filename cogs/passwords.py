import discord
import os
import string
from random import *
import random
from discord.ext import commands


class passwords(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command()
    async def passlist(self,ctx):
     await ctx.author.send('https://thehacktoday.com/password-cracking-dictionarys-download-for-free/')


    @commands.command()
    async def passgen(self,ctx):
      chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789_-][}{;:/|+=`¬'
      password ="".join(choice(chars)for c in range(70))
      await ctx.author.send(password)



def setup(client):
    client.add_cog(passwords(client))