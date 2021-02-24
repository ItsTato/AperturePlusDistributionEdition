import discord, random
import aiohttp
import json
from discord.ext import commands
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

client.remove_command("help")

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = '+'

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes.pop(str(guild.id))
        

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def prefix(ctx, prefix):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        

    prefixes[str(ctx.guild.id)] = prefix
        

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
@client.command(pass_context=False)
async def meme(ctx):
    embed=discord.Embed(title="Meme", description='Aperture Memes', color=0x3D85C6)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

client.run('TOKEN')
