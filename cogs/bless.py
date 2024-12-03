import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from random import choice
from discord.app_commands import Choice
from typing import Optional
import json

def reload():
    with open("./json/bless.json", "r", encoding='utf-8') as JSON_file:
        recorder = json.load(JSON_file)
    return recorder

class bless(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="波雞祝福者設置", description="如果你有在10/26日祝福波雞生日快樂，請使用這個指令來註冊你的訊息")
    @app_commands.describe(表單編號="請輸入你的祝福影片或音檔的表單編號", 凌晨訊息鏈結="請輸入當天有發送祝福的訊息連結")
    async def bless(self, interaction: discord.Interaction, 表單編號: str, 凌晨訊息鏈結: str):
        if interaction.guild_id == 1297231296468090911:
            if 表單編號 == None or 凌晨訊息鏈結 == None:
                await interaction.response.send_message("你有空格沒有輸入，請確認是否有輸入完整內容。 (錯誤代碼: blank form)")
            elif 表單編號 == "Null" or 凌晨訊息鏈結 == "Null":
                await interaction.response.send_message("你有空格沒有輸入，請確認是否有輸入完整內容。 (錯誤代碼: blank form)") 
            else:
                user_id = str(interaction.user.id)
                user_name = interaction.user.name
                settings = reload()

                if user_id not in settings:
                    settings[user_id] = {}

                settings[user_id]["name"] = user_name
                settings[user_id]["first"] = 表單編號
                settings[user_id]["second"] = 凌晨訊息鏈結
                with open('./json/bless.json', 'w', encoding='utf-8') as file:
                    json.dump(settings, file, ensure_ascii=False, indent=4)

                await interaction.response.send_message(f"已成功註冊你的個人訊息，若要更改請再次輸入指令!")
        else:
            await interaction.response.send_message("你目前沒辦法使用這個指令，請聯繫開發者取得更詳細資訊。 (錯誤代碼: not in PSguild.)")

async def setup(bot: commands.Bot):
    await bot.add_cog(bless(bot))
