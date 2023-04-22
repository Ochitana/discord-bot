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
		result = random.choice(['heads', 'tails'])
		await self.betExecute(result, ctx)

	@commands.command()
	async def bet(self, ctx, *args):
		await self.addBet(ctx, args)

#TODO make it interact with data.json to be able to make bets

	async def addBet(self, ctx, args):
		with open('game_state.json', 'r') as openfile:
			gameStateDict = json.load(openfile)
		with open('data.json', 'r') as openfile:
			bankBalanceDict = json.load(openfile)
		tmpDict = gameStateDict['coinflip']
		if bankBalanceDict[ctx.author.name] >= int(args[1]):
			if ctx.author.name not in tmpDict.keys():
				tmpDict[ctx.author.name] = [args[0], int(args[1])]
				gameStateDict['coinflip'] = tmpDict
				with open('game_state.json', 'w', encoding='utf-8') as f:
					json.dump(gameStateDict, f, ensure_ascii=False, indent=4)
				await ctx.send('success!')
		await ctx.send('failed lmao')

	async def betExecute(self, result, ctx):
		with open('game_state.json', 'r') as openfile:
			gameStateDict = json.load(openfile)
		with open('data.json', 'r') as openfile:
			bankBalanceDict = json.load(openfile)
		tmpDict = gameStateDict['coinflip']
		for key in tmpDict.keys():
			tmpList = tmpDict[key]
			if tmpList[0] == result:
				bankBalanceDict[key] += tmpList[1]
				await ctx.send(f"congratz {key}!")
			else:
				bankBalanceDict[key] -= tmpList[1]
				await ctx.send(f"sucks to suck {key}!")
		gameStateDict['coinflip'] = dict()
		with open('data.json', 'w', encoding='utf-8') as f:
			json.dump(bankBalanceDict, f, ensure_ascii=False, indent=4)
		with open('game_state.json', 'w', encoding='utf-8') as f:
			json.dump(gameStateDict, f, ensure_ascii=False, indent=4)


async def setup(bot):
	await bot.add_cog(coin_flip(bot))
