import discord
from discord.ext import commands
import os 
from discord import app_commands
from datetime import datetime
import asyncio
import json
from typing import Optional
from discord.app_commands import Choice
import subprocess
import sys

intents = discord.Intents.all()

with open('main.json', 'r') as JSON_MAIN:
    KEY = json.load(JSON_MAIN)
key = KEY["key"]

# activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
## Type 可以改成 watching, listening, playing... 
activity = discord.Streaming(name="輸入/以開始使用", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#Status 可以改成 online , idle, dnd, invisible
bot = commands.Bot(command_prefix = "<@1269666706876530733> ", intents = intents,activity = activity, status=discord.Status.online)

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"已讀取 {extension} 。")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"取消讀取 {extension} 。")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"重新讀取 {extension} 。")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


class StatusModal(discord.ui.Modal, title="更改機器人狀態"):
    狀態 = discord.ui.TextInput(
        label="請輸入機器人狀態",
        placeholder="online, idle, dnd, invisible",
        required=True,
    )
    活動類型 = discord.ui.TextInput(
        label="請輸入活動類型",
        placeholder="playing, watching, listening, streaming",
        required=True,
    )
    活動內容 = discord.ui.TextInput(
        label="活動內容",
        placeholder="輸入活動名稱，例如 'Minecraft'",
        required=True,
    )

    async def on_submit(self, interaction: discord.Interaction):
        status_mapping = {
            "online": discord.Status.online,
            "idle": discord.Status.idle,
            "dnd": discord.Status.dnd,
            "invisible": discord.Status.invisible,
        }

        status = status_mapping.get(self.狀態.value.lower())
        if not status:
            await interaction.response.send_message("無效的狀態類型，請輸入 online, idle, dnd 或 invisible。", ephemeral=True)
            return

        activity = None
        if self.活動類型.value.lower() == "playing":
            activity = discord.Game(name=self.活動內容.value)
        elif self.活動類型.value.lower() == "watching":
            activity = discord.Activity(type=discord.ActivityType.watching, name=self.活動內容.value)
        elif self.活動類型.value.lower() == "listening":
            activity = discord.Activity(type=discord.ActivityType.listening, name=self.活動內容.value)
        elif self.活動類型.value.lower() == "streaming":
            activity = discord.Streaming(name=self.活動內容.value, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            await interaction.response.send_message("無效的活動類型，請輸入 playing, watching, listening 或 streaming。", ephemeral=True)
            return

        await bot.change_presence(status=status, activity=activity)

        embed = discord.Embed(
            title="機器人狀態已更新",
            description=f"**狀態:** {self.狀態.value}\n**活動:** {self.活動類型.value} - {self.活動內容.value}",
            colour=0x00ff00,
            timestamp=datetime.now()
        )
        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256") 
        await interaction.response.send_message(embed=embed)
        channel_id = 1302497000758972497
        channel = bot.get_channel(channel_id)
        await channel.send(embed=embed)

@bot.tree.command(name = "開發者選項", description = "北極企鵝的開發者專用的功能")
@app_commands.describe(動作 = "請選擇你要執行的動作", 選擇更新的模組 = "(你可以選擇你要更新的Cog。)")
@app_commands.choices(動作=[
        Choice(name="重新啟動", value="restart"),
        Choice(name="關機", value="stop"),
        Choice(name="更改機器人狀態", value="status"),
        Choice(name="重新載入Cog", value="reload"),
        Choice(name="取消載入Cog", value="unload"),
        Choice(name="載入Cog", value="load")
    ]
    )
@app_commands.choices(選擇更新的模組=[
        Choice(name="全部Cog", value="all"),
        Choice(name="設定歡迎消息", value="add_welcome"),
        Choice(name="數數字", value="count"),
        Choice(name="伺服器設定", value="Guild_setting"),
        Choice(name="幫助", value="help"),
        Choice(name="介紹", value="introduce"),
        Choice(name="迷因", value="meme"),
        Choice(name="Discord訊息連結自動攝取", value="message"),
        Choice(name="音樂建議", value="music_suggest"),
        Choice(name="企鵝的小小小窩介紹", value="PGpenguin72's_Channel"),
        Choice(name="剪刀石頭布", value="PSR"),
        Choice(name="自動回覆訊息", value="replies"),
        Choice(name="大聲說", value="message"),
        Choice(name="溫暖領航團的規則", value="rules"),
        Choice(name="簽到", value="sign"),
        Choice(name="建議", value="suggest"),
        Choice(name="服務條款", value="TOS"),
        Choice(name="想玩機器人", value="trick"),
        Choice(name="更新公告", value="update"),
        Choice(name="用戶設定", value="User_setting"),
        Choice(name="語音頻道使用者設定", value="VoiceStateTracker"),
        Choice(name="歡迎消息", value="welcome"),
        Choice(name="匿名說", value="anonymous")
    ]
    )
async def developer(interaction: discord.Interaction, 動作: str, 選擇更新的模組: Optional[str]):
    if interaction.user.id in [609189792571457550, 368643370756866048]:
        channel_id = 1302497000758972497
        channel = bot.get_channel(channel_id)

        if 動作 == "restart":
            embed = discord.Embed(
                title="機器人重新啟動中",
                description=f"執行者: {interaction.user.global_name}",
                colour=0xd8d222,
                timestamp=datetime.now()
            )
            embed.set_footer(
                text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256"
            )
            await interaction.response.send_message(embed=embed)
            await channel.send(embed=embed)
            
            os.system('cls')
            subprocess.Popen([sys.executable] + sys.argv)
            await bot.close()
            
        elif 動作 == "stop":
            embed = discord.Embed(title="機器人關機中",
                    description=f"執行者: {interaction.user.global_name}",
                    timestamp=datetime.now())

            embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                             icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")

            await interaction.response.send_message(embed=embed)
            await channel.send(embed=embed)
            await bot.close()

        elif 動作 == "reload":
            if 選擇更新的模組 == "all":
                failed_cogs = []
                embed = discord.Embed(title="所有 Cog 皆已嘗試重新讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                for filename in os.listdir("./cogs"):
                    if filename.endswith(".py"):
                        try:
                            await bot.reload_extension(f"cogs.{filename[:-3]}")
                            embed.add_field(name=f"{filename[:-3]}",
                                value=f"重新讀取成功!",
                                inline=False)
                             
                        except Exception as e:
                            embed.add_field(name="此Cog 重新讀取失敗: ",
                                value=f"{e}",
                                inline=False)
                await interaction.response.send_message(embed=embed)

            else:
                embed = discord.Embed(title=f"Cog {選擇更新的模組} 已嘗試重新讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                try:
                    await bot.reload_extension(f"cogs.{選擇更新的模組}")
                    embed.add_field(name=f"{選擇更新的模組}",
                                    value=f"重新讀取成功!",
                                    inline=False)
                except Exception as e:
                            embed.add_field(name="此Cog 重新讀取失敗: ",
                                value=f"{e}",
                                inline=False)
                await interaction.response.send_message(embed=embed)
                
            embed = discord.Embed(title=f"Cog {選擇更新的模組} 已重新讀取",
                      description=f"執行者: {interaction.user.global_name}",
                      colour=0xd8d222,
                      timestamp=datetime.now())

            embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                 icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
            await channel.send(embed=embed)

        elif 動作 == "load":
            if 選擇更新的模組 == "all":
                failed_cogs = []
                embed = discord.Embed(title="所有 Cog 皆已嘗試讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                for filename in os.listdir("./cogs"):
                    if filename.endswith(".py"):
                        try:
                            await bot.load_extension(f"cogs.{filename[:-3]}")
                            embed.add_field(name=f"{filename[:-3]}",
                                value=f"讀取成功!",
                                inline=False)
                            
                        except Exception as e:
                            embed.add_field(name="此Cog 讀取失敗: ",
                                value=f"{e}",
                                inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(title=f"Cog {選擇更新的模組} 已嘗試讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                try:
                    await bot.load_extension(f"cogs.{選擇更新的模組}")
                    embed.add_field(name=f"{選擇更新的模組}",
                                    value=f"讀取成功!",
                                    inline=False)
                except Exception as e:
                            embed.add_field(name="此Cog 讀取失敗: ",
                                value=f"{e}",
                                inline=False)
                await interaction.response.send_message(embed=embed)
                
            embed = discord.Embed(title=f"Cog {選擇更新的模組} 已讀取",
                      description=f"執行者: {interaction.user.global_name}",
                      colour=0xd8d222,
                      timestamp=datetime.now())

            embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                 icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
            await channel.send(embed=embed)

        elif 動作 == "unload":
            if 選擇更新的模組 == "all":
                failed_cogs = []
                embed = discord.Embed(title="所有 Cog 皆已嘗試取消讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                for filename in os.listdir("./cogs"):
                    if filename.endswith(".py"):
                        try:
                            await bot.unload_extension(f"cogs.{filename[:-3]}")
                            embed.add_field(name=f"{filename[:-3]}",
                                value=f"取消讀取成功!",
                                inline=False)
                            
                        except Exception as e:
                            embed.add_field(name="此Cog 取消讀取失敗: ",
                                value=f"{e}",
                                inline=False)
            else:
                embed = discord.Embed(title=f"Cog {選擇更新的模組} 已嘗試取消讀取",
                    description=f"執行者: {interaction.user.global_name}",
                    colour=0xd8d222,
                    timestamp=datetime.now())

                embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                    icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
                try:
                    await bot.unload_extension(f"cogs.{選擇更新的模組}")
                    embed.add_field(name=f"{選擇更新的模組}",
                                    value=f"取消讀取成功!",
                                    inline=False)
                except Exception as e:
                            embed.add_field(name="此Cog 取消讀取失敗: ",
                                value=f"{e}",
                                inline=False)
            await interaction.response.send_message(embed=embed)
                
            embed = discord.Embed(title=f"Cog {選擇更新的模組} 已取消讀取",
                      description=f"執行者: {interaction.user.global_name}",
                      colour=0xd8d222,
                      timestamp=datetime.now())

            embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                 icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
            await channel.send(embed=embed)
        
        elif 動作 == "status":
            await interaction.response.send_modal(StatusModal())
        else:
            await interaction.response.send_message("抱歉，你使用了無法使用的功能。")
    else:
        await interaction.response.send_message("抱歉，你並不是機器人開發者，不可以設定機器人開發者設定喔!")    

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    regular_commands = list(bot.commands)
    print(f"$$$目前登錄身分: {bot.user}")
    print(f"載入了 {len(slash)} 個斜線指令。")
    print(f"\n載入了 {len(regular_commands)} 個一般指令:")
    for cmd in regular_commands:
        print(f"- 一般指令: {bot.command_prefix}{cmd.name}")
        
    print(f"\n總共載入了 {len(slash) + len(regular_commands)} 個指令")
    print("Bot is ready!")
    embed = discord.Embed(title="北極企鵝上線了!",
                      colour=0x44ff00,
                      timestamp=datetime.now())

    embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
    channel_id = 1302497000758972497
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(key)


if __name__ == "__main__":
    asyncio.run(main())

