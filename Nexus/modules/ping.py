from pyrogram import Client, filters
from pyrogram.types import Message
from Nexus import Nexus


@Nexus.on_message(filters.command("alive"))
async def alive_command_handler(client: Client, message: Message):
    await message.reply("Yes, I'm alive!")
