from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 📞", url="https://t.me/Peterparker6")],
        [InlineKeyboardButton(
            "𝔸𝕕𝕕 𝕄𝕖 😊", url="https://t.me/ytdownloadv2bot?startgroup=true")]
    ])
    welcomed = f"𝗛𝗲𝗹𝗹𝗼 {message.from_user.first_name}\n\n**I am the 𝐌𝐨𝐬𝐭 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐁𝐨𝐭😂**[📥](https://telegra.ph/file/a6cd21396b2430384ecc9.png)\n\n/help 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
