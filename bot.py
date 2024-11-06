import discord
from discord.ext import commands
import os 
from datetime import datetime
import asyncio
import json

intents = discord.Intents.all()

with open('main.json', 'r') as JSON_MAIN:
    KEY = json.load(JSON_MAIN)
key = KEY["key"]

# activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
## Type 可以改成 watching, listening, playing... 
activity = discord.Streaming(name="輸入/以開始使用", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#Status 可以改成 online , idle, dnd, invisible
bot = commands.Bot(command_prefix = "<@1269666706876530733> ", intents = intents,activity = activity, status=discord.Status.online)

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"已讀取 {extension} 。")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"取消讀取 {extension} 。")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"重新讀取 {extension} 。")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    regular_commands = list(bot.commands)
    print(f"$$$目前登錄身分: {bot.user}")
    print(f"載入了 {len(slash)} 個斜線指令。")
    print(f"\n載入了 {len(regular_commands)} 個一般指令:")
    for cmd in regular_commands:
        print(f"- 一般指令: {bot.command_prefix}{cmd.name}")
        
    print(f"\n總共載入了 {len(slash) + len(regular_commands)} 個指令")
    print("Bot is ready!")
    embed = discord.Embed(title="北極企鵝上線了!",
                      colour=0x44ff00,
                      timestamp=datetime.now())

    embed.set_footer(text="北極企鵝 || Created by. PGpenguin72 and IceBearowob",icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256")
    channel_id = 1302497000758972497
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(key)


if __name__ == "__main__":
    asyncio.run(main())

