"""Emoji

Available Commands:

.think"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "think":
        await event.edit(input_str)
        animation_chars = [
            "THINKING",
            "THINK RETARD THINK",
            "THI&K#N₹",
            "USE YOUR FUCKING BRAIN",
            "¿H$NK∆NG",
            "DAMN YOU RETARD*",
            "NGITHKIN",
            "ITS LIKE SEARCHING FOR GOOD PORN",
            "THINKING",
            "BRAIN.EXE STOPPED WORKING",
            "T+IN@I?G",
            "EMPTY ASF BRAIN",
            "¶H×NK&N*",
            "DO YOU EVEN HAVE A BRAIN NIGGA?",
            "T+I#K@₹G",
            "I'M HIGH ON DRUGS",
            "THI&K#N₹",
            "NEED TIME TO PROCESS",
            "¿H$NK∆NG",
            "ERROR 404*",
            "NGITHKIN",
            "WTF I CANT THINK",
            "THINKING",
            "WTF IS THIZZZ",
            "T+IN@I?G",
            "BRAIN SHUTDOWN",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
