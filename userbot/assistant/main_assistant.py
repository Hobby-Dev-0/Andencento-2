import asyncio
import io
import os
import re

from telethon import Button, custom, events, functions
import telethon
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id
from ..config import Config
from .. import noob, bot
from ..sql.blacklist_ass import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)

from ..sql.bot_users_sql import add_me_in_db, his_userid
from ..sql.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
# await function async def ke baad lagega

@noob.on(events.NewMessage(pattern="/start$"))
async def start(event):
    pro = await bot.get_me()
    boy = pro.id
    iam = await noob.get_me()
    bot_id = iam.first_name
    bot_username = iam.username
    replied_user = await tbot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    devlop = await bot.get_me()
    hmmwow = devlop.first_name
    vent = event.chat_id
    mypic = "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Assistant Bot. \n\nMy Master [{hmmwow}](tg://user?id={boy}) \nYou Can Talk/Contact My Master Using This Bot. \n\nIf You Want Your Own Assistant Bot You Can Deploy From Button Below. \n\nPowered By [Andencento](t.me/AndencentoSupport)"
    if event.sender_id == boy:
        await tbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
            buttons=[
                [custom.Button.inline("Show Bot Users", data="users")],
                [custom.Button.inline("Show My Commands", data="cmds")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tbot.send_file(
            event.chat_id,
            file=mypic,
            caption=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.url("Deploy Andencento Bot", "https://github.com/Noob-Stranger/andencento")],
                [Button.url("Support", "t.me/AndencentoSupport")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


@noob.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    pro = await bot.get_me()
    boy = pro.id
    if event.is_group:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for ultrappl in total_users:
            users_list += ("=> {} \n").format(int(ultrappl.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@noob.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmds")))
async def users(event):
    await event.delete()
    #@LEGENDX, #@PROBOY add cmd List Here
    # later bro
    pass

@noob.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.is_group:
        return
    if event.raw_text.startswith("/"):
        return
    if os.environ.get("SUB_TO_MSG_ASSISTANT", False):
        try:
            result = await tbot(
                functions.channels.GetParticipantRequest(
                    channel=Config.JTM_CHANNEL_ID, user_id=event.sender_id
                )
            )
        except telethon.errors.rpcerrorlist.UserNotParticipantError:
            await event.reply(f"**Opps, I Couldn't Forward That Message To Owner. Please Join My Channel First And Then Try Again!**",
                             buttons = [Button.url("Join Channel", Config.JTM_CHANNEL_USERNAME)])
            return
    await event.get_sender()
    sed = await event.forward_to(bot.uid)
    add_me_in_db(sed.id, event.sender_id, event.id)


@noob.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id != bot.uid:
        return
    elif event.raw_text.startswith("/"):
        return
    elif event.text is not None and event.media:
        bot_api_file_id = pack_bot_file_id(event.media)
        await tbot.send_file(
            user_id,
            file=bot_api_file_id,
            caption=event.text,
            reply_to=reply_message_id,
        )
    else:
        msg_s = event.raw_text
        await tbot.send_message(
            user_id,
            msg_s,
            reply_to=reply_message_id,
        )


@noob.on(events.NewMessage(pattern="/broadcast ?(.*)"))
async def sedlyfsir(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id == boy:
         return
    msgtobroadcast = event.text.split(" ", maxsplit=1)[1]
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    hmmok = ""
    if msgtobroadcast == None:
        await event.reply("`Wait. What? Broadcast None?`")
        return
    elif msgtobroadcast == " ":
        await event.reply("`Give Something to Broadcast ☺️`")
        return
    for uzers in userstobc:
        try:
            sent_count += 1
            await tbot.send_message(int(uzers.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except:
            error_count += 1
    await tbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@noob.on(events.NewMessage(pattern="/stats"))
async def _(event):
    if not event.sender_id == boy:
       return
    eberyone = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(eberyone)}"
    )



@noob.on(events.NewMessage(pattern="/block ?(.*)"))
async def ok(event):
    if not event.sender_id == boy:
         return
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@noob.on(events.NewMessage(pattern="/unblock ?(.*)"))
async def gey(event):
    if not event.sender_id == boy:
        return
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await tbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
