import disnake
from disnake.ext import commands
import pdfkit
import uuid
import os

class PDFCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Convert website to PDF")
    async def web2pdf(self, inter, url: str):
        await inter.response.defer(with_message=True)

        try:
            filename = f"{uuid.uuid4()}.pdf"
            css_file = f"{uuid.uuid4()}.css"

            with open(css_file, "w") as f:
                f.write("body { background: white !important; }")

            config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
            options = {
                'print-media-type': '',
                'user-style-sheet': css_file,
            }

            pdfkit.from_url(url, filename, configuration=config, options=options)

            await inter.followup.send(file=disnake.File(filename))
            os.remove(filename)
            os.remove(css_file)

        except Exception as e:
            await inter.followup.send(f"❌ Could not generate PDF: `{e}`")
