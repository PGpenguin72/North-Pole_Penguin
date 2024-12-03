import time
from random import choice
import discord.ext
from discord.ext import commands
from discord import app_commands
import discord


class choose(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "隨機分組", description = "隨機分組小程式" )
    @app_commands.describe(組別= "請輸入要分的組別名稱,並以「, 」隔開(最多26個組)(例如:企鵝隊, 螃蟹隊, 北極熊隊)。。", 成員 = "請輸入所有成員名單，並以「, 」隔開每個成員的名字(例如:小明, 小紅, 小黃)。")
    async def choose(self, interaction: discord.Interaction, 組別: str= None, 成員:str = None):
        if 組別 == None:
            await interaction.response.send_message("請輸入組別")
        elif 成員 == None:
            await interaction.response.send_message("請輸入成員")
        else:
            try:
                input_team = 組別.split(", ")
                input_players = 成員.split(', ')
                teams = {}

                function = 1 

                for t in input_team:
                    key = f'team_{function}'
                    teams[key] = t
                    function += 1

                T_function = function -1

                players = {}
                function = 1

                for p in input_players:
                    player = f'player_{function}'
                    players[player] = p
                    function += 1

                P_list = list(players.values())
                T_list = [[] for _ in range(T_function)]

                function -= 1
                function = 1

                while len(P_list) > 0:
                    for i in range(T_function):
                        if P_list:
                            player = choice(P_list)
                            T_list[i].append(player)
                            P_list.remove(player)
                for index, team_key in enumerate(teams.keys()):
                    if index < len(T_list):
                        await self.bot.get_channel(interaction.channel_id).send(f'{teams[team_key]} 成員: {", ".join(T_list[index])}')
                        time.sleep(0.3)
                await interaction.response.send_message("分組完成!")

            except Exception as e:
                await interaction.response.send_message(e)
                
async def setup(bot: commands.Bot):
    await bot.add_cog(choose(bot))  