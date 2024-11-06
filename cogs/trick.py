import discord
from discord import app_commands
from discord.ext import commands

class trick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "想玩機器人", description = "如果你想玩這個機器人，你可以使用這個指令。")
    async def trick(self, interaction: discord.Interaction):
        await interaction.response.send_message("# 叫你亂玩的喔(? 不要隨便玩我好嗎:( 給你一個小懲罰 \n ## (註:開個小玩笑 別走心阿:D) \n https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(trick(bot))