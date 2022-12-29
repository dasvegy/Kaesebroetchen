import discord
from discord.ext import commands
from discord.commands import slash_command


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Grüße einen Member")
    async def greet(self, ctx):
        await ctx.respond(f"Willkommen {ctx.author.mention}! ")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Willkommen",
            description=f"Hey {member.mention}! <:peepoHappy:1054178719301898380>",
            color=0x4d6fd8,
        )

        channel = await self.bot.fetch_channel(1040743584770568303)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Greet(bot))
