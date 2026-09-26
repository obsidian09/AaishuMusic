# ═══════════════════════════════════════════════════════════
#                🖤  A A I S H U   M U S I C  🖤
#                    Premium Voice Plugin
#  Made By  : Mohit Agarwal
# ═══════════════════════════════════════════════════════════

from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def vc(_, message):
    cmd = message.command[0].lower()

    if cmd == "join":
        txt = """
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗩ᴏɪᴄᴇ 𝗖ʜᴀᴛ 𝗖ᴏɴɴᴇᴄᴛᴇᴅ**

🎧 Assistant joined successfully.

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""
    else:
        txt = """
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗩ᴏɪᴄᴇ 𝗖ʜᴀᴛ 𝗗ɪsᴄᴏɴɴᴇᴄᴛᴇᴅ**

👋 Assistant left the VC.

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    await message.reply_text(txt)

def register(app):
    app.add_handler(
        MessageHandler(vc, filters.command(["join","leave"])),
        group=17
    )

