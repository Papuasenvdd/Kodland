
import discord 

from discord.ext import commands

import os, random

import aiohttp

import json

import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

    
@client.command()
async def meme(ctx):
     embed = discord.Embed(title = '', description = '')

     async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
               res = await r.json()

               embed.set_image(url = res['data']['children'][random.randint(0, 25)]['data']['url']) 
               await ctx.reply(embed=embed)



@client.command()
async def cat(ctx):
     async with aiohttp.ClientSession() as ses:
          async with ses.get('http://some-random-api.ml/animal/cat') as r:
               if r.status in range(200, 299):
                    data = await r.json()
                    image = data["image"]
                    await ctx.reply(image)
                    ses.close
#client.run('MTEwOTQ5MDAxODUxMjI3NzYzNQ.GbewUY.F0KUbigEVd_SMsBtpmgNF7-c1yrHUfuxifafTg')



