from discord.ext import commands
import json
import random


class Quotes(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Quotes has loaded')

	@commands.command()
	async def quotes(self, ctx, *args):
		with open('tate_quotes.json', 'r') as openfile:
			tateDict = json.load(openfile)
		tateList = tateDict['tate_quote']
		# print(len(tateList))
		await ctx.send(f'"{tateList[random.randint(0,103)]}"')


async def setup(bot):
	await bot.add_cog(Quotes(bot))
