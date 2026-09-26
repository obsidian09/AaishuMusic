from pyrogram import filters
from pyrogram.handlers import MessageHandler
from config import OWNER_ID

async def broadcast(_, message):
    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "✦ **ᴜsᴇ →** `/broadcast your message`"
        )

    msg = message.text.split(None, 1)[1]

    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗕ʀᴏᴀᴅᴄᴀsᴛ 𝗣ʀᴇᴠɪᴇᴡ**

━━━━━━━━━━━━━━━
{msg}
━━━━━━━━━━━━━━━

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    await message.reply_text(text)

def register(app):
    app.add_handler(
        MessageHandler(broadcast, filters.command("broadcast")),
        group=14
    )

