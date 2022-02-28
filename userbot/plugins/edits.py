import asyncio
import random
from random import choice
import requests
import re
import time

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from . import *


@Andencento.on(admin_cmd(pattern="type (.*)"))
@Andencento.on(sudo_cmd(pattern="type (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    shiiinabot = "\u2060"
    for _ in range(601):
        shiiinabot += "\u2060"
    try:
        await eor(event, shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = "_"
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await eor(event, typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = f'{previous_text}{character}'
        typing_text = f'{previous_text}{typing_symbol}'
        try:
            await eor(event, typing_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        try:
            await eor(event, previous_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)


@Andencento.on(admin_cmd(pattern="emoji (.*)"))
@Andencento.on(sudo_cmd(pattern="emoji (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(16)
    input_str = event.pattern_match.group(1)
    if input_str == "shrug":
        await eor(event, "¯\_(ツ)_/¯")
    elif input_str == "apple":
        await eor(event, "\uF8FF")
    elif input_str == ":/":
        await eor(event, input_str)
        animation_chars = [":\\", ":/"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
    elif input_str == "-_-":
        await eor(event, input_str)
        animation_chars = ["-__-", "-_-"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])


@Andencento.on(admin_cmd(pattern="gendar$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="gendar$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(GENDER)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="shrug$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="shrug$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SHRUG)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="doge", outgoing=True))
@Andencento.on(sudo_cmd(pattern="doge", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DOG)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="mesed$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="mesed$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SED)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="medead$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="medead$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DEAD)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="confused$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="confused$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(CONFUSED)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="lobb$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="lobb$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(LOB)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="wut$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="wut$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WTF)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="wavee$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="wavee$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WAVING)
    await edit_or_reply(e, txt)
    
@Andencento.on(admin_cmd(pattern="hehe$", outgoing=True))
@Andencento.on(sudo_cmd(pattern="hehe$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(EMOTICONS)
    await edit_or_reply(e, txt)
    
CmdHelp("edits").add_command(
  "hehe", None, "Use and see"
).add_command(
  "wavee", None, "Use and see"
).add_command(
  "wut", None, "Use and see"
).add_command(
  "lobb", None, "Use and see"
).add_command(
  "confused", None, "Use and see"
).add_command(
  "medead", None, "Use and see"
).add_command(
  "mesed", None, "Use and see"
).add_command(
  "doge", None, "Use and see"
).add_command(
  "shrug", None, "Use and see"
).add_command(
  "gendar", None, "Use and see"
).add_command(
  "type", "<word>", "Animates the given word into a typewriter."
).add_command(
  "emoji", None, "Available cmnds are:-\n• shrug\n• apple\n• :/\n• -_-\n Add .emoji in front of all cmds."
).add_info(
  "Bass Bakchodi hai ye."
).add_warning(
  "✅ Harmless Module."
).add()
