import discord
import random
import typing
import datetime
from discord.ext import commands
from discord import app_commands

class PfpSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Pong!")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # Get the bot's latency in milliseconds
        await interaction.response.send_message(f'Pong! Bot Latency: {latency}ms')
    @app_commands.command(description='Shows profile picture')
    async def pfp(self, interaction: discord.Interaction, member: discord.Member=None):
        nl = "\n"
        if member == None:
          member = interaction.user
            
        embed = discord.Embed(
            title=f"{member.name}'s Profile Picture",
            color=discord.Colour.from_rgb(113, 7, 7),
            timestamp=datetime.datetime.utcnow()
        )
        png_url = member.avatar.url
        jpeg_url = member.avatar.replace(format="jpeg").url

        embed.set_image(url=png_url)
        embed.description = f"**Links as:**{nl}[PNG]({png_url}){nl}[JPEG]({jpeg_url})"

        await interaction.response.send_message(embed=embed)

        
async def setup(bot):
    await bot.add_cog(PfpSlash(bot))
 