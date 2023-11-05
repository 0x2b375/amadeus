import discord
import random
from discord.ext import commands


class Gaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gaming(self, ctx):
        games = ["Dota 2", "Valorant", "Shingen", "Apex Legend"]
        random_games = random.choice(games)
        if random_games == "Dota 2":
            await ctx.send(f"{random_games} - - - Tiirtsgeey!")
        elif random_games == "Valorant":
            await ctx.send(f"{random_games} - - - BUUDII!")
        elif random_games == "Shingen":
            await ctx.send(f"{random_games} - - - Impacters!")
        else:
            await ctx.send(f"{random_games} - - - chillrelt!")


async def setup(bot):
   await bot.add_cog(Gaming(bot))
