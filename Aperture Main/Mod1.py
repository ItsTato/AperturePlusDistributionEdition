import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
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
    await ctx.send(f'Aperture Prefix was changed to `{prefix}` on all modules')

@client.command(aliases=['rbc'])
async def bc(ctx, *, msg):
    embed=discord.Embed()
    embed.title=':mega: Broadcast'
    embed.description=msg
    await ctx.send(embed=embed)
    await ctx.message.delete()

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@client.command(pass_context = True                    )
@has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await ctx.send(":x: Please provide a reason!")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@client.command()
async def say(ctx, msg):
    await ctx.send(msg)
    await ctx.message.delete()
@client.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {', '.join(current_user['reasons'])}")
      break
  else:
    await ctx.send(f"{user.name} has never been reported")  

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await client.send_message(ctx.message.channel, text)   

client.run("TOKEN")
