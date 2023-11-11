import discord
import requests
import hmtai
import random
from discord.ext import commands


class Risky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def risky(self, ctx, category: str = None):
        """NSFW"""
        hentai_lists = [
            'anal', 'ass', 'bdsm', 'cum', 'classic', 'creampie', 'manga', 'femdom',
            'hentai', 'incest', 'masturbation', 'public', 'ero', 'orgy', 'elves',
            'yuri', 'pantsu', 'glasses', 'cuckold', 'blowjob', 'boobjob', 'footjob',
            'handjob', 'boobs', 'thighs', 'pussy', 'ahegao', 'uniform', 'gangbang',
            'tentacles', 'gif', 'zettaiRyouiki'
        ]
        hentai = random.choice(hentai_lists)
        hentai_img = hmtai.get("hmtai", hentai)
        channel_id = 800790726668451871
        channel = self.bot.get_channel(channel_id)
        if ctx.channel != channel:
            await ctx.send("You can't use this command on this channel.")
            return
        if category is not None:
            if category in hentai_lists:
                hentai_img = hmtai.get("hmtai", category)
                await ctx.send(hentai_img)
            else:
                available_categories = ', '.join(hentai_lists)
                await ctx.send(
                    f"Invalid category.\nAvailable categories: {available_categories}")
        else:
            hentai = random.choice(hentai_lists)
            hentai_img = hmtai.get("hmtai", hentai)
            await ctx.send(hentai_img)


async def setup(bot):
    await bot.add_cog(Risky(bot))
