from pyrogram import filters
from pyrogram.handlers import MessageHandler

QUEUE = []

async def queue_cmd(_, message):
    if not QUEUE:
        return await message.reply_text("""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗤ᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ**

━━━━━━━━━━━━━━━
🎧 Add songs with `/play`
━━━━━━━━━━━━━━━

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
""")

    text = "🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**\n\n> ✦ **𝗖ᴜʀʀᴇɴᴛ 𝗤ᴜᴇᴜᴇ**\n\n"

    for i, song in enumerate(QUEUE, 1):
        text += f"**{i}.** {song}\n"

    text += "\n**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**"

    await message.reply_text(text)

def register(app):
    app.add_handler(MessageHandler(queue_cmd, filters.command("queue")), group=5)

