from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def profile(_, message):
    user = message.from_user

    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **𝗨sᴇʀ 𝗣ʀᴏғɪʟᴇ**

┏━━━━━━━━━━━━━━━┓
┃ 👤 {user.mention}
┃ 🆔 `{user.id}`
┃ 🌟 Premium Listener
┃ 🎧 Black Aura Member
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    await message.reply_text(text)

def register(app):
    app.add_handler(
        MessageHandler(profile, filters.command("profile")),
        group=16
    )

