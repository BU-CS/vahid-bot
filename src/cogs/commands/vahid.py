import logging
import os

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger(__name__)


class VahidCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="cs", description="Our mantra")
    async def cs(self, ctx: discord.Interaction):
        await ctx.response.send_message("Computer Science at Boston University.")

    @app_commands.command(name="hello", description="Gives a kind greeting")
    async def hello(self, ctx: discord.Interaction):
        await ctx.response.send_message("Hello there friend!")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(VahidCommands(bot))
    log.info("Commands loaded: vahid")
