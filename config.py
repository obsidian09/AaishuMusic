# ═══════════════════════════════════════════════════════════
#                🖤  A A I S H U   M U S I C  🖤
#          Premium Telegram VC Music Bot • Black Aura
#
#  GitHub    : github.com/obsidian09/AaishuMusic
#  Made By   : Mohit Agarwal
#  Coder     : Mohit Agarwal
#  Version   : v1.0.0
# ═══════════════════════════════════════════════════════════

from os import getenv
from dotenv import load_dotenv

load_dotenv()

# ── Telegram Core ─────────────────────────────────────────
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# ── Owner ────────────────────────────────────────────────
OWNER_ID = int(getenv("OWNER_ID"))
OWNER_USERNAME = "MohitAgarwal"

# ── Branding ─────────────────────────────────────────────
BOT_NAME = "『 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 』🖤"
BOT_USERNAME = "AaishuMusicBot"
ASSISTANT_NAME = "『 𝗔ssɪsᴛᴀɴᴛ 』"

# ── Database ─────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")

# ── Assistant ────────────────────────────────────────────
STRING_SESSION = getenv("STRING_SESSION")

# ── Images ───────────────────────────────────────────────
START_IMG = "https://files.catbox.moe/buzc8q.jpg"
HELP_IMG = START_IMG

# ── Logger ───────────────────────────────────────────────
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

print("""
╔════════════════════════════════════╗
║      🖤 𝗔ᴀɪsʜᴜ 𝗠ᴜsɪᴄ 🖤
║   ✦ Made by Mohit Agarwal ✦
╚════════════════════════════════════╝
""")


