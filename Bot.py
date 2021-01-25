import discord
from discord.ext import commands
import json
import os
from subprocess import call

bot = commands.Bot(command_prefix = '$') # user need to put a '$' before writing a command

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('With our work'))
    print("Bot Loading")

# Clearing 10 chats
@bot.command()
@commands.has_permissions(manage_messages = True)

async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'Deleted 10 messages, Channel looking clean.')

# For kicking/ban someone out of server
@bot.command
async def kick(ctx, member : discord.Member,*,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'A {member.mention} has been kicked')
    
@bot.command
async def ban(ctx, member : discord.Member,*,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'A {member.mention} has been banned')

# Unban the member
async def unban(ctx, *, member): 
    banned = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for b_entry in banned:
        user = b_entry.user
        
        # Creating a Tuple 
        if(user.discriminator, user.name) == (member_discriminator, member_name):
            await ctx.guild.unban(user)
            await ctx.send(f'A user {user.name} has been unbanned now!')
            await ctx.send(f'A lesson well learnt.')
            return

@bot.command()
async def ping(ctx):
    await ctx.send(f'Umm! {round(bot.latency * 1000)}ms')

# for the bot to join and leave the voice channel in which user is present!!
@bot.command(pass_context = True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

@bot.command(pass_context = True)
async def leave(ctx):
    if ctx.message.author.voice:
        client = ctx.message.guild.voice_client
        await client.disconnect()

bot.run('write your token ID here from bot settings in discord')

