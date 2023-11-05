import discord
import random
from discord.ext import commands


class Buud(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buud(self, ctx):
        user_id = [
            "232445753954402304", "715435199886000139", "1003509759862915083",
            "1150000323079962635"
        ]
        random_user = random.choice(user_id)
        await ctx.send(f"<@{random_user}> buuduulj uhlee..")


async def setup(bot):
    await bot.add_cog(Buud(bot))
 