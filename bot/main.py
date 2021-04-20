import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='!support | By TheYoBots'))
    print(f"Logged in as {client.user.name}")
    print(f"Bot ID: {client.user.id}")
    
@client.command()
async def support(ctx):
    await ctx.send("List of commands: `!test`, `!source`")
    
@client.command()
async def source(ctx):
    await ctx.send("This Bot is made by TheYoBots. Checkout the source code here: https://github.com/TheYoBots/discord-bot")
    
@client.command()
async def test(ctx):
    await ctx.send("Tested! It works!")

if __name__ == "__main__":
    client.run(TOKEN)
