from pyrogram import filters
from pyrogram.handlers import CallbackQueryHandler

async def close_cb(_, q):
    await q.message.delete()

async def pause_cb(_, q):
    await q.answer("⏸ 𝗣ᴀᴜsᴇᴅ", show_alert=True)

async def skip_cb(_, q):
    await q.answer("⏭ 𝗦ᴋɪᴘᴘᴇᴅ", show_alert=True)

async def queue_cb(_, q):
    await q.answer(
        "🖤 『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』\n\n📜 𝗤ᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ",
        show_alert=True
    )

def register(app):
    app.add_handler(
        CallbackQueryHandler(close_cb, filters.regex("^close$")), group=9
    )
    app.add_handler(
        CallbackQueryHandler(pause_cb, filters.regex("^pause$")), group=10
    )
    app.add_handler(
        CallbackQueryHandler(skip_cb, filters.regex("^skip$")), group=11
    )
    app.add_handler(
        CallbackQueryHandler(queue_cb, filters.regex("^queue$")), group=12
    )

