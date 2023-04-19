import asyncio
import discord
from discord.ext import commands
import os
import time
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
app = Flask('')
allowlist = ['Ochitana', 'Eoj']


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
	if ctx.author.name in allowlist:
		count = 0
		for f in os.listdir("./cogs"):
			if f.endswith(".py"):
				await bot.unload_extension("cogs." + f[:-3])
				await bot.load_extension("cogs." + f[:-3])
				count += 1
		await ctx.send(f'Weak. Only {count} cogs?')
	else:
		await ctx.send('no')


@bot.event
async def on_ready():
	global start_time
	start_time = time.time()


@bot.command()
async def uptime(ctx):

	elapsed_time = time.time() - start_time
	hours = int(elapsed_time // 3600)
	minutes = int((elapsed_time % 3600) // 60)
	seconds = int(elapsed_time % 60)

	if ctx.author.name in allowlist:
		await ctx.send(
		 f'Been out of prison for {hours} hours, {minutes} minutes, and {seconds} seconds.'
		)
	else:
		await ctx.send(
		 'Time is the the enemy of the rich man. And you, are not a rich man.')


#TODO: Figure out how to keep bot alive without paying money
#upTimeRobot

asyncio.run(load())
bot.run(os.environ['TOKEN'])
