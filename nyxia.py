import disnake
from disnake.ext import commands
import gethonis
import random
import asyncio
import os 
from dotenv import load_dotenv
from disnake import Option
from cogs import FunCog, PDFCog, LoveArch0Cog, MathCog, GethonisCog, RandomTextCog

ai = gethonis.Gethonis(TOKEN_GETHONIS, "gethonis", False, "https://api.gethonis.com")

bot = commands.Bot(intents=disnake.Intents.all())

@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.slash_command(description="Ping Pong")
async def ping(inter):
    await inter.response.send_message("Pong")



@bot.slash_command(description="Sends a pink embed with a message")
async def hello_embed(inter):
    embed = disnake.Embed(
        title="🌸 Hello, cutie!",
        description="This is a pink embed message 💖",
        color=disnake.Color.from_rgb(255,38,132)  # Hot pink!
    )
    embed.set_footer(text="With love, Nyxia")
    embed.set_thumbnail(url="https://i.imgur.com/your_icon_here.png")  # Optional

    await inter.response.send_message(embed=embed)



@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Load cogs BEFORE running the bot
def load_cogs():
    bot.add_cog(FunCog(bot))
    bot.add_cog(PDFCog(bot))
    bot.add_cog(LoveArch0Cog(bot))
    bot.add_cog(MathCog(bot))
    bot.add_cog(GethonisCog(bot))
    bot.add_cog(RandomTextCog(bot))
    #bot.add_cog(PromptCog(bot))

if __name__ == "__main__":
    print("🚀 Starting bot...")

    def load_cogs():
        try:
            bot.add_cog(FunCog(bot))
            bot.add_cog(PDFCog(bot))
            bot.add_cog(LoveArch0Cog(bot))
            bot.add_cog(MathCog(bot))
            bot.add_cog(GethonisCog(bot))
            bot.add_cog(RandomTextCog(bot))
            #bot.add_cog(PromptCog(bot))
            print("✅ All cogs loaded successfully.")
        except Exception as e:
            print(f"❌ Error loading cogs: {e}")

    load_cogs()  # Make sure to call the function here

    print("✅ Cogs loaded.")

    bot.run(TOKEN_NYXIA)
