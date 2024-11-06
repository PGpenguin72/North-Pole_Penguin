from discord.ext import commands

class Replies(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()
        
        if any(word in content for word in ["goodnight", "晚安", "晚昂", "晚安 瑪卡巴卡", "早唞"]):
            await message.reply(f"<@{message.author.id}> 晚安呀!")
            
        
        if any(word in content for word in ["goodmorning", "早安", "早昂", "早上好", "早阿", "早啊"]):
            await message.reply(f"<@{message.author.id}> 早安呀!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Replies(bot))