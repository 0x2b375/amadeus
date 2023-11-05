from discord.ext import commands


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vote(ctx, question, *choices):
        if len(choices) < 2:
            await ctx.send("Please provide at least two choices for the vote.")
            return

        formatted_choices = "\n".join(
            [f"{index + 1}. {choice}" for index, choice in enumerate(choices)])
        poll_message_text = f"**{ctx.author.name}** asks: {question}\n\n{formatted_choices}"
        poll_message = await ctx.send(poll_message_text)

        for emoji in [chr(127462 + index) for index in range(len(choices))]:
            await poll_message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(Vote(bot))
