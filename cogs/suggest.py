import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

class suggest(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "建議", description = "有任何想要跟作者提出的建議或新增什麼功能嗎? 趕快來使用吧:D")
    @app_commands.describe(內容 = "輸入你要提的建議")
    async def suggest(self, interaction: discord.Interaction, 內容: str):
        channel_id = 1302915721373683712
        
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(title=內容,
                      colour=0xca215c,
                      timestamp=datetime.now())
        user = interaction.user.name
        embed.set_author(name= f"{user} 提出了一個建議/想法:",icon_url= interaction.user.avatar)
        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
        await channel.send(embed=embed)

        # 沒有下面一段會導致Discord認定機器人沒有回應
        # ephemeral=True 代表只能該用戶可視
        await interaction.response.send_message("感謝你提出建議讓北極企鵝變得更好:D", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(suggest(bot))