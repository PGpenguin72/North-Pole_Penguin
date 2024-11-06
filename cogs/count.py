import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import commands

count_num = 1
channel_id = None
NowCH = None
last_member = None

class count(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="數數字", description="點此開始數數字吧(從一開始)")
    async def count(self, interaction: discord.Interaction):
        global channel_id,count_num, NowCH, last_member
        if NowCH == None:
            await interaction.response.send_message("開始數數字，我先來! 0")
            channel_id = interaction.channel_id
            NowCH = interaction.channel_id
            count_num = 1 
        else:
            await interaction.response.send_message(f"目前有頻道<#{NowCH}>正在玩遊戲，請稍後再嘗試。")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        global count_num, channel_id, NowCH, last_member
        member = message.author.id
        if NowCH == channel_id:
            if message.channel.id == channel_id :
                if member == last_member:
                        await message.add_reaction("❌")
                        channel = self.bot.get_channel(channel_id)
                        await channel.send("不，有人連續了，打指令重新開始吧!")
                        count_num = "一個用來停止的字串"
                        NowCH = None
                        last_member = None
                else:
                    if message.content.isdigit():
                        if message.content.isdigit() and int(message.content) == count_num:
                            await message.add_reaction("✅")
                            count_num += 1  
                            last_member = member
                        elif count_num == "一個用來停止的字串":
                            None 
                        else:
                            await message.add_reaction("❌")
                            channel = self.bot.get_channel(channel_id)
                            await channel.send("不，有人失誤了，打指令重新開始吧!")
                            count_num = "一個用來停止的字串"
                            NowCH = None
                            last_member = None

async def setup(bot: commands.Bot):
    await bot.add_cog(count(bot))
