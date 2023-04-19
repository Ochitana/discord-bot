from discord.ext import commands
import json
import random

class coin_flip(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('coin_flip has loaded')

	@commands.command()
	async def flip(self, ctx, *args):
		result = random.choice(['heads','tails'])
		await ctx.send(f'{result}')

#TODO make it interact with data.json to be able to make bets

	# @commands.command()
	# async def coinflip(self, ctx, *args):
	# 	with open('game-state.json', 'r') as openfile:
	# 		gameStateDict = json.load(openfile)


async def setup(bot):
	await bot.add_cog(coin_flip(bot))
		