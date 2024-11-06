import discord
from discord.ext import commands

class xiaoyujiang_joing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        channel_id = after.channel.id
        channel = self.bot.get_channel(channel_id)
        if before.channel is None and after.channel:
            if member.id == 613007318258548766:
                await channel.send("<@613007318258548766>唱歌!!!")

async def setup(bot: commands.Bot):
    await bot.add_cog(xiaoyujiang_joing(bot))