import disnake
from disnake.ext import commands
import random
import os


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Memes Army Imgs")
    async def hahaarmy(self, inter):
        images = os.listdir("armymemes")
        meme = random.choice(images)
        path = os.path.join("armymemes", meme)
        await inter.response.send_message(file=disnake.File(path))