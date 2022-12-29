import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Kicke einen Member")
    @discord.default_permissions(kick_members=True)
    async def kick(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.kick()
        except (discord.Forbidden, discord.HTTPException) as e:
            print(e)
            await ctx.respond("Du hast keine Berechtigungen dafür")
            return
        await ctx.respond(f"{member.mention} got kicked!")

    @slash_command(description="Banne einen Member")
    @discord.default_permissions(ban_members=True)
    async def ban(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.ban()
        except (discord.Forbidden, discord.HTTPException) as e:
            print(e)
            await ctx.respond("Du hast keine Berechtigungen dafür")
            return
        await ctx.respond(f"{member.mention} got banned!")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        await ctx.respond(f"An error has occurred: ´´´{error}´´´", ephemeral=True)
        raise error


def setup(bot):
    bot.add_cog(Admin(bot))
