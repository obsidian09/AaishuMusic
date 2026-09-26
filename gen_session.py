from pyrogram import Client

API_ID = 30722253
API_HASH = "dc75139c00241733b1ab606216fa9424"

with Client(
    "session",
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
) as app:
    print("\n🖤 STRING SESSION 👇\n")
    print(app.export_session_string())

