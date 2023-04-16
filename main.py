import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# TODO: Make an allowlist
async def load():
	count = 0
	for f in os.listdir("./cogs"):
		if f.endswith(".py"):
			await bot.load_extension("cogs." + f[:-3])
			count += 1
	print(f'Loaded: {count} Cogs')


@bot.event
async def on_command_error(ctx, error):
	await ctx.send('tf?')
	print(error)
		  
@bot.command()
async def refresh(ctx):
	count = 0
	for f in os.listdir("./cogs"):
		if f.endswith(".py"):
			await bot.unload_extension("cogs." + f[:-3])
			await bot.load_extension("cogs." + f[:-3])
			count += 1
	print(f'Refreshed: {count} Cogs')


asyncio.run(load())
bot.run(os.environ['TOKEN'])
