import discord
from discord import app_commands
from discord.ext import commands
import json
import asyncio

# 全域鎖，用於避免多執行緒操作 JSON 時發生競爭
lock = asyncio.Lock()

file_path = './json/count.json'

async def reload():
    """重新載入 JSON 檔案資料"""
    async with lock:
        try:
            with open(file_path, 'r', encoding='utf-8') as JSON_count:
                return json.load(JSON_count)
        except FileNotFoundError:
            # 若檔案不存在，建立一個空 JSON
            with open(file_path, 'w', encoding='utf-8') as JSON_count:
                json.dump({}, JSON_count)
            return {}

class count(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="數數字", description="點此開始數數字吧(從一開始)")
    async def count(self, interaction: discord.Interaction):
        CH_id = interaction.channel_id
        data = await reload()
        
        # 初始化最高分數
        if "The_Higher_Score" not in data:
            data["The_Higher_Score"] = "0"
            async with lock:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

        # 檢查頻道是否已啟用遊戲
        if str(CH_id) in data:
            count_number = int(data[str(CH_id)]['count_num'])
            await interaction.response.send_message(f"已在此頻道開啟遊戲，目前已經數到了 {count_number-1} ，請繼續數數。")
        else:
            # 初始化頻道遊戲數據
            await interaction.response.send_message("開始數數字，我先來! 0")
            count_number = 1
            JSONdata = {
                f"{CH_id}": {
                    "count_num": str(count_number),
                    "last_counter": "null"
                }
            }
            
            data.update(JSONdata)
            async with lock:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        data = await reload()
        Higher_score = int(data.get("The_Higher_Score", 0))
        CH_Get = data.get(str(message.channel.id), None)
        channel_id = message.channel.id
        channel = self.bot.get_channel(channel_id)

        # 檢查頻道是否啟用遊戲
        if CH_Get is None:
            return

        last_Counter = CH_Get["last_counter"]
        Now_Count = int(CH_Get["count_num"])
        member = message.author.id

        if message.content.isdigit():
            if last_Counter == str(member):
                # 連續數數導致失敗
                await message.add_reaction("❌")
                await channel.send(f"不，有人連續了，打指令重新開始吧! \n目前全北極最高紀錄: {Higher_score}")

                # 刪除頻道資料
                del data[str(channel_id)]
                async with lock:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

            elif int(message.content) == Now_Count:
                # 正確數字
                if Now_Count == 5272:
                    await channel.send(
                        f"恭喜 <@{member}> 數到了第272個數字，觸發隱藏獎勵!!!請將本截圖提供給 <@609189792571457550> 並提供訊息鏈結，來兌換一個精美獎品喔:D"
                    )
                    print(f"用戶{message.author.display_name}觸發了隱藏獎勵!")

                await message.add_reaction("✅")
                Now_Count += 1

                # 更新 JSON 資料
                data[str(channel_id)] = {
                    "count_num": str(Now_Count),
                    "last_counter": str(member)
                }

                # 更新最高分數
                if Now_Count > Higher_score:
                    data["The_Higher_Score"] = str(Now_Count - 1)

                async with lock:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

            else:
                # 錯誤數字
                await message.add_reaction("❌")
                await channel.send(f"不，有人失誤了，打指令重新開始吧! \n目前全北極最高紀錄: {Higher_score}")

                # 刪除頻道資料
                del data[str(channel_id)]
                async with lock:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

async def setup(bot: commands.Bot):
    await bot.add_cog(count(bot))
