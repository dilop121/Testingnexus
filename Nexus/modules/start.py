from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID, SUPPORT
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from Nexus import Nexus as app

start_txt = """
IAM NOOB 
"""


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("🎩ADD ME BABY🪄", callback_data="admin_data")
        ],
        [
            InlineKeyboardButton("🆘𝖲𝖴𝖯𝖱𝖮𝖳🆘", url="https://t.me/{SUPPORT}"),
            InlineKeyboardButton("🧑‍💻𝖣𝖤𝖵🧑‍💻", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://telegra.ph/file/630e51ee72baec5dc9012.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
