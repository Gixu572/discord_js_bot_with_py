from unicodedata import category
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='');

@bot.event
async def on_ready():
    print("Ready!!")

@bot.command()
async def meow(ctx):
    await ctx.send('Hi')

@bot.command()
async def Hi(ctx):
    await ctx.send("How Can I help");
    await ctx.send("Type: help (case sensitive) for more help")

async def help(ctx):
    category = "Help"
    await ctx.send("Type Hi for a reply");
    await ctx.send("Type meow for Hi xD");
bot.run('OTU2NTMyMzAyOTY2NTc1MTI0.YjxmIA.9kR5De1MTI2XILw5f_qCKKOW1tI')
