import logging
import os

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger(__name__)


class GeneralCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Checks if the bot is responding")
    @app_commands.guilds(
        discord.Object(os.environ.get("DISCORD_GUILD_ID", "DISCORD_GUILD_ID_MISSING"))
    )
    async def ping(self, ctx: discord.Interaction):
        await ctx.response.send_message("Pong!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GeneralCommands(bot))
    log.info("Commands loaded: general")
