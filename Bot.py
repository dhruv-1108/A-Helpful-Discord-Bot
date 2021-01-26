import discord
from discord.ext import commands
import random
from discord.ext.commands import Bot
from discord import Game

bot = commands.Bot(command_prefix = '$') # user need to put a '$' before writing a command   

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('With our work'))
    print("Bot Loading")

# Command for random coin flip game
@bot.command(aliases = ['flip','test'])
async def _flip(ctx):
    outcome = ['Heads',
                'Tails',
                'Oops! Coin is lost!']
    await ctx.send(f'Here you go: {random.choice(outcome)}')

# Clearing 10 chats
@bot.command()
@commands.has_permissions(manage_messages = True)

async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'Deleted 10 messages, Channel looking clean.')

# For kicking/ban someone out of server
@bot.command()
async def kick(ctx, member : discord.Member,*,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'A {member.mention} has been kicked')
    
@bot.command()
async def ban(ctx, member : discord.Member, *,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'A {member.mention} has been banned')

# Unban the member
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
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


bot.run('Write your token here from developer options!')
