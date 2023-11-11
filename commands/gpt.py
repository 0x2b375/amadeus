
import requests
import json
from discord.ext import commands


class Gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gpt(self, ctx, *, content: str):
      """Ask anything from AI"""
      url = "https://chatgpt-api8.p.rapidapi.com/"

      payload = [{"content": content, "role": "user"}]
      headers = {
          "content-type": "application/json",
          "X-RapidAPI-Key": "ef2f58efa4msh7876203c9f2a5ccp1e6fe1jsncc94e6b01516",
          "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
      }
      response = requests.post(url, json=payload, headers=headers)
      data = response.json()
      if 'text' in data:
        await ctx.send(json.loads(response.text)['text'])
      else:
        await ctx.send("Margaash ashiglaarai.")
        
async def setup(bot):
    await bot.add_cog(Gpt(bot))
