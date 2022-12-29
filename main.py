import discord
import os

from discord import Status
from dotenv import load_dotenv
from discord.ext import commands
from discord.commands import slash_command, Option

intents = discord.Intents.default()
intents.members = True

status = discord.Status.idle
activity = discord.Activity(type=discord.ActivityType.streaming, name="vegy", url="https://www.twitch.tv/ananassosse")

bot = discord.Bot(
    intents=intents,
    debug_guilds=[913500523016126495],
    status=status,
    activity=activity
)


@bot.event
async def on_ready():
    print(f"{bot.user} ist Online")


if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("TOKEN"))
