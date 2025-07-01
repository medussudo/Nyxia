import disnake
from disnake.ext import commands
import random

class LoveArch0Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.target_user_id = 1148252680565821500

    @commands.Cog.listener()
    async def on_message(self, message):
        if "nyxia" in message.content.lower():
            if message.author.id != 1376945592470736986:
                await message.channel.send("Yes, cutie-pie?")

        if message.author.id == self.target_user_id and self.bot.user in message.mentions:
            try:
                with open("mention_responses.txt", "r", encoding="utf-8") as file:
                    responses = [line.strip() for line in file if line.strip()]
            except FileNotFoundError:
                await message.reply("⚠️ Mention response file not found.", mention_author=True)
                return

            if responses:
                await message.reply(random.choice(responses), mention_author=True)
            else:
                await message.reply("😶 I have nothing to say...", mention_author=True)

    #await self.bot.process_commands(message)
