import discord
from discord import app_commands
from discord.ext import commands

class signs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "每日簽到訊息", description = "發送出每日簽到訊息。")
    async def signs(self, interaction: discord.Interaction):
        if interaction.user.id in [609189792571457550, 368643370756866048]:
            await interaction.response.send_message("# 新的一天已經開始! 趕快來簽到吧!!!\n> # </簽到:1304707527753203732>")
        else:
            await interaction.response.send_message("抱歉你不是管理員，無法使用這個功能。",ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(signs(bot))

