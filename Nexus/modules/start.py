from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID, SUPPORT
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from Nexus import Nexus as app


START_TEXT = """
ʜᴇʟʟᴏ {} 
\n⋆─────────────────────⋆
Wᴇʟᴄᴏᴍᴇ \n⋆─────────────────────⋆
Iᴍᴍᴇʀsᴇ ʏᴏᴜʀsᴇʟғ ɪɴ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ\n⋆─────────────────────⋆
Dɪsᴄᴏᴠᴇʀ, ᴘʟᴀʏ, ᴀɴᴅ ᴇɴJᴏʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴛᴜɴᴇs ʀɪɢʜᴛ ʜᴇʀᴇ\n⋆─────────────────────⋆
Sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ sᴏɴɢ ᴏʀ ᴀʀᴛɪsᴛ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴇʟᴏᴅʏ ʙᴇɢɪɴ. \n⋆─────────────────────⋆
Usᴇ Help ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs. 🎶
"""
# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("⦿ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ⦿", callback_data="admin_data")
        ],
        [
            InlineKeyboardButton("⦿ɢʀᴏᴜᴘ⦿", url="https://t.me/{SUPPORT}"),
            InlineKeyboardButton("⦿ᴏᴡɴᴇʀ⦿", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://graph.org/file/5690109178f081adf464d.mp4",
        caption=START_TEXT,
        reply_markup=reply_markup
    )
