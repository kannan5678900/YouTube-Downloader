from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

PHOTO = [
    "https://telegra.ph/file/0a37f338a47ab2a909997.jpg",
    "https://telegra.ph/file/9be92d8a94f53bf6d6192.jpg",
    "https://telegra.ph/file/1c4dc6991b182c4af1512.jpg",
    "https://telegra.ph/file/400882986bb62bab8940d.jpg"
]

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    chat_id = message.chat.id
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 📞", url="https://t.me/Peterparker6")],
        [InlineKeyboardButton("𝔸𝕕𝕕 𝕄𝕖 😊", url="https://t.me/ytdownloadv2bot?startgroup=true")]
    ])
    welcomed = f"𝗛𝗲𝗹𝗹𝗼 {message.from_user.first_name}\n\n**I am the 𝐌𝐨𝐬𝐭 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐁𝐨𝐭😂**\n\n/help 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨"
    await client.send_photo(
        chat_id, 
        photo=f"{random.choice(PHOTO)}",
        caption=welcomed,
        reply_markup=joinButton,
        parse_mode="html",
)
    raise StopPropagation
