from discord.ext import commands
import json
import random


class Roulette(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Roulette has loaded')

	@commands.command()
	async def roulette(self, ctx, *args):
		with open('game-state.json', 'r') as openfile:
			gameStateDict = json.load(openfile)
		print(gameStateDict)
		# !roulette list
		if args[0] == 'list':
			await ctx.send(gameStateDict['roulette'])


async def setup(bot):
	await bot.add_cog(Roulette(bot))
