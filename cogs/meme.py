import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from random import choice
from discord.app_commands import Choice
from typing import Optional

colors = [
    0xc97e4d, 0x8cbf5e, 0x6aa2d2, 0xe6a157, 0xb37ca1, 0x59a5a2, 0xde8579, 
    0x9289b8, 0xa2b872, 0xcb9763, 0x798ea4, 0xbf677a, 0x7aa861, 0x9a7a5c, 
    0x669f99, 0xb2a35c, 0xd17769, 0x7189c0, 0x9c8b77, 0x848f73
]

class meme(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="迷因", description="點此發送一次迷因吧!")
    @app_commands.describe(選擇迷因="請選擇你要的迷因")
    @app_commands.choices(選擇迷因=[
        Choice(name="RollingSkyKids", value="1"),
        Choice(name="太鼓達人", value="2"),
        Choice(name="叭叭叭", value="3"),
        Choice(name="叭叭狐", value="4"),
        Choice(name="新蓬萊之槌", value="5"),
        Choice(name="企鵝·犯罪", value="6"),
        Choice(name="企鵝·TMD", value="7"),
        Choice(name="企鵝·操!", value="8"),
        Choice(name="原神啟動!", value="9"),
        Choice(name="品客瑞克搖", value="10")
    ])
    async def meme(self, interaction: discord.Interaction, 選擇迷因: Optional[str] = None):
        gif_url = [
            "https://imgur.com/qBlth1H.gif",
            "https://imgur.com/mEJFEtR.gif",
            "https://imgur.com/hGE6umV.gif",
            "https://imgur.com/xW8boYw.gif",
            "https://imgur.com/bIDT8oz.gif",
            "https://c.tenor.com/27v8vpDLubsAAAAC/tenor.gif",
            "https://c.tenor.com/wxoWW3t8VVIAAAAC/tenor.gif",
            "https://c.tenor.com/FqOiNT34Tn0AAAAC/tenor.gif",
            "https://media1.tenor.com/m/fDSBzsHOFboAAAAC/%E5%8E%9F%E7%A5%9E-%E5%90%AF%E5%8A%A8.gif",
            "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmZoMXdld2ExYTloOG45eXc4MmQ0NmdrZjNtcGdqejl0N2p5NTd1YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8CSpGec911fwZJ24Nv/giphy.gif"
        ]
        index = int(選擇迷因) - 1
        await interaction.response.send_message(gif_url[index])

async def setup(bot: commands.Bot):
    await bot.add_cog(meme(bot))  