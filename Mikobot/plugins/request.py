from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Mikobot import app

LOG_ID = int("-1001989832800")
SUDO_USERS = [
    5978107653,
    5907205317,
    1284920298,
    5881613383,
]  # Replace with your actual list of admin IDs

toggle_status = True


@app.on_message(filters.command("request"))
async def requests(client, message):
    global toggle_status

    if not toggle_status:
        await message.reply_text("Sorry, the request feature is currently disabled.")
        return

    text_link = message.link
    text = message.text.split("/request")[1].strip()

    if not text:
        await message.reply_text(
            "For requests, please make sure to include the name of the anime."
        )
        return

    EVENT = InlineKeyboardMarkup([[InlineKeyboardButton(text="𝗘𝗩𝗘𝗡𝗧", url=text_link)]])

    USER_TEXT = f"""**<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, Your request has been successfully sent to our uploaders. They will reply to you soon. Thank you!**"""
    DEV_TEXT = f"""**❗️𝗡𝗲𝘄 𝗔𝗻𝗶𝗺𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁

ᴜsᴇʀ: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
ʀᴇǫᴜᴇsᴛ: {text}**"""

    # Send the request message to the log channel and pin it
    msg = await client.send_message(LOG_ID, DEV_TEXT, reply_markup=EVENT)
    await msg.pin()

    await message.reply_text(USER_TEXT)


@app.on_message(filters.command("toggle_request"))
async def toggle_request(client, message):
    global toggle_status

    if message.from_user.id not in SUDO_USERS:
        return

    toggle_status = not toggle_status

    if toggle_status:
        await message.reply_text("The request feature has been enabled.")
    else:
        await message.reply_text("The request feature has been disabled.")
