import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from random import choice

class update(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "更新公告", description = "發出最新一期更新公告(1.1.1)。")
    async def update(self, interaction: discord.Interaction):
        embed = discord.Embed(title="北極企鵝版本1.1.1",
                              description="新增以下功能:",
                              colour=0x07dfd0,
                              timestamp=datetime.now())

        embed.set_author(name="###北極企鵝更新公告 ###")

        embed.add_field(name="/音樂新增建議 [內容]",
                        value="為未來的播放音樂功能提供之音樂的建議。",
                        inline=False)
        embed.add_field(name="#/迷因 [選項]",
                        value="新增一條迷因。",
                        inline=False)

        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",
                         icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256") 
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(update(bot))