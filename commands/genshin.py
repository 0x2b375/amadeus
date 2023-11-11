import discord
from discord.ext import commands


class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="genshin")
    async def genshin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please specify a valid subcommand: wrio")

    @genshin.command(name="wrio")
    async def wrio(self, ctx):
        """Check Wriothesley's farm guide"""
        nl = "\n"
        message = (
            f"Mon: Stormterror x1, Wolf x2/Ley line xp book{nl}"
            f"Tue: Boss/Artifact{nl}"
            f"Wed: Talent{nl}"
            f"Thu: Boss/Artifact{nl}"
            f"Fri: Boss/Artifact{nl}"
            f"Saturday: Talent{nl}"
            f"Sun: Talent/Weapon"
        )
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(Genshin(bot))
