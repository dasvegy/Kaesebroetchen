import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def memes(
            self, ctx,
            meme: Option(str, choices=["gigachad", "tlowraps"])

    ):
        if meme == "gigachad":
            await ctx.respond("https://media.tenor.com/yPUAJMwL2uwAAAAC/gigachad.gif")

        elif meme == "tlowraps":
            await ctx.respond("https://cdn.discordapp.com/attachments/1039591507306500189/1054514409436893184/tlowraps.mp4")


def setup(bot):
    bot.add_cog(Memes(bot))

