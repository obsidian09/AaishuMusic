# ═══════════════════════════════════════════════════════════
#                🖤  A A I S H U   M U S I C  🖤
#                    Premium Play Plugin
#  Made By  : Mohit Agarwal
# ═══════════════════════════════════════════════════════════

from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from AaishuMusic.core.player import play_song

async def play(_, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "✦ **Usage →** `/play song name`"
        )

    query = " ".join(message.command[1:])
    wait = await message.reply_text("🖤 **Searching Your Vibe...**")

    song = await play_song(message.chat.id, query)

    text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

> ✦ **Now Playing**

🎶 **{song['title']}**

┏━━━━━━━━━━━━━━━┓
┃ ⏱ {song['duration']} sec
┃ 👁 {song['views']} views
┃ 🎧 Black Aura Player
┗━━━━━━━━━━━━━━━┛

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    btn = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⏸ 𝗣ᴀᴜsᴇ", callback_data="pause"),
            InlineKeyboardButton("⏭ 𝗦ᴋɪᴘ", callback_data="skip")
        ],
        [
            InlineKeyboardButton("📜 𝗤ᴜᴇᴜᴇ", callback_data="queue"),
            InlineKeyboardButton("❌ 𝗖ʟᴏsᴇ", callback_data="close")
        ]
    ])

    await wait.delete()

    await message.reply_photo(
        photo=song["thumbnail"],
        caption=text,
        reply_markup=btn
    )

def register(app):
    app.add_handler(
        MessageHandler(play, filters.command("play")),
        group=1
    )
