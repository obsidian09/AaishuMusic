from pyrogram import filters
from pyrogram.handlers import MessageHandler

ADMINS = filters.group & filters.command(["skip","pause","resume","end"])

async def admin_cmd(_, message):
    cmd = message.command[0].lower()

    data = {
        "skip":("⏭","𝗦𝗸𝗶𝗽𝗽𝗲𝗱","Next track loaded"),
        "pause":("⏸","𝗣𝗮𝘂𝘀𝗲𝗱","Playback paused"),
        "resume":("▶️","𝗥𝗲𝘀𝘂𝗺𝗲𝗱","Music resumed"),
        "end":("⏹","𝗘𝗻𝗱𝗲𝗱","Queue cleared")
    }

    emoji,title,desc = data[cmd]

    await message.reply_text(f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

{emoji} **{title}**

> {desc}

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
""")

def register(app):
    app.add_handler(MessageHandler(admin_cmd, ADMINS), group=4)

