from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
	return "I'm alive"


def keep_alive():
	# Keeps bot alive
	t = Thread(target=app.run(host='0.0.0.0', port=8080))
	t.start()


class KeepAlive(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('KeepAlive has loaded')
		keep_alive()


async def setup(bot):
	await bot.add_cog(KeepAlive(bot))
