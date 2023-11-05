import discord
from discord.ext import commands


class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 786220835974938668
        color_bot = discord.Colour.from_rgb(141, 9, 9)
        welcome_message = f"Эрхэм {member.mention} танаа манай server-t нэгдсэнд баяр хүргэн мэндчилж байна XD"
        channel = member.guild.get_channel(channel_id)
        if channel:
            embed = discord.Embed(title="",
                                  description=welcome_message,
                                  color=color_bot)
            embed.set_image(
                url='https://media.tenor.com/rK3k9EgLkhEAAAAC/steins-gate.gif')
            message = await channel.send(embed=embed)
            await message.add_reaction("👋")


async def setup(bot):
    await bot.add_cog(OnMemberJoinCog(bot))
