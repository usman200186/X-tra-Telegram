"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
       
            "`Calling Mr.Robot`",
            "`Mr.Robot Agreed to fuck your ass`",
            "`Connecting To Mr.Robot's Anonymous Server...`",
            "`Mr.Robot Starting His Hacks`",
            "`Target Selected.`",
            "`Hacking External Storage... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking Sd Card... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking My Files... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking Camera... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Searching & Saving Nudes... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Locking Your Device... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking Snapchat Nudes... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Target Successfully Hacked...\n\nPay 69$ To` @ItsBuddy007 `Or suck my dick to remove This Hack`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
