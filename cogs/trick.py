import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import json

def reload():
    with open('./json/entered_password.json', 'r', encoding='utf-8') as file:
        user_check = json.load(file)
    return user_check

class trick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="想玩機器人", description="如果你想玩這個機器人，你可以使用這個指令。")
    @app_commands.describe(奇怪的選擇咚咚="這個好像要解鎖一個東西才能成功選擇，如果沒有解鎖還是無效。")
    @app_commands.choices(
        奇怪的選擇咚咚=[
            Choice(name="不知名的奇怪選項", value=72)  
        ]
    )
    async def trick(self, interaction: discord.Interaction, 奇怪的選擇咚咚: int = None):
        print(f"選擇的值: {奇怪的選擇咚咚}")

        user_check = reload()
        if str(interaction.user.id) in user_check:
            if 奇怪的選擇咚咚 == 72:
                await interaction.response.send_message("https://discord.gg/WGhJz7XQNH", ephemeral=True)
            else:
                await interaction.response.send_message("# 叫你亂玩的喔(? 不要隨便玩我好嗎:( 給你一個小懲罰 \n ## (註:開個小玩笑 別走心阿:D) \n https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif", ephemeral=True)
        else:
            await interaction.response.send_message("# 叫你亂玩的喔(? 不要隨便玩我好嗎:( 給你一個小懲罰 \n ## (註:開個小玩笑 別走心阿:D) \n https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(trick(bot))