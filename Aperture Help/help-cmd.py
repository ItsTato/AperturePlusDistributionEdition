import discord, random
from discord.ext import commands
import json
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
async def help(ctx):
    embed=discord.Embed(title=":information_source: **Help** :information_source:", description="", color=0x3D85C6)
    embed.set_author(name="Aperture+", url="https://sites.google.com/view/aperturedsicordb",     icon_url="https://i.imgur.com/lvUmFyr.png")
    embed.set_thumbnail(url="https://i.imgur.com/lvUmFyr.png")
    embed.set_footer(text='Aperture+ • Since: 2020 • By: Tato1234#7211')
    embed.add_field(name='volume', value="Sets the volume of the player.", inline=False)
    embed.add_field(name='leave', value="Clears the queue and leaves the voice channel.", inline=False)
    embed.add_field(name='now', value="Displays the currently playing song.", inline=False)
    embed.add_field(name='p or play', value="Plays a song.", inline=False)
    embed.add_field(name='join', value="Joins a voice channel.", inline=False)
    embed.add_field(name='queue', value="hows the player's queue.", inline=False)
    embed.add_field(name='shuffle', value="Shuffles the queue.", inline=False)
    embed.add_field(name='skip', value="Vote to skip a song. The requester can automatically skip.", inline=False)
    embed.add_field(name='stop', value="Stops playing song and clears the queue.", inline=False)
    embed.add_field(name='summon', value="Summons the bot to a voice channel.", inline=False)
    embed.add_field(name='warn', value='warn [@user] [reasson]', inline=False)
    embed.add_field(name='kick', value='kick [@user]', inline=False)
    embed.add_field(name='ban', value='ban [@user]', inline=False)
    embed.add_field(name='prefix', value='prefix [prefix]', inline=False)
    embed.add_field(name='say', value='say [message]', inline=False)
    embed.add_field(name='meme', value="Sends a meme!", inline=False)
    await ctx.send(embed=embed)

client.run('TOKEN')
