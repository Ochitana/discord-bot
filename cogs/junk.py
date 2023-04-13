from discord.ext import commands


class Junk(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Junk has loaded')

	# @commands.command()
	# async def givememoney(ctx):
	# 	if ctx.author.name in allowlist:
	# 		await ctx.send('take it')
	# 	else:
	# 		await ctx.send('get out')

	@commands.command()
	async def saymyname(self, ctx):
		user_name = ctx.author.name
		await ctx.send(user_name)

	@commands.command()
	async def makeitrain(self, ctx):
		await ctx.send('https://tenor.com/view/money-make-it-rain-gif-26525310')

	@commands.command()
	async def dealmein(self, ctx):
		await ctx.message.add_reaction('👌')

	@commands.command()
	async def echo(self, ctx):
		message = ctx.message.content
		for x in range(len(message)):
			if message[x] == ' ':
				await ctx.send(message[x:])
				break

		if x == len(message) - 1:
			await ctx.send('_but nothing could be heard..._')


async def setup(bot):
	await bot.add_cog(Junk(bot))
