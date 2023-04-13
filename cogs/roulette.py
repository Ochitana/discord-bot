from discord.ext import commands
import random


class Roulette(commands.Cog):
	# min_num = 1
	# max_num = 2
	# num_of_rand_numbers = 5

	# !yahtzee start
	#

	def __init__(self, client):
		self.client = client  # sets the client variable so we can use it in cogs

	@commands.Cog.listener()
	async def on_ready(self):
		# an example event with cogs
		print('Roulette has loaded')

	@commands.command()
	async def roulette(self, ctx, *args):
		if len(args) == 0:
			await ctx.send('Please get help')

## !roulette start
# all players set bets
# !roulette bet (money) (red,black,1-50)
# bet recorded
		# !roulette bet 50 red
		# bet recorded
		# !roulette roll
		# rolling...
		# 3
		# 2
		# 1
		# 20 red
		# Congrats: Joe, Kevin


async def setup(bot):
	await bot.add_cog(Roulette(bot))
