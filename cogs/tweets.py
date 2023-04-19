from discord.ext import commands
import tweepy

class Tweets(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Tweets has loaded')

	@commands.command()
	async def tweet(self, ctx, *args):
		pass


async def setup(bot):
	await bot.add_cog(Tweets(bot))
