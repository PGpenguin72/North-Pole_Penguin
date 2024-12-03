import discord
from discord import app_commands
from discord.ext import commands
import json

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

group_id = None
group_name = None

class Create(discord.ui.Modal, title = "設定歡迎消息"):
    one = discord.ui.TextInput(label = "請輸入用來發送歡迎消息的頻道ID:", placeholder = "開啟設定中的「開發者模式」，右鍵頻道名稱選「複製頻道ID」。", max_length = 19)
    two = discord.ui.TextInput(label = "輸入大標題歡迎消息。", default = "歡迎加入 {guild} ，你是第 {count} 位用戶")
    three = discord.ui.TextInput(label = "請輸入稱呼之用戶", default = "用戶 {user} 你好!")
    four = discord.ui.TextInput(label = "請輸入當用戶加入時傳送之圖片連結(限制一張)。", required = False )
    five = discord.ui.TextInput(label = "請輸入歡迎消息。",placeholder= "不要太長，要不然機器人會爆掉:D", style = discord.TextStyle.paragraph, max_length = 500)
    async def on_submit(self, interaction: discord.Interaction):
        welcome_msg = {
            f"{group_id}" : {
                "GROUPname": f"{group_name}", 
                "CH_welcome": f"{self.one.value}",
                "welcome_MSG":{
                    "title": f"{self.three.value}",
                    "description": f"{self.five.value}",
                    "author":{
                        "name": f"{self.two.value}"
                    },
                    "images": f"{self.four.value}"
                }
            }
        }

        file_path = './json/welcome.json'

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data.update(welcome_msg)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
       
        await interaction.response.send_message("恭喜你成功設定了歡迎消息!",ephemeral=True)

class add_welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "設定歡迎消息", description = "想要在你的群組裡面設定歡迎消息嗎? 若果你擁有管理員權限，你就可以設定喔!(註:若伺服器原本存在歡迎消息將會被覆蓋)")
    async def add_welcome(self, interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            global group_id, group_name
            group_id = interaction.guild.id
            group_name = interaction.guild.name
            await interaction.response.send_modal(Create())
                    
        else:
            await interaction.response.send_message("抱歉，你並不是管理員，不可以設定歡迎消息喔!", ephemeral=True)    

async def setup(bot: commands.Bot):
    await bot.add_cog(add_welcome(bot))