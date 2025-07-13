import disnake
from disnake.ext import commands, tasks
import textwrap
import gethonis
import asyncio

from dotenv import load_dotenv

load_dotenv()

class GethonisCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.channel_id = 1309940193389707294
        self.getho = geth.Gethonis("geth-Ecuw2g7oy9FIlN3RZMAOxw", "https://api.gethonis.com/")
        self.listen_for_posts.start()
    @tasks.loop(seconds=3)
    async def listen_for_posts(self):
        channel = self.bot.get_channel(self.channel_id)
        if channel:
        	self.getho.set_listener(str(self.bot.user.id))
        	result = self.getho.get_postaslistener()
        	try:
            	raw_result = result[0]
            	parsed_data = json.loads(raw_result)
            	if parsed_data.get("Post"):
                	post = parsed_data["Post"]
                	title = post.get("Title", "Untitled Post")
                	paragraphs = post.get("paragraphs", [])
                	footer_text = post.get("Footer", "")
                	joined_paragraphs = "\n\n".join(paragraphs)

                	embed = disnake.Embed(
                    	title=title,
                    	description=joined_paragraphs,
                    	color=disnake.Color.gold()
                	)
                	embed.set_footer(text=footer_text)

                	await channel.send(embed=embed)
            	else:
                	print("No post found yet.")
        	except Exception as e:
            	print(f"Eroare la parsarea postului: {e}")
            
	@commands.slash_command(description="Gethonis")
	async def getho(inter, ctx, message):
		await ctx.response.defer()
		msg = await ctx.followup.send("Please Wait...")
		bot = gethonis.Gethonis(os.getenv("TOKEN_GETHONIS"), "gethonis", False, "https://gethonis.com/")
		async with ctx.channel.typing():
			response = await asyncio.to_thread(bot.get_message, message)
			await msg.edit(content=response)
	@commands.slash_command(description="Gethonis")
	async def getho(inter, ctx, message):
		await ctx.response.defer()
		msg = await ctx.followup.send("Please Wait...")
		bot = gethonis.Gethonis(os.getenv("TOKEN_GETHONIS"), "gethonis", False, "https://gethonis.com/")
		async with ctx.channel.typing():
			response = await asyncio.to_thread(bot.get_message, message)
			await msg.edit(content=response)

