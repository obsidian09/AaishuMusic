from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_IMG

def register(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(_, message):
        text = f"""
🖤 **『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』**

Hey {message.from_user.mention} ✨

Premium Black Aura Music Bot
Made with 🖤 by Mohit Agarwal
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me", url="https://t.me/Aaishu_Music_Bot?startgroup=true")],
            [
                InlineKeyboardButton("👑 Owner", url="https://t.me/hey_mohit"),
                InlineKeyboardButton("💬 Support", url="https://t.me/Aaishu_bots")
            ],
            [InlineKeyboardButton("📢 Updates", url="https://t.me/Aaishu_Updates")]
        ])

        await message.reply_photo(START_IMG, caption=text, reply_markup=buttons)

