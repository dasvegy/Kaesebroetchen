import discord
from discord.ext import commands, tasks
from discord.commands import slash_command


class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="Passagiere")
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(Task(bot))