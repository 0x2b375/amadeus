import discord
import requests
import datetime
from discord.ext import commands


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, day: int = 0):
      try:
        url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"
        querystring = {
            "place_id": "ulaanbaatar-hot",
            "language": "en",
            "units": "metric"
        }

        headers = {
            "X-RapidAPI-Key": "ef2f58efa4msh7876203c9f2a5ccp1e6fe1jsncc94e6b01516",
            "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
        }

        response = requests.get(url,
                                headers=headers,
                                params=querystring,
                                timeout=5)
        response.raise_for_status()
        data = response.json()

        daily_data = data.get('daily', {}).get('data', [])[day]
        embed = discord.Embed(title="Weather Information",
                              color=discord.Colour.from_rgb(113, 7, 7))
        embed.add_field(name="Date",
                        value=daily_data.get('day', 'N/A'),
                        inline=False)
        embed.add_field(name="Weather",
                        value=daily_data.get('weather', 'N/A'),
                        inline=False)
        embed.add_field(name="Summary",
                        value=daily_data.get('summary', 'N/A'),
                        inline=False)
        embed.add_field(name="Temperature",
                        value=f"{daily_data.get('temperature', 'N/A')}°C",
                        inline=False)
        embed.add_field(name="Temperature Min",
                        value=f"{daily_data.get('temperature_min', 'N/A')}°C",
                        inline=False)
        embed.add_field(name="Temperature Max",
                        value=f"{daily_data.get('temperature_max', 'N/A')}°C",
                        inline=False)
        embed.add_field(name="Feels Like",
                        value=f"{daily_data.get('feels_like', 'N/A')}°C",
                        inline=False)
        embed.add_field(name="Feels Like Min",
                        value=f"{daily_data.get('feels_like_min', 'N/A')}°C",
                        inline=False)
        embed.add_field(name="Feels Like Max",
                        value=f"{daily_data.get('feels_like_max', 'N/A')}°C",
                        inline=False)

        await ctx.send(embed=embed)

      except requests.exceptions.RequestException:
        await ctx.send(
            "An error occurred while fetching weather data. Please try again later."
        )
    @weather.error
    async def weather_error(self, ctx, error):
      current_date = datetime.datetime.now()
      if isinstance(error, commands.BadArgument):
        await ctx.send(f"You have to insert number. [{current_date} = 0]")

async def setup(bot):
    await bot.add_cog(Weather(bot))
