from discord.ext import commands
import json
import random 

def reload():
    with open('./json/user_setting.json', 'r', encoding='utf-8') as JSON_file:
        setting = json.load(JSON_file)
    return setting

class Replies(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()
        
        setting = reload()
        if setting[str(message.author.id)].get("replies") is True:
            if "<@1269666706876530733>" in content:

                if any(word in content for word in ["goodnight", "晚安", "晚昂", "晚安 瑪卡巴卡", "早唞"]):
                    await message.reply(f"<@{message.author.id}> 晚安呀!")

                if any(word in content for word in ["goodmorning", "早安", "早昂", "早上好", "早阿", "早啊"]):
                    await message.reply(f"<@{message.author.id}> 早安呀!")

                if any(word in content for word in ["安安"]):
                    await message.reply(f"哈囉阿! <@{message.author.id}> !")
                if any(word in content for word in ["好可愛"]):
                    await message.reply(f"謝謝 <@{message.author.id}> ~ 你也是喔.w.")
                if any(word in content for word in ["喵"]):
                    await message.reply(f"# 汪")

            number = random.randint(1, 100000)
            if number == 59472:
                await message.reply(f"恭喜 {message.author.display_name}! 你發送訊息時觸發了隱藏獎勵!!!請將本截圖提供給 <@609189792571457550> 並提供訊息鏈結，來兌換一個精美獎品喔:D")

async def setup(bot: commands.Bot):
    await bot.add_cog(Replies(bot))