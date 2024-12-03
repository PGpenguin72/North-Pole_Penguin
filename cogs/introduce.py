import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from random import choice

colors = [
    0xc97e4d, 0x8cbf5e, 0x6aa2d2, 0xe6a157, 0xb37ca1, 0x59a5a2, 0xde8579, 
    0x9289b8, 0xa2b872, 0xcb9763, 0x798ea4, 0xbf677a, 0x7aa861, 0x9a7a5c, 
    0x669f99, 0xb2a35c, 0xd17769, 0x7189c0, 0x9c8b77, 0x848f73
    ]

class introduce(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "介紹", description = "告訴你一些事情。")
    async def introduce(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="歡迎使用北極企鵝!",
            description="北極企鵝是一隻由PG企鵝及北極貓開發的機器人喔~",
            colour=choice(colors),
            timestamp=datetime.now()
            )
        embed.add_field(
            name="我可以做什麼?",
            value="目前我的功能少之又少，因為這隻企鵝正在努力開發，學習如何寫discord bot，所以沒辦法一下子就寫出一個超級厲害的功能TwT",
            inline=False
            )
        embed.add_field(
            name="如何開始使用呢?",
            value="你可以輸入 \"/\" 然後點選我，選擇目前有的功能，你就可以使用了喔!",
            inline=False
            )
        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")    
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(introduce(bot))

