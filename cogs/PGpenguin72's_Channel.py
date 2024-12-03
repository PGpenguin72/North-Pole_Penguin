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

class PGpenguin72s_Channel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "企鵝的小小小窩介紹", description = "發出企鵝的小小小窩介紹")
    async def PGpenguin72s_Channel(self, interaction: discord.Interaction):
        if interaction.user.id == 609189792571457550:
            if interaction.channel.name == "企鵝的小小小窩":
                embed = discord.Embed(title="企鵝的小小小窩介紹:",
                              description="```fix\n-<［& 還是一個不嘈雜的小窩:D &］>-\n```\n> 1. 請隨時關閉你的麥克風 不要時常開啟。\n> 2. 常以文字代替語音，必要時可以開麥講話，說完要記得關閉。\n> 3. 不可截圖、錄音或錄影我的直播畫面，違者永遠拒絕加入本小窩。\n> 4. 直播畫面提供音樂串流資訊，電腦螢幕畫面，Discord聊天室，祈諾DC爆破工程，及鏡頭兩顆。\n> 5. 禁止在本小窩喧嘩，大叫，播放嘈雜的音效版，洗屏。\n> 6. 可點歌，想聽什麼歌我可以用 Apple Music，bilibili，Youtube等 播放，只要告訴我歌名，我就會播放喔。",
                              colour=choice(colors),
                              timestamp=datetime.now())

                embed.set_author(name="PG企鵝:",
                                 icon_url="https://images-ext-1.discordapp.net/external/p0nutJIzjcXy6w4lfgHh2SwL8C-EkXlfG3L91gOzubU/%3Fsize%3D512/https/cdn.discordapp.com/avatars/609189792571457550/a_8a23656ee0a43bc70fa1f652845e0e2c.gif")

                embed.add_field(name="小小小窩宗旨:",
                                value="``本小窩是給想要有人陪但卻想要個不嘈雜的環境的小夥伴用的``",
                                inline=False)
                embed.add_field(name="規範:",
                                value="> 1. 請隨時關閉你的麥克風 不要時常開啟。\n> 2. 常以文字代替語音，必要時可以開麥講話，說完要記得關閉。\n> 3. 不可截圖、錄音或錄影我的直播畫面，違者永遠拒絕加入本小窩。\n> 4. 直播畫面提供音樂串流資訊，電腦螢幕畫面，Discord聊天室，祈諾DC爆破工程，及鏡頭兩顆。\n> 5. 禁止在本小窩喧嘩，大叫，播放嘈雜的音效版，洗屏。\n> 6. 可點歌，想聽什麼歌我可以用 Apple Music，bilibili，Youtube等 播放，只要告訴我歌名，我就會播放喔。",
                                inline=False)
                embed.add_field(name="小小小窩的管理員: 一隻享受寧靜的溫暖版主PG企鵝",
                                value="~~**備註: 有問題可以問我，我會解決問題。如果你製造問題，我會先解決你。**~~",
                                inline=False)

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                                 icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
            else:
                await interaction.response.send_message("抱歉，你現在並不在企鵝的小小小窩裡面，不可以發出企鵝的小小小窩介紹。")

            await interaction.response.send_message(embed = embed)
        else:
            await interaction.response.send_message("抱歉，你並不是企鵝的小小小窩的管理員，不可以發出企鵝的小小小窩介紹。")

async def setup(bot: commands.Bot):
    await bot.add_cog(PGpenguin72s_Channel(bot))
