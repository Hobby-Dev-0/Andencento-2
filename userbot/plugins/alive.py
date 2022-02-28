# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive
"""



import asyncio
import os
import random
from telethon import events, TelegramClient
from . import *
YOUR_NAME = os.environ.get("YOUR_NAME")
from telethon.tl.types import ChannelParticipantsAdmins


DEFAULTUSER = str(YOUR_NAME) if YOUR_NAME else "ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴜꜱᴇʀ"
""" =======================CONSTANTS====================== """
EXTREMEPRO_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
EXTREMEPRO = f"**`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO = " ┏━━━━━━━━━━━━━━━━━━━\\n"
EXTREMEPRO = f" ┣•➳➠ **`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┣•➳➠ "
EXTREMEPRO += "┗━━━━━━━━━━━━━━━━━━━\\n"
@Andencento.on(admin_cmd(outgoing=True, pattern="alive$"))
@Andencento.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(op):
    if op.fwd_from:
        return
    await op.get_chat()
    await op.delete()
    await borg.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await op.delete() 
