from discord.ext import commands


class Template(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Template has loaded')

	@commands.command()
	async def command(self, ctx, *args):
		pass


async def setup(bot):
	await bot.add_cog(Template(bot))
