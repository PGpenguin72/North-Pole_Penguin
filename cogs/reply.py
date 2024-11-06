import discord
from discord.ext import commands
from datetime import datetime
import json
import re
import io
from random import choice

class reply(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self,message):
        match = re.match(r'^https://discord\.com/channels/(\d+)/(\d+)/(\d+)$', message.content)
        if match:
            guild_id, channel_id, message_id = map(int, match.groups())

            channel = self.bot.get_channel(channel_id)
            if channel is None:
                return

            # if guild_id != message.guild.id:
            #     return

            mentioned = await channel.fetch_message(message_id)
            reply_content = f"{mentioned.author.mention} {discord.utils.format_dt(mentioned.created_at, 'F')}, 在 {mentioned.channel.mention}, 在 {mentioned.guild.name}"

            files = []
            has_video = False
            image_file = None

            for attachment in mentioned.attachments:
                file_data = await attachment.read()
                file = discord.File(io.BytesIO(file_data), filename=attachment.filename)

                if attachment.filename.lower().endswith(('.mp4', '.mov', '.avi', '.webm')):
                    has_video = True
                    files.append(file)
                elif not image_file and attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    image_file = file
                else:
                    files.append(file)

            if has_video:
                full_content = f"{reply_content}\n\n{mentioned.content}" if mentioned.content else reply_content
                await message.reply(
                    content=full_content,
                    files=files,
                    allowed_mentions=discord.AllowedMentions.none(),
                    silent=True
                )
            else:
                embeds = []
                if mentioned.content or not mentioned.embeds:
                    main_embed = discord.Embed(
                        description=mentioned.content if mentioned.content else "",
                        color=mentioned.author.color,
                        timestamp=mentioned.created_at
                    )
                    main_embed.set_author(name=mentioned.author.name, icon_url=mentioned.author.display_avatar.url)
                    main_embed.set_footer(
            text="北極企鵝 || Created by. PGpenguin72 and IceBearowob", 
            icon_url="https://cdn.discordapp.com/app-icons/1269666706876530733/e185878d40272a50720334434811b71a.png?size=256"
        )
                    if image_file:
                        files.append(image_file)
                        main_embed.set_image(url=f"attachment://{image_file.filename}")

                    embeds.append(main_embed)

                embeds.extend(mentioned.embeds)

                await message.reply(
                    content=reply_content,
                    embeds=embeds,
                    files=files,
                    allowed_mentions=discord.AllowedMentions.none(),
                    silent=True
                )

        await self.bot.process_commands(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(reply(bot))