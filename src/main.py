import os
from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

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

"""
@bot.command()
async def count(ctx):
    #await discord.Client.get_all_members()
    #await ctx.send(ctx.bot.get_all_members())
    '''for member in ctx.bot.get_all_members():
        await ctx.send(member)'''
    '''guild = ctx.bot.fetch_guilds()
    for e in guild:
        print(e)
        await ctx.send(e)'''
    
    for e in bot.guilds:
        print(e.members)
        await ctx.send(e.members)
    print(bot.guilds)
    print(bot.get_all_members())
    print(bot.users)
    """

@bot.command()
async def ban(ctx, user: discord.User):
    await user.ban()

@bot.command()
async def unban(ctx, user: discord.User):
    await user.unban()


token = os.environ["DISCORD_TOKEN"]
bot.run(token)  # Starts the bot