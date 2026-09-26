from time import time
from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def ping(_, message):
    start = time()

    m = await message.reply_text("🖤 **Pɪɴɢɪɴɢ Aᴀɪsʜᴜ...**")

    ms = (time() - start) * 1000

    txt = f"""
**『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』** 🖤

> ✦ **Sʏsᴛᴇᴍ Sᴛᴀᴛᴜs**

┏━━━━━━━━━━━━━━━┓
┃ ⚡ **{ms:.0f} ms**
┃ 🟢 ʙᴏᴛ : ᴏɴʟɪɴᴇ
┃ 🎧 ᴍᴏᴅᴇ : ᴘʀᴇᴍɪᴜᴍ
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    await m.edit_text(txt)

def register(app):
    app.add_handler(MessageHandler(ping, filters.command("ping")), group=2)

