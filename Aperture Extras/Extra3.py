import discord, random
from discord.ext import commands
import aiohttp

client=commands.Bot(command_prefix='+')

@client.command(pass_context=False)
async def status(ctx):
    embed=discord.Embed(title="**Status**", description="", color=0x3D85C6)
    embed.set_author(name="Aperture+", url="https://sites.google.com/view/aperturedsicordb", icon_url="https://i.imgur.com/lvUmFyr.png")
    embed.add_field(name="Server1", value=":green_square: Online", inline=False)
    embed.add_field(name="Server2", value=":globe_with_meridians: None", inline=False)
    embed.add_field(name="Server3", value=":globe_with_meridians: None", inline=False)
    embed.set_footer(text="Aperture+ • Since: 2020 • By: Tato1234#7211")
    await ctx.send(embed=embed)

client.run('TOKEN')
