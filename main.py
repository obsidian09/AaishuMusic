from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *

from plugins.play import register as play_register
from plugins.ping import register as ping_register
from plugins.help import register as help_register
from plugins.about import register as about_register
from plugins.settings import register as settings_register
from plugins.queue import register as queue_register
from plugins.owner import register as owner_register
from plugins.profile import register as profile_register
from plugins.broadcast import register as broadcast_register
from plugins.voice import register as voice_register
from plugins.lyrics import register as lyrics_register
from plugins.callbacks import register as callback_register
from plugins.stats import register as stats_register
from plugins.admin import register as admin_register

app = Client(
    "AaishuMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    caption = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

Hey {message.from_user.mention} ✨

Premium Black Aura Music Bot

**𓆩 𝗠𝗼𝗵𝗶𝘁 𝗔𝗴𝗮𝗿𝘄𝗮𝗹 𓆪**
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ 𝗔ᴅᴅ 𝗠ᴇ", url="https://t.me/Aaishu_Music_Bot?startgroup=true")],
        [
            InlineKeyboardButton("👑 𝗢ᴡɴᴇʀ", url="https://t.me/hey_mohit"),
            InlineKeyboardButton("💬 𝗦ᴜᴘᴘᴏʀᴛ", url="https://t.me/Aaishu_bots")
        ],
        [InlineKeyboardButton("📢 𝗔ᴀɪsʜᴜ 𝗨ᴘᴅᴀᴛᴇꜱ", url="https://t.me/Aaishu_Updates")]
    ])

    await message.reply_photo(
        photo=START_IMG,
        caption=caption,
        reply_markup=buttons
    )

play_register(app)
ping_register(app)
help_register(app)
about_register(app)
settings_register(app)
queue_register(app)
owner_register(app)
profile_register(app)
broadcast_register(app)
voice_register(app)
lyrics_register(app)
callback_register(app)
stats_register(app)
admin_register(app)

print("🖤 Aaishu Music Started")
app.run()
