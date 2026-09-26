from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def lyrics(_, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "🎙 **ᴜsᴇ →** `/lyrics song name`"
        )

    song = " ".join(message.command[1:])

    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗟ʏʀɪᴄs 𝗦ᴇᴀʀᴄʜ**

🎶 **{song}**

━━━━━━━━━━━━━━━
⚠ Lyrics API will be connected
in the next update.
━━━━━━━━━━━━━━━

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    await message.reply_text(text)

def register(app):
    app.add_handler(
        MessageHandler(lyrics, filters.command("lyrics")),
        group=

