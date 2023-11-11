import discord
import random
from discord.ext import commands


class Gaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gaming(self, ctx):
        """Choose your game"""
        games = ["Dota 2", "Valorant", "Shingen", "Apex Legend"]
        random_games = random.choice(games)
        if random_games == "Dota 2":
            await ctx.send(f"You can't choose your own game? shouganainaaa \n**{random_games}**")
        elif random_games == "Valorant":
            await ctx.send(f"You can't choose your own game? shouganainaaa \n**{random_games}**")
        elif random_games == "Shingen":
            await ctx.send(f"You can't choose your own game? shouganainaaa \n**{random_games}**")
        else:
            await ctx.send(f"You can't choose your own game? shouganainaaa \n**{random_games}**")


async def setup(bot):
   await bot.add_cog(Gaming(bot))
