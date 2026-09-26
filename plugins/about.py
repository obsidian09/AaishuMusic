from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def about(_, message):
    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗟ᴜxᴜʀʏ 𝗕ʟᴀᴄᴋ 𝗔ᴜʀᴀ**

┏━━━━━━━━━━━━━━━┓
┃ 👑 ᴏᴡɴᴇʀ : @hey_mohit
┃ ⚡ ᴠᴇʀsɪᴏɴ : 1.0.0
┃ 🎧 ᴇɴɢɪɴᴇ : Pyrogram
┃ 🟢 sᴛᴀᴛᴜs : Online
┗━━━━━━━━━━━━━━━┛

**「 ᴄʀᴀғᴛᴇᴅ ᴡɪᴛʜ 🖤 」**

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👑 𝗢ᴡɴᴇʀ", url="https://t.me/hey_mohit"),
            InlineKeyboardButton("💬 𝗦ᴜᴘᴘᴏʀᴛ", url="https://t.me/Aaishu_bots")
        ],
        [
            InlineKeyboardButton("📢 𝗔ᴀɪsʜᴜ 𝗨ᴘᴅᴀᴛᴇꜱ", url="https://t.me/Aaishu_Updates")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

def register(app):
    app.add_handler(
        MessageHandler(about, filters.command("about")),
        group=6
    )

