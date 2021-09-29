import os
from discord.ext import commands
import discord

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 238201344643563520  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(str(ctx.author)[:-5])

token = "ODkyODI0MDc1MTA4NTExNzg0.YVShNw.SyWGFzoIYqlq9C17jWKKXqZhWl0"
bot.run(token)  # Starts the bot