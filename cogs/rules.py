import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from random import choice
from discord.app_commands import Choice
from typing import Optional

colors = [
    0xc97e4d, 0x8cbf5e, 0x6aa2d2, 0xe6a157, 0xb37ca1, 0x59a5a2, 0xde8579, 
    0x9289b8, 0xa2b872, 0xcb9763, 0x798ea4, 0xbf677a, 0x7aa861, 0x9a7a5c, 
    0x669f99, 0xb2a35c, 0xd17769, 0x7189c0, 0x9c8b77, 0x848f73
]

class Rules(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="規則", description="點此發送一次溫暖領航團的規則吧!")
    @app_commands.describe(規則第〇條="輸入規則的條數(羅馬數字)")
    @app_commands.choices(規則第〇條=[
        Choice(name="1", value="1"),
        Choice(name="2", value="2"),
        Choice(name="3", value="3"),
        Choice(name="4", value="4"),
        Choice(name="5", value="5"),
        Choice(name="6", value="6"),
        Choice(name="7", value="7"),
        Choice(name="8", value="8"),
        Choice(name="9", value="9"),
    ])
    async def rules(self, interaction: discord.Interaction, 規則第〇條: Optional[str] = None):
        rule_texts = [
            "1. 打造友善的環境是所有人的責任。請尊重他人。",
            "2. 確保所有人都能感到安心。我們不允許任何形式的霸凌行為，也無法容忍有關種族、宗教、文化、性傾向、性別或個性的嘲笑留言。",
            "3. 雖然開誠布公的討論有助於社群成長、茁壯，但也要注意到敏感議題和個人隱私。",
            "4. 請多多為社團貢獻實用內容。我們不允許垃圾訊息、不相關的連結與推銷。",
            "5. 我們重視所有人的言論自由，可以適度的發洩情緒，但前提是不影響其他小夥伴。",
            "6. 我們會注意各位小夥伴的言論，不希望任何人的負面情緒影響到想開心遊玩的小夥伴們。",
            "7. 如果有負面情緒、或是想要超派爭吵，可以在 #小樹洞 處理，裡面的發言不受團規限制。",
            "8. 若違反以上規定，我們會先以「拔除身份組」跟「禁言」警告⚠️，禁言天數會以管理員討論後視情況而懲處。違反超過三次者會請小夥伴先離開大家(DC停權)。",
            "9. 請勿違反我國(中華民國)之律法，違者將處飛機票一張，永不加入。"
        ]
        
        en_rule_texts = [
            "Creating a friendly environment is everyone’s responsibility. Please respect others.",
            "Ensure everyone feels safe. We do not allow any form of bullying, nor do we tolerate derogatory comments about race, religion, culture, sexual orientation, gender, or personality.",
            "While open discussions are beneficial for community growth, be mindful of sensitive topics and personal privacy.",
            "Please contribute useful content to the community. Spam, irrelevant links, and promotions are not allowed.",
            "We value everyone’s freedom of expression and understand the need to vent emotions occasionally, but please do so without affecting others.",
            "We monitor everyone’s speech and aim to ensure that negative emotions do not impact members who wish to have fun.",
            "If you need to vent or have heated discussions, please use #venting-space, where messages are not subject to regular rules.",
            "If any of the above rules are violated, we will issue a warning by removing roles or imposing a mute⚠️. The mute duration will be determined by the admins based on the situation. Violating rules more than three times may result in a temporary suspension from the community (Discord ban).",
            "Please do not violate the laws of our country (Republic of China). Those who do so will be permanently banned from rejoining."
        ]
        
        embed = discord.Embed(title="領航團團規",
                              description="The rule of our group.",
                              colour=choice(colors),
                              timestamp=datetime.now())

        if 規則第〇條:
            index = int(規則第〇條) - 1  # Convert to 0-based index
            embed.add_field(name=rule_texts[index], value=en_rule_texts[index], inline=False)
        else:
            for i in range(len(rule_texts)):
                embed.add_field(name=rule_texts[i], value=en_rule_texts[i], inline=False)

        embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Rules(bot))  