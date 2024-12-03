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

class help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="幫助", description="在這裡可以查看機器人的用法喔!")
    @app_commands.describe(選擇幫助="請選擇你要詢問的指令用法(或是不輸入來查看全部)")
    @app_commands.choices(選擇幫助=[
    Choice(name="/介紹", value="1"),
    Choice(name="/幫助", value="2"),
    Choice(name="/匿名說", value="3"),
    Choice(name="/迷因", value="4"),
    Choice(name="/大聲說", value="5"),
    Choice(name="/想玩機器人", value="6"),
    Choice(name="/規則", value="7"),
    Choice(name="/剪刀石頭布", value="8"),
    Choice(name="/更新公告", value="9"),
    Choice(name="/建議", value="10"),
    Choice(name="/數數字", value="11"),
    Choice(name="/音樂新增建議", value="12"),
    Choice(name="/設定歡迎消息", value="13"),
    Choice(name="/簽到", value="14"),
    Choice(name="/服務條款", value="15"),
    Choice(name="/密碼", value="16"),
    Choice(name="/伺服器設定", value="17"),
    Choice(name="/用戶設定", value="18"),
    Choice(name="/企鵝的小小小窩介紹", value="19"),
    Choice(name="/開發者選項", value="20")
    ])
    async def help(self, interaction: discord.Interaction, 選擇幫助: Optional[Choice[str]] = None):
        help = [
            "/介紹 :",
            "/幫助 (選擇幫助) :",
            "/匿名說 [發送的伺服器] [內容] :",
            "/迷因 [選項] :",
            "/大聲說 [內容] :",
            "/想玩機器人 (奇怪的選擇咚咚):",
            "/規則 (選擇幫助) :",
            "/剪刀石頭布 :",
            "/更新公告 :",
            "/建議 [內容] :",
            "/數數字 :",
            "/音樂新增建議 [內容] :",
            "/設定歡迎消息 :",
            "/簽到 :",
            "/服務條款 :",
            "/密碼 [密碼] :",
            "/伺服器設定 [選項] [狀態] :",
            "/用戶設定 [選項] [狀態] :",
            "/企鵝的小小小窩介紹",
            "/開發者選項 [動作] [選擇更新的模組]"
        ]
        description = [
            "發送出北極企鵝的基本簡介。",
            "你可以使用這個指令來得到北極企鵝的幫助。若不選擇可以發送全部的幫助喔:D",
            "發送一條匿名訊息到指定的伺服器。",
            "發送一條北極企鵝推薦的迷因Gif。",
            "發送一條大聲說的話，會用機器人幫你以較大字體展示。",
            "一個小彩蛋，你可以試試看。",
            "你可以選擇發送整條 '溫暖領航團' 團規，或是發送單條的團規。(備註: 本功能為專屬於溫暖領航團之功能。)",
            "和電腦猜拳，無聊時可以玩喔。",
            "發送最新一期北極企鵝的更新公告出來。",
            "向我們提供你的想法或建議。",
            "開始遊玩數數字的遊戲。(備註:建議每個人發送的訊息間隔一秒鐘，且不可同一個人連續發送數字，否則遊戲會結束。)",
            "為未來的播放音樂功能提供之音樂的建議。",
            "設定自己伺服器的專屬歡迎消息喔! (備註: {member} 會顯示用戶名稱， {count} 會顯示伺服器人數, {guild} 會顯示伺服器名稱。)",
            "每天一簽，來看看誰的簽到數量最大吧!(備註:排行榜等到有人簽到數達到10才開啟)",
            "發出北極企鵝的服務條款。",
            "一個密碼系統，不知道可以拿來幹啥。",
            "可以設定伺服器的一些功能。",
            "可以設定用戶的一些功能。",
            "僅企鵝的小小小窩且為企鵝小小小窩管理員的人可以使用的介紹系統。",
            "開發者工具，僅北極企鵝開發者可以使用。"
        ]
        embed = discord.Embed(title="北極企鵝幫助區",description="有任何使用指令上的問題嗎? 看看下面的介紹是否可以讓你清楚呢?",colour=choice(colors),timestamp=datetime.now())

        if 選擇幫助:
            index = int(選擇幫助.value) - 1  # Convert to 0-based index
            embed.add_field(name=help[index], value=description[index], inline=False)
        else:
            for i in range(len(help)):
                embed.add_field(name=help[i], value=description[i], inline=False)
       
        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))  
