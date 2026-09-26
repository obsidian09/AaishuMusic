from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

async def owner(_, message):
    if message.from_user.id != OWNER_ID:
        return

    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗢ᴡɴᴇʀ 𝗣ᴀɴᴇʟ**

┏━━━━━━━━━━━━━━━┓
┃ 👑 Premium Access
┃ 📢 Broadcast
┃ ⚙ Manage Bot
┃ 📊 Live Stats
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats"),
            InlineKeyboardButton("📢 Broadcast", callback_data="bc")
        ],
        [
            InlineKeyboardButton("⚙ Settings", callback_data="settings")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

def register(app):
    app.add_handler(
        MessageHandler(owner, filters.command("owner")),
        group=15
    )
