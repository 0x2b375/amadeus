import discord
import re
import random
from discord.ext import commands


class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        msgs = [
            "bye", "gn", "sayonara", "goodnight", "untlaa", "oyasumi", "untla",
            "adios", "унтла", "унтлаа", "untalt"
        ]
        responses = [
            ("Operation Untalt",
             "https://tenor.com/view/steins-gate-deceive-the-world-deceive-world-victory-is-assured-gif-24393402"
             ),
            ("Goodnight!", "https://tenor.com/view/whsotak-venti-gn-gif-24078985"),
            ("Oyasumi!",
             "https://tenor.com/view/your-name-kiminonawa-shooting-star-anime-gif-17883512"
             )
        ]

        pattern = r'\b(?:' + '|'.join(map(re.escape, msgs)) + r')\b'

        if re.search(pattern, message.content.lower()):
            text, gif_url = random.choice(responses)
            await message.channel.send(f"{text}")
            await message.channel.send(f"{gif_url}")


async def setup(bot):
    await bot.add_cog(OnMessageCog(bot))
