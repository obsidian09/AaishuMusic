from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def stats(_, message):
    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗟ɪᴠᴇ 𝗦ᴛᴀᴛꜱ**

┏━━━━━━━━━━━━━━━┓
┃ 🤖 ʙᴏᴛ : ᴏɴʟɪɴᴇ
┃ 🎧 ᴍᴏᴅᴇ : ᴘʀᴇᴍɪᴜᴍ
┃ ⚡ ᴠᴇʀꜱɪᴏɴ : 1.0.0
┃ 🌙 ᴛʜᴇᴍᴇ : ʙʟᴀᴄᴋ ᴀᴜʀᴀ
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 𝗦ᴜᴘᴘᴏʀᴛ", url="https://t.me/Aaishu_bots")],
        [InlineKeyboardButton("📢 𝗔ᴀɪsʜᴜ 𝗨ᴘᴅᴀᴛᴇꜱ", url="https://t.me/Aaishu_Updates")]
    ])

    await message.reply_text(text, reply_markup=buttons)

def register(app):
    app.add_handler(MessageHandler(stats, filters.command("stats")), group=8)

