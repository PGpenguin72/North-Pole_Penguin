import random
import discord
from random import choice
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from discord.app_commands import Choice
from typing import Optional

colors = [
    0xc97e4d, 0x8cbf5e, 0x6aa2d2, 0xe6a157, 0xb37ca1, 0x59a5a2, 0xde8579, 
    0x9289b8, 0xa2b872, 0xcb9763, 0x798ea4, 0xbf677a, 0x7aa861, 0x9a7a5c, 
    0x669f99, 0xb2a35c, 0xd17769, 0x7189c0, 0x9c8b77, 0x848f73
]

class PSR(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="剪刀石頭布", description="來和電腦猜拳吧:D")
    @app_commands.describe(選擇出拳="請選擇你要出的拳")
    @app_commands.choices(選擇出拳=[
        Choice(name="剪刀", value="1"),
        Choice(name="石頭", value="2"), 
        Choice(name="布", value="3")
    ])
    async def PSR(self, interaction: discord.Interaction, 選擇出拳: Optional[str] = None):
        player_ans = [
            "剪刀",
            "石頭",
            "布"
        ]
        count = int(選擇出拳) - 1
        player = player_ans[count]
        computer = random.choice(["剪刀", "石頭", "布"])
        
        if player == computer:
            winner = "平手"
        elif player == "剪刀":
            if computer == "布":
                winner = "玩家贏了"
            else:
                winner = "電腦贏了"
        elif player == "石頭":
            if computer == "剪刀":
                winner = "玩家贏了"
            else:
                winner = "電腦贏了"
        else:
            if computer == "石頭":
                winner = "玩家贏了"
            else:
                winner = "電腦贏了"

        embed = discord.Embed(title="本次的猜拳結果是:",
                      description=winner,
                      colour=choice(colors),
                      timestamp=datetime.now())

        embed.set_author(name="猜拳小遊戲")

        embed.set_thumbnail(url="https://imgur.com/yG58Rw6.jpg")

        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
         
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(PSR(bot))  
