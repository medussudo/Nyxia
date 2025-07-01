import disnake
from disnake.ext import commands
import random
import os 
from disnake import Option

class RandomTextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Dark Joke")
    async def joke(self, inter: disnake.ApplicationCommandInteraction):
        filename = 'jokes.txt'
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        # Split jokes by blank line
        jokes = [j.strip() for j in content.split("\n\n") if j.strip()]
        chosen_joke = random.choice(jokes)

        embed = disnake.Embed(
            title="😈 Dark Joke",
            description=chosen_joke,
            color=disnake.Color.from_rgb(255,38,132)
        )
        embed.set_footer(text="Don't take it personally ;))")

        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="Date ideas")
    async def dates(self, inter: disnake.ApplicationCommandInteraction):
        filename = 'dates.txt'
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        dates = [j.strip() for j in content.split("\n\n") if j.strip()]
        chosen_dates = random.choice(dates)
        await inter.response.send_message(chosen_dates)


    @commands.slash_command(description="magic 8-ball")
    async def eightball(self, inter, question: str = Option("question", description="Your question to the magic 8-ball")):
        with open("8ball_responses.txt", "r", encoding="utf-8") as file:
                responses = [line.strip() for line in file if line.strip()]
        if responses:
            reply = random.choice(responses)

            embed = disnake.Embed(
                title="🎱 Magic 8-Ball",
                description=f"> **You :** {question}\n> **Nyxia :** {reply}",
                color=disnake.Color.from_rgb(255,38,132)  # Hot pink!
            )
            embed.set_footer(text="Ask again anytime! 🔮")
            await inter.response.send_message(embed=embed)
        else:
            await inter.response.send_message("😕 No responses found in the file.")
