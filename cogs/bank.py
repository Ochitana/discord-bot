from discord.ext import commands
import json


class Bank(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.balances = dict()

	@commands.Cog.listener()
	async def on_ready(self):
		print('Bank has loaded')

	#TODO: Interest system

	@commands.command()
	async def bank(self, ctx, *args):
		with open('data.json', 'r') as openfile:
			self.balances = json.load(openfile)
		# !bank balance
		if args[0] == 'balance':
			if ctx.author.name not in self.balances.keys():
				self.balances[ctx.author.name] = 100
			await ctx.send(f"Your balance is: ${self.balances[ctx.author.name]}")
			if self.balances[ctx.author.name] == 0:
				await ctx.send('stop being poor')

		# !bank transfer person amount
		if args[0] == 'transfer':
			await self.transfer(ctx, args)

		with open('data.json', 'w', encoding='utf-8') as f:
			json.dump(self.balances, f, ensure_ascii=False, indent=4)

	async def transfer(self, ctx, args):
		tmpNum = int(args[2])
		if args[1] not in self.balances.keys():
			await ctx.send('Invalid recipient')
			return
		if tmpNum > self.balances[ctx.author.name]:
			await ctx.send('Better Call Saul')
			return
		self.balances[ctx.author.name] -= tmpNum
		self.balances[args[1]] += tmpNum
		await ctx.send('Funds transferred')


async def setup(bot):
	await bot.add_cog(Bank(bot))
