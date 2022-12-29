import discord
from discord.ext import commands
from discord.commands import message_command, user_command


class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @message_command(name="Message ID")
    async def get_ID(self, ctx, message):
        await ctx.respond(f"Die Message ID ist {message.id}", ephemeral=True)

    @user_command(name="User ID")
    async def get_ID(self, ctx, user):
        await ctx.respond(f"Die User ID ist {user.id}", ephemeral=True)


def setup(bot):
    bot.add_cog(Context(bot))
