import logging
import os

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger(__name__)


class AdminCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="purge", description="Mass deletes messages")
    @app_commands.default_permissions(manage_messages=True)
    @app_commands.guild_only()
    @app_commands.describe(amount="Amount of messages to delete (1-99)")
    async def purge(self, ctx: discord.Interaction, amount: int):
        # Only allow command to be used in text channels
        if not isinstance(ctx.channel, discord.TextChannel):
            await ctx.response.send_message(
                "This command can only be used in text channels"
            )
            return

        # Only allow amount to be between 1 and 100
        if amount < 1 or amount > 99:
            await ctx.response.send_message("Amount must be between 1 and 99")
            return

        await ctx.channel.purge(limit=amount)
        await ctx.response.send_message(f"Deleted {amount} messages", delete_after=3)

    @app_commands.command(name="say", description="Send message through the bot")
    @app_commands.default_permissions(administrator=True)
    @app_commands.guild_only()
    @app_commands.describe(message="Message to send")
    async def say(self, ctx: discord.Interaction, message: str):
        # Only allow command to be used in text channels
        if not isinstance(ctx.channel, discord.TextChannel):
            await ctx.response.send_message(
                "This command can only be used in text channels"
            )
            return

        await ctx.channel.send(message)
        await ctx.response.send_message("Message sent", ephemeral=True)

    @app_commands.command(name="status", description="Set bot status")
    @app_commands.default_permissions(administrator=True)
    @app_commands.guild_only()
    @app_commands.describe(status="Text to change status to")
    async def status(self, ctx: discord.Interaction, status: str):
        await self.bot.change_presence(activity=discord.Game(name=status))
        await ctx.response.send_message("Status changed", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AdminCommands(bot))
    log.info("Commands loaded: admin")
