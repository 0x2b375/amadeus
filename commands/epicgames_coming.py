import discord
import requests
from discord.ext import commands


class Epicgames_coming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def epicgames_coming(self, ctx):
      url = "https://epic-free-games.p.rapidapi.com/epic-free-games-coming-soon"

      headers = {
          "X-RapidAPI-Key": "ef2f58efa4msh7876203c9f2a5ccp1e6fe1jsncc94e6b01516",
          "X-RapidAPI-Host": "epic-free-games.p.rapidapi.com"
      }
      response = requests.get(url, headers=headers, timeout=5)
      response.raise_for_status()
      data = response.json()
      if isinstance(data, list) and len(data) > 0:
        game_data = data[0]
        embed = discord.Embed(title="Epic Free Game Coming Soon",
                              color=discord.Colour.from_rgb(113, 7, 7))
        embed.add_field(name="Name", value=game_data["name"], inline=False)
        embed.add_field(name="Description",
                        value=game_data["description"],
                        inline=False)
        embed.add_field(name="Publisher",
                        value=game_data["publisher"],
                        inline=True)
        embed.add_field(name="originalPrice",
                        value=game_data["originalPrice"],
                        inline=True)
        embed.add_field(name="discountPrice",
                        value=game_data["discountPrice"],
                        inline=True)
        embed.add_field(name="Link", value=game_data["appUrl"], inline=True)
        embed.set_image(url=game_data["offerImageTall"])
        await ctx.send(embed=embed)
      else:
        await ctx.send("No game data available.")


async def setup(bot):
    await bot.add_cog(Epicgames_coming(bot))
