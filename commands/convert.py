import typing
from discord.ext import commands

class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group()
    async def convert(self, ctx):
        """Convert things using this command, >help convert"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f'Invalid subcommand. Use `>help convert`.')
    
    @convert.command()
    async def hex(self, ctx, number: typing.Union[int, str]):
        """Converts a decimal number to hex etc"""
        if isinstance(number, int):
            await ctx.send(f"{number} in decimal is {hex(number)[2:]} in hex.")
        elif isinstance(number, str):
            try:
                if number.startswith('0x'):
                  decimal_number = int(number, 16)
                  hex_representation = hex(decimal_number)[2:]
                  
                  await ctx.send(f"{number} in hex is {decimal_number} in decimal.")
                elif number.startswith('0b'):
                    decimal_number = int(number, 2)
                    binary_representation = bin(decimal_number)[2:]
                    hex_representation = hex(decimal_number)[2:]
                    await ctx.send(f"{binary_representation} in binary is {hex_representation} in hex.")
                elif number.startswith('0o'):
                    decimal_number = int(number, 8)
                    octal_representation = oct(decimal_number)[2:]
                    hex_representation = hex(decimal_number)[2:]
                    await ctx.send(f"{octal_representation} in octal is {hex_representation} in hex.")
            except ValueError:
                await ctx.send(f"Invalid hex input: {number}")

    @convert.command()
    async def octagon(self, ctx, number: typing.Union[int, str]):
        """Converts a decimal number to octal etc"""
        if isinstance(number, int):
            await ctx.send(f"{number} in decimal is {oct(number)[2:]} in octal.")
        elif isinstance(number, str):
            try:
                if number.startswith('0b'):
                  decimal_number = int(number, 2)
                  octal_representation = oct(decimal_number)[2:]
                  binary_representation = bin(decimal_number)[2:]
                  await ctx.send(f"{binary_representation} in binary is {octal_representation} in octal.")
                elif number.startswith('0x'):
                  decimal_number = int(number, 16)
                  hex_representation = hex(decimal_number)[2:]
                  octal_representation = oct(decimal_number)[2:]
                  await ctx.send(f"{hex_representation} in hex is {octal_representation} in octal.")
                elif number.startswith('0o'):
                  decimal_number = int(number, 8)
                  octal_representation = oct(decimal_number)[2:]
                  await ctx.send(f"{octal_representation} in octal is {decimal_number} in decimal.")
            except ValueError:
                await ctx.send(f"Invalid octal input: {number}")

    @convert.command()
    async def binary(self, ctx, number: typing.Union[int, str]):
        """Converts a decimal number to binary etc"""
        if isinstance(number, int):
            await ctx.send(f"{number} in decimal is {bin(number)[2:]} in binary.")
        elif isinstance(number, str):
            try:
                if number.startswith('0x'):
                  decimal_number = int(number, 16)
                  hex_representation = hex(decimal_number)[2:]
                  binary_representation = bin(decimal_number)[2:]
                  await ctx.send(f"{hex_representation} in hex is {binary_representation} in binary.")
                elif number.startswith('0o'):
                  decimal_number = int(number, 8)
                  octal_representation = oct(decimal_number)[2:]
                  binary_representation = bin(decimal_number)[2:]
                  await ctx.send(f"{octal_representation} in octal is {binary_representation} in binary.")
                elif number.startswith('0b'):
                  decimal_number = int(number, 2)
                  binary_representation = bin(decimal_number)[2:]
                  await ctx.send(f"{binary_representation} in binary is {decimal_number} in decimal.")
            except ValueError:
                await ctx.send(f"Invalid binary input: {number}")

async def setup(bot):
    await bot.add_cog(Converter(bot))
