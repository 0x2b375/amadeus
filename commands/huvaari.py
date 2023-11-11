import discord
from discord.ext import commands


class Huvaari(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def huvaari(self, ctx, user: discord.Member):
        """Shows huvaari of registered people"""
        user_id = str(user.id)
        user_images = {
            "232445753954402304":
            "https://cdn.discordapp.com/attachments/911917339191164958/1145390926001340466/image.png",
            "1003509759862915083":
            "https://cdn.discordapp.com/attachments/911917339191164958/1148255229922508810/image.png",
            "715435199886000139":
            "https://cdn.discordapp.com/attachments/786220835974938668/1148254920424829009/image.png",
            "470354634142384128":
            "https://cdn.discordapp.com/attachments/1143584916601311313/1148929313488519168/654d2101cfbf758c.png",
            "1150000323079962635":
            "https://cdn.discordapp.com/attachments/911917339191164958/1156138596990996501/image.png",
            "444150198030041089":
            "https://cdn.discordapp.com/attachments/786220835974938668/1159496326082465884/image.png"
        }
        if user_id in user_images:
            img_url = user_images[user_id]
            embed = discord.Embed(
                title=f"{user.name}-ийн хуваарь",
                color=discord.Colour.from_rgb(113, 7, 7)
            )
            embed.set_image(url=img_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The mentioned user does not have a picture.")
            
    @huvaari.error
    async def huvaari_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        await ctx.send("I could not find that member.")
      elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to mention someone.")


async def setup(bot):
    await bot.add_cog(Huvaari(bot))
