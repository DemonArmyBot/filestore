import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE_NAME = "bot.log"
PORT = int(os.environ.get("PORT", "8091"))
URL = os.environ.get("URL", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "7917224706"))  # Replace with your owner ID
MSG_EFFECT = int(os.environ.get("MSG_EFFECT", "5046509860389126442"))  # Replace with your message effect ID

DEFAULT_MESSAGES = {
    "START": "<b><blockquote>𝖧𝖾𝗒 {mention}!</blockquote></b>\n\n(っ◔◡◔)っ 𝕴 𝖆𝖒 𝖆 𝖋𝖎𝖑𝖊 𝖘𝖙𝖔𝖗𝖊 𝖇𝖔𝖙.\n𝖨 ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ.\n\n<b><blockquote>➤ 𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝚋𝚢 @DemonArmy</blockquote></b>",
    "FSUB": "<b><blockquote>✗ 【Ａｃｃｅｓｓ　Ｄｅｎｉｅｄ！】</blockquote></b>\n\nʏᴏᴜ ᴍᴜꜱᴛ ᴊᴏɪɴ ᴏᴜʀ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ. ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ʙᴇʟᴏᴡ.",
    "ABOUT": "<b><blockquote>𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭\n╭────[  𝚃𝚎𝚌𝚑𝚗𝚒𝚌𝚊𝚕 𝚂𝚝𝚊𝚌𝚔 ]────⍟\n➠ BӨƬ ПΛMΣ : {bot_name}\n\n➠ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @DemonArmy\n➠ ʟɪʙʀᴀʀʏ : Demon Library\n➠ ʟᴀɴɢᴜᴀɢᴇ : ǝɓɐnɓuɐ˥ uoɯǝᗡ\n➠ ᴅᴀᴛᴀʙᴀꜱᴇ : Dҽɱσɳ LιႦɾαɾყ\n➠ ᴠᴇʀꜱɪᴏɴ :  666 [ 𝖫𝖺𝗍𝖾𝗌𝗍 ]\n➠ ʜᴏꜱᴛɪɴɢ : plɹoM uoɯǝᗡ pǝʇɐɔıpǝᗡ\n╰───────────────⍟</blockquote></b>",
    "REPLY": "✓ ɪ ᴀᴍ ᴅᴇᴅɪᴄᴀᴛᴇᴅ ᴛᴏ ᴍʏ ᴍᴀꜱᴛᴇʀ, ᴀɴᴅ ʏᴏᴜ ᴀʀᴇɴ'ᴛ ᴡᴏʀᴛʜʏ ,ᴍᴏʀᴛᴀʟ!.",
    "START_PHOTO": "https://files.catbox.moe/xs6tvt.jpg",
    "ABOUT_PHOTO": "https://files.catbox.moe/myu6vn.jpg",
    "FSUB_PHOTO": "https://files.catbox.moe/d8l452.jpg",
    "SETTINGS_PHOTO": "https://files.catbox.moe/z9iavz.jpg",
    "AUTO_DEL_TEXT": "<b>⚠️ 𝙳𝚄𝙴 𝚃𝙾 𝙲𝙾𝙿𝚈𝚁𝙸𝙶𝙷𝚃 𝙸𝚂𝚂𝚄𝙴𝚂.......\n\n<blockquote>ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ {time}. 𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚃𝚑𝚎𝚖 𝚃𝚘 𝙰𝚗𝚢 𝙾𝚝𝚑𝚎𝚛 𝙿𝚕𝚊𝚌𝚎 𝙵𝚘𝚛 𝙵𝚞𝚝𝚞𝚛𝚎 𝙰𝚟𝚊𝚒𝚕𝚊𝚋𝚒𝚕𝚒𝚝𝚢.</blockquote>\n\n<blockquote>ᑎOTE : ᴜꜱᴇ ᴠʟᴄ ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ɢᴏᴏᴅ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴀᴘᴘ ᴛᴏ ᴡᴀᴛᴄʜ ᴛʜᴇ ᴠɪᴅᴇᴏꜱ ᴡɪᴛʜ ɢᴏᴏᴅ ᴇxᴘᴇʀɪᴇɴᴄᴇ!</blockquote></b>",
    "AUTO_DEL_PHOTO": "https://files.catbox.moe/l1sdcr.jpg"
}

BOTS = [
    {
        "session": os.environ.get("SESSION", "Demon"),  # Set your session name
        "token": os.environ.get("BOT_TOKEN", ""),  # Set your bot token
        "api_id": int(os.environ.get("API_ID", "0")),  # Set your API ID
        "api_hash": os.environ.get("API_HASH", ""),  # Set your API hash
        "workers": int(os.environ.get("WORKERS", "8")),
        "db_uri": os.environ.get("DATABASE_URL", ""),  # Set your MongoDB URI
        "db_uri_2": os.environ.get("DATABASE_URL_2", ""),
        "db_uri_3": os.environ.get("DATABASE_URL_3", ""),
        "db_uri_4": os.environ.get("DATABASE_URL_4", ""),
        "db_name": os.environ.get("DATABASE_NAME", ""),  # Set your database name
        "fsubs": [],
        "databases": {
            "primary": int(os.environ.get("PRIMARY_DB", "0")),
            "secondary": [],
            "backup": None
        },
        "auto_del": int(os.environ.get("AUTO_DEL", "600")),
        "messages": DEFAULT_MESSAGES,
        "admins": [],
        "disable_btn": False,
        "protect": False
    }
]

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(stream_handler)

    return logger
