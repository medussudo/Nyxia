import disnake
from disnake.ext import commands
import gethonis
import asyncio

class GethonisCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="Gethonis")
	async def getho(inter, ctx, message):
		await ctx.response.defer()
		msg = await ctx.followup.send("Please Wait...")
		bot = gethonis.Gethonis(TOKEN_GETHONIS, "gethonis", False, "https://gethonis.com/")
		async with ctx.channel.typing():
			response = await asyncio.to_thread(bot.get_message, message)
			await msg.edit(content=response)