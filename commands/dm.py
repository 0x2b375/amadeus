import discord
from discord.ext import commands


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, message=None):
      """Direct message to user"""
      if user == ctx.author:
        await ctx.send("I cannot send a DM to myself.")
        return
      try:
        if message is not None:
          embed = discord.Embed(description=message)
          await user.send(embed=embed)
        else:
          await ctx.send("You must provide a message to send.")
      except discord.Forbidden:
        await ctx.send("I don't have permission to send DMs to that user.")
      except discord.HTTPException:
        await ctx.send("An error occurred while sending the message.")
      


async def setup(bot):
    await bot.add_cog(Dm(bot))
