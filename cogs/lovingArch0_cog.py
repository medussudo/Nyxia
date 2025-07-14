import json, disnake, asyncio, random, textwrap
import gethonis as geth
from disnake.ext import commands

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
            """
                This function works only when a user sends a message.
                Random message on a server.
            """
            load_dotenv()
            channel_id = int(os.getenv('CHANNEL_POSTS')) # The channel where the posts will be posteds
            channel = self.bot.get_channel(channel_id)
            if channel:
                # Gethonis Setup
                getho = geth.Gethonis(os.getenv('TOKEN_GETHONIS'),os.getenv('BASEURL_GETHONIS'))
                getho.set_listener(str(self.bot.user.id))

                # Receives the answer
                result = getho.get_postaslistener()
                try:

                    # Preparing the Json
                    raw_result = result[0]
                    parsed_data = json.loads(raw_result)
                    if parsed_data['Post']:
                        post = parsed_data['Post']
                        title = post.get("Title", "Untitled Post")
                        paragraphs = post.get("paragraphs", [])
                        footer_text = post.get("Footer", "")
                        joined_paragraphs = "\n\n".join(paragraphs)

                        # Initiating the Embed
                        embed = disnake.Embed(
                            title=title,
                            description="\n\n".join(paragraphs),
                            color=disnake.Color.gold()
                        )
                        embed.set_footer(text=footer_text)


                        #   This is not in use anymore but can be used if you want to be sent as a message not as ambed
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
