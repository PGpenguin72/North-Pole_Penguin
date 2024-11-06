import discord
from discord import app_commands
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "大聲說", description = "當你想要大喊時，可以使用這個指令來大喊!!!")
    @app_commands.describe(內容 = "輸入你要大聲說的話")


    async def Message(self, interaction: discord.Interaction, 內容: str):
        user = interaction.user.name
        await interaction.response.send_message("*" + user + "*說\n> # " + 內容)

async def setup(bot: commands.Bot):
    await bot.add_cog(Message(bot))