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
@client.command()
async def stfu(ctx, *, msg):
    embed=discord.Embed(title=":octagonal_sign: **Shut the fuck up** :octagonal_sign:", description="", color=0x3D85C6)
    embed.set_author(name="Aperture+", url="https://sites.google.com/view/aperturedsicordb", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Aperture_Science.svg/1200px-Aperture_Science.svg.png")
    embed.add_field(name="Shut The Fuck Up", value=msg, inline=False)
    embed.set_footer(text="Aperture+ • Since: 2020 • By: Tato1234#7211")
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def invite(ctx):
    embed=discord.Embed(title="Click Here To Add!", url="https://discord.com/oauth2/authorize?client_id=741379497181315224&permissions=8&scope=bot", color=0x3d85c6)
    embed.set_author(name="Aperture+", url="https://sites.google.com/view/aperturedsicordb", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Aperture_Science.svg/1200px-Aperture_Science.svg.png")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Aperture_Science.svg/1200px-Aperture_Science.svg.png")
    embed.add_field(name="Aperture+ Discord Bot", value="We aren't responsible for how you use our Discord bot.", inline=False)
    embed.set_footer(text="Aperture+ • Since: 2020 • By: Tato1234#7211")
    
    await ctx.send(embed=embed)
@client.command()
async def aperture(ctx):
    embed=discord.Embed(title="Aperture Button", url="https://sites.google.com/view/aperturedsicordb", color=0x3d85c6)
    embed.set_author(name="Aperture+", url="https://sites.google.com/view/aperturedsicordb",     icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Aperture_Science.svg/1200px-Aperture_Science.svg.png")
    embed.set_footer(text="Aperture+ • Since: 2020 • By: Tato1234#7211")
    
    await ctx.send(embed=embed)


client.run('TOKEN')
