# Tutbot by Da532 edited into Zardashtand bot by Zardasht HQ on YouTube

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

token='(NDY0ODI2NzM3MTg5MDYwNjA4.Dn_zfQ.6HAY-8wIgDNI4xIL1J0oki4nr2M)'

bot = commands.Bot(command_prefix='z!')

@bot.event
async def on_ready():
    print ("Ready when you are XD")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":mans_shoe: Cya, {}.If this User is a mod/staff they wouldn't have been banned but if they aren't The User Was Succesfully kicked!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say(":mans_shoe: Cya, {}. If this User is a mod/staff they wouldn't have been banned but if they aren't The User Was Succesfully banned!".format(user.name))
    await bot.ban(user)
    
@bot.command(pass_context=True)
async def cookie(ctx):
    await bot.say(":cookie: Here free cookie")
   
@bot.command(pass_context=True)
async def latest_updates(ctx):
    await bot.say(":robot: New Update includes New Command ('z!latest_updates') and the bot is now a 24/7 bot yay!! to support the creator subscribe to Zardasht HQ")
    print ("looked at updates")

#if that dosn't work replace it with your actuall token instead of leving it in as token'

bot.run("NDY0ODI2NzM3MTg5MDYwNjA4.Dn_zfQ.6HAY-8wIgDNI4xIL1J0oki4nr2M'")
