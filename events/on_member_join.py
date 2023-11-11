import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from discord import File

class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 786220835974938668
        member_count = len(member.guild.members)
        channel = member.guild.get_channel(channel_id)
        if channel:
            background = Editor("images/hello.jpg")
            profile_image = await load_image_async(str(member.avatar.url))
            profile = Editor(profile_image).resize((150,150)).circle_image()
            poppins = Font.poppins(size=50, variant="bold")
            
            poppins_small = Font.poppins(size=20, variant="light")
            background.paste(profile, (325, 90))
            background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)
            
            background.text((400, 260), f"LAB MEMBER {member_count}" , color="white", font=poppins, align="center")
            background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
            file = File(fp=background.image_bytes, filename="images/hello.jpg")
            await channel.send(f"**YOUKOSOU {member.mention}!**")
            await channel.send(file=file)


async def setup(bot):
    await bot.add_cog(OnMemberJoinCog(bot))
