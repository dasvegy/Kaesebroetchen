import discord
from discord.ext import commands, tasks
from discord.commands import slash_command

options = [
    discord.SelectOption(label="Administration", description="Beschreibung aller Commands der Administration",
                         emoji="<:mod_shield:1057779493672079461>"),
    discord.SelectOption(label="Meme Commands", description="Beschreibung aller Commands der Memes",
                         emoji="<:pepe:1057780202580738220>", value="gigachad"),
    discord.SelectOption(label="vegy", description="Infos über vegy",
                         emoji="<:AKiss:927647428511952937>")

]


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(HelpView())

    @slash_command()
    async def help(self, ctx):
        await ctx.respond("Wähle eine Kategorie", view=HelpView())


def setup(bot):
    bot.add_cog(Help(bot))


class HelpSelect(discord.ui.Select):
    def __init__(self):
        super().__init__(
            min_values=1,
            max_values=1,
            placeholder="Wähle eine Kategorie",
            options=options
        )

    async def callback(self, interaction):
        await interaction.response.send_message(f"Du hast {self.values[0]}")


class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Wähle eine Kategorie",
        options=options,
        custom_id="help"
    )
    async def select_callback(self, select, interaction):
        s = ""
        for auswahl in select.values:
            s += f"- {auswahl}\n"

        await interaction.response.send_message(f"Du hast folgendes ausgewählt:\n{s}")
