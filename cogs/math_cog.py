import disnake
from disnake.ext import commands

class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="? steps until it reaches 1 - Collatz")
    async def collatz(self, inter: disnake.ApplicationCommandInteraction, number: int):
        if number <= 0:
            await inter.response.send_message("❌ Please enter a positive integer greater than 0.")
            return

        steps = 0
        original = number
        while number != 1:
            if number % 2 == 0:
                number //= 2
            else:
                number = number * 3 + 1
            steps += 1

        embed = disnake.Embed(
            title="🧮 Collatz Conjecture",
            description=f"{original} took **{steps}** steps to **reach 1**! ",
            color=disnake.Color.from_rgb(255,38,132)  # Hot pink!
        )
        embed.set_footer(text="Ask another number! 👀")
        await inter.response.send_message(embed=embed)
