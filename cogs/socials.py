import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def socials(
            self, ctx,
            von: Option(str, choices=["vegy", "ananassosse"])

    ):
        if von == "vegy":
            embed = discord.Embed(
                title="vegys Socials",
                color=0x4d6fd8,
            )

            embed.add_field(name=f'\u200b\n',
                            value=f'[[YouTube]](https://www.youtube.com/@dasvegy)\n'
                                  f'[[Soundcloud]](https://soundcloud.com/dasvegy)\n'
                                  f'[[Twitch]](https://www.twitch.tv/dasvegy)\n'
                                  f'[[Twitter]](https://twitter.com/dasvegy)\n'
                                  f'[[Instagram]](https://www.instagram.com/dasvegy/)\n',
                            inline=False)

            await ctx.respond(embed=embed)

        elif von == "ananassosse":
            embed = discord.Embed(
                title="ananassosses Socials",
                color=0x4d6fd8,
            )

            embed.add_field(name=f'\u200b\n',
                            value=f'[[YouTube]](https://www.youtube.com/channel/UCkudjUdOOAvRt1DxWF3yakQ)\n'
                                  f'[[Soundcloud]](https://soundcloud.com/andre-gamerlp)\n'
                                  f'[[Twitch]](https://www.twitch.tv/ananassosse)\n'
                                  f'[[Twitter]](https://twitter.com/ananassosse)\n'
                                  f'[[Instagram]](https://www.instagram.com/ananassosse/)\n',
                            inline=False)

            await ctx.respond(embed=embed)

        await ctx.respond("Hier die Socials!")


def setup(bot):
    bot.add_cog(Socials(bot))