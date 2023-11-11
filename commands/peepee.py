import discord
from discord.ext import commands
import random


class Peepee(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def peepee(self, ctx, *mentions: discord.User):
        """( ͡° ͜ʖ ͡°)"""
        equals_count = random.randint(1, 20)
        if not mentions:
            mentions = [ctx.author]

        message = "8" + "=" * equals_count + "D"
        for user in mentions:
            embed = discord.Embed(
                title='peepee size machine',
                description=f"{user.name}'s peepee size\n" + message,
                color=discord.Colour.from_rgb(113, 7, 7)
            )
            await ctx.send(embed=embed
                           )
        if equals_count >= 10:
            await ctx.send("That's a big peepee!")
        elif equals_count >= 15:
            await ctx.send("( ͡° ͜ʖ ͡°)")
        else:
            await ctx.send("(ಠ_ಠ)")


async def setup(bot):
    await bot.add_cog(Peepee(bot))
