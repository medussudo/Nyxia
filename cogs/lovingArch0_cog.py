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
        if True:
            channel_id = 1309940193389707294
            channel = self.bot.get_channel(channel_id)
            if channel:
                getho = gethonis.Gethonis("geth-Ecuw2g7oy9FIlN3RZMAOxw", "https://api.gethonis.com/")
                getho.set_listener(str(self.bot.user.id))
                result = getho.get_postaslistener()
                try:
                    raw_result = result[0]
                    parsed_data = json.loads(raw_result)
                    if parsed_data['Post']:
                        post = parsed_data['Post']
                        title = post.get("Title", "Untitled Post")
                        paragraphs = post.get("paragraphs", [])
                        footer_text = post.get("Footer", "")
                        joined_paragraphs = "\n\n".join(paragraphs)

                        embed = disnake.Embed(
                            title=title,
                            description="\n\n".join(paragraphs),
                        color=disnake.Color.gold()
                        )
                        embed.set_footer(text=footer_text)
                        output = textwrap.dedent(f"""
                        # {title}
                        {joined_paragraphs}
                        {footer_text}
                        """)
                        await channel.send(embed=embed)
                    else:
                        await channel.send("Looking for post")
                except:
                    print("Looking for post")
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
