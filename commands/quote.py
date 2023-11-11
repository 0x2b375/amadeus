import discord
import requests
from discord.ext import commands


class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx, cat: str):
      """Inspire yourself with this"""
      url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
      category = cat
      querystring = {"cat": category, "count": "1"}
      valid_categories = ["movies", "famous"]
      if cat.lower() not in valid_categories:
        await ctx.send(
            "Invalid category. Please choose either 'movies' or 'famous'.")
        return

      headers = {
          "X-RapidAPI-Key": "ef2f58efa4msh7876203c9f2a5ccp1e6fe1jsncc94e6b01516",
          "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com"
      }

      response = requests.post(url, headers=headers, params=querystring)
      response.raise_for_status()

      data = response.json()
      if isinstance(data, list) and len(data) > 0:
        quote_data = data[0]
        embed = discord.Embed(title="", color=discord.Colour.from_rgb(113, 7, 7))
        embed.add_field(name="Author", value=quote_data["author"], inline=False)
        embed.add_field(name="Quote", value=quote_data["quote"], inline=False)
        embed.add_field(name="Category",
                        value=quote_data["category"],
                        inline=False)
        await ctx.send(embed=embed)
      else:
        await ctx.send("Try again.")
        
        
    @quote.error
    async def quote_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to choose category. famous or movies")

async def setup(bot):
    await bot.add_cog(Quote(bot))
