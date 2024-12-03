import discord
from discord import app_commands
from discord.ext import commands
import json
from datetime import datetime, timedelta

def reload():
    with open(file_path, 'r', encoding='utf-8') as JSON_sign:
        data = json.load(JSON_sign)
    return data

file_path = './json/sign.json'

class sign(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="簽到", description="從今天開始每天都簽到吧!")
    async def sign(self, interaction: discord.Interaction):
        user = str(interaction.user.id)
        day = datetime.now().strftime("%Y/%m/%d")
        user_get = reload()

        if user in user_get:
            nowday = user_get[user]['day']
            count = user_get[user]['count']
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y/%m/%d")
            if nowday == day:
                await interaction.response.send_message("你今日已簽到了喔!，下次簽到時間為明天。")
            elif nowday == yesterday:
                user_get[user]['day'] = day 
                user_get[user]['count'] = count + 1 
                json_file = {
                    user : {
                        "day" : day,
                        "count" : count +1
                    }
                }
                user_get.update(json_file)
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(user_get, file, ensure_ascii=False, indent=4)
                await interaction.response.send_message(f"簽到成功! 目前已成功連續簽到 {count +1} 天。")
            else:
                json_file = {
                    user : {
                        "day" : day,
                        "count" : 1
                    }
                }
                user_get.update(json_file)
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(user_get, file, ensure_ascii=False, indent=4)
                await interaction.response.send_message(f"簽到成功! 因為你昨天沒有簽到，所以簽到連續數重置。目前已成功簽到 1 天。")

        else:
            json_file = {
                user : {
                    "day" : day,
                    "count" : 1
                }
            }
            user_get.update(json_file)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(user_get, file, ensure_ascii=False, indent=4)
            await interaction.response.send_message(f"簽到成功! 目前已成功簽到 1 天。")



async def setup(bot: commands.Bot):
    await bot.add_cog(sign(bot))