import discord
from discord.ext import commands

def is_admin(ctx):
    return ctx.author.guild_permissions.administrator

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def admin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f'Invalid admin command. Use `>admin kick` or `>admin ban`.')

    @admin.command()
    @commands.check(is_admin)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked for the reason: {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have permission to kick people.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to specify a member to kick.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("The member you are trying to kick is not in the server.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("I don't have permission to kick that member.")
        else:
            await ctx.send("An error occurred while trying to kick that member.")

    @admin.command()
    @commands.check(is_admin)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for the reason: {reason}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have permission to ban people.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to specify a member to ban.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("The member you are trying to ban is not in the server.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("I don't have permission to ban that member.")
        else:
            await ctx.send("An error occurred while trying to ban that member.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
