from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def help_cmd(_, message):
    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs**

┏━━━━━━━━━━━━━━━┓
┃ 🎶 /play
┃ ⏸ /pause
┃ ⏭ /skip
┃ 📜 /queue
┃ ⚡ /ping
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 𝗣ʟᴀʏ", callback_data="play_help"),
            InlineKeyboardButton("⚙️ 𝗔ᴅᴍɪɴ", callback_data="admin_help")
        ],
        [
            InlineKeyboardButton("💬 𝗦ᴜᴘᴘᴏʀᴛ", url="https://t.me/Aaishu_bots")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

def register(app):
    app.add_handler(MessageHandler(help_cmd, filters.command("help")), group=3)

