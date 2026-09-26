from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def settings(_, message):
    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗦ᴇᴛᴛɪɴɢꜱ 𝗣ᴀɴᴇʟ**

┏━━━━━━━━━━━━━━━┓
┃ 🔊 Volume : 100%
┃ 🎧 Mode : Premium
┃ 🎵 Quality : High
┃ 🌙 Theme : Black Aura
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔈 50%", callback_data="vol50"),
            InlineKeyboardButton("🔊 100%", callback_data="vol100")
        ],
        [
            InlineKeyboardButton("🎵 𝗛ɪɢʜ", callback_data="high"),
            InlineKeyboardButton("⚡ 𝗨ʟᴛʀᴀ", callback_data="ultra")
        ],
        [
            InlineKeyboardButton("❌ 𝗖ʟᴏsᴇ", callback_data="close")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

def register(app):
    app.add_handler(
        MessageHandler(settings, filters.command("settings")),
        group=7
    )

