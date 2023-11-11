import discord
import random
import typing
import datetime
from discord.ext import commands
from discord import app_commands

eight_ball_responses = [
    "It is certain", "It is decidedly so", "Without a doubt",
    "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely",
    "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again",
    "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "My reply is no",
    "My sources say no", "Outlook not so good", "Very doubtful"
]


class EightballSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='8ball', description='Ask the magic 8-ball a question')
    async def eight_ball(self, interaction: discord.Interaction, *, question: str):
        ballresponse = random.choice(eight_ball_responses)
        user_display_name = interaction.user.display_name
        title = f"<:the8ball:1157555345368043570> | {ballresponse}, {user_display_name}"
        embed_color = discord.Color.from_rgb(113, 7, 7)
        embed = discord.Embed(title=title, description="", color=embed_color)
        embed.set_footer(text="Know your fortune.")
        await interaction.response.send_message(embed=embed)

        
async def setup(bot):
    await bot.add_cog(EightballSlash(bot))
 