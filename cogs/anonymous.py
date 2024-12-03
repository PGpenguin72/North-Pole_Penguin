import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from discord.app_commands import Choice
import json
from typing import Optional

with open('./json/anonymous.json', 'r', encoding='utf-8') as JSON_anonymous:
    data = json.load(JSON_anonymous)

class anonymous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "匿名說", description = "當你想要偷偷說話不想被別人知道你是誰時，可以使用這個指令。(備註:不適合發長篇文章)")
    @app_commands.describe(發送的伺服器 = "請選擇你要發送到的地方",內容 = "輸入你要偷偷說的話")
    @app_commands.choices(發送的伺服器=[
        Choice(name= "北極企鵝官方支援伺服器", value="1302293453459423253" )
    ])
    async def anonymous(self, interaction: discord.Interaction, 發送的伺服器: str, 內容: str):
        Channel = data.get(發送的伺服器)
        CHlog_id = Channel.get("log_CH")
        channel_id = Channel.get("channel_id")
        
        channel = self.bot.get_channel(int(channel_id))
        CHlog = self.bot.get_channel(int(CHlog_id))
        embed = discord.Embed(title=內容,
                      colour=0xca215c,
                      timestamp=datetime.now())

        embed.set_author(name="一個匿名者說了:")

        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
        await channel.send(embed=embed)
        user = interaction.user.name
        await CHlog.send(f"{user} 發送了【{內容}】到<#{channel_id}> 裡面。")
        # 沒有下面一段會導致Discord認定機器人沒有回應
        # ephemeral=True 代表只能該用戶可視
        await interaction.response.send_message("送出囉~", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(anonymous(bot))
