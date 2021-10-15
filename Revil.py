import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5 ,STRING6 ,STRING7 ,STRING8 ,STRING9 ,STRING10
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
from telegram import ParseMode


a = API_ID
b = API_HASH
smex = STRING
revill = STRING2
revilll = STRING3
revillll = STRING4
revilllll = STRING5
revilop = STRING6
revilopx = STRING7
revilopxx = STRING8
revilopxxx = STRING9
revilbotop = STRING10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
rdk = ""
mdk = ""
fdk = ""
ldk = ""
xdk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_revilbot():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global rdk
    global mdk
    global fdk
    global ldk
    global xdk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "revil"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if revill:
        session_name = str(revill)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if revilll:
        session_name = str(revilll)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if revillll:
        session_name = str(revillll)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if revilllll:
        session_name = str(revilllll)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass

    if revilop:
        session_name = str(revilop)
        print("String 6 Found")
        rdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await rdk.start()
            botme = await rdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        rdk = TelegramClient(session_name, a, b)
        try:
            await rdk.start()
        except Exception as e:
            pass  

    if revilopx:
        session_name = str(revilopx)
        print("String 7 Found")
        mdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await mdk.start()
            botme = await mdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        mdk = TelegramClient(session_name, a, b)
        try:
            await mdk.start()
        except Exception as e:
            pass  

    if revilopxx:
        session_name = str(revilopxx)
        print("String 8 Found")
        fdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await fdk.start()
            botme = await fdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        fdk = TelegramClient(session_name, a, b)
        try:
            await fdk.start()
        except Exception as e:
            pass 

    if revilopxxx:
        session_name = str(revilopxxx)
        print("String 9 Found")
        xdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await xdk.start()
            botme = await xdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        xdk = TelegramClient(session_name, a, b)
        try:
            await xdk.start()
        except Exception as e:
            pass 

    if revilbotop:
        session_name = str(revilbotop)
        print("String 10 Found")
        ldk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await ldk.start()
            botme = await ldk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        ldk = TelegramClient(session_name, a, b)
        try:
            await ldk.start()
        except Exception as e:
            pass                                                                                                                 
    
loop = asyncio.get_event_loop()
loop.run_until_complete(start_revilbot())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

EVIL_PIC = "https://telegra.ph/file/00bc1bdc3ea94c1b2adc0.jpg"
devs = [1787364816, 1787040289, 2031164360]

@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = revilbot[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(revilbot) == 2:
            message = str(revilbot[1])
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.dspam <sleep time> <count> <message to spam>\n\n.dspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        revilbot = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        revilbotisop = revilbot[1:]
        if len(revilbotisop) == 2:
            message = str(revilbotisop[1])
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴 𝗕𝗼𝘁 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(revilbot) == 2:
            message = str(revilbot[1])
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.curse"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = CURSE \n\nCommand:\n\n.curse <count> <Username of User>\n\n.curse <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(revilbot) == 2:
            message = str(revilbot[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in devs:
                text = f"This user is one of my developers, I can't betray him."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(revilbot[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in devs:
                text = f"This user is one of my developers, I can't betray him."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(revilbot[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@rdk.on(events.NewMessage(incoming=True))
@mdk.on(events.NewMessage(incoming=True))
@fdk.on(events.NewMessage(incoming=True))
@xdk.on(events.NewMessage(incoming=True))
@ldk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.replycurse"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆curse\n\nCommand:\n\n.replycurse <Username of User>\n\n.replycurse <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(revilbot[0])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in devs:
                text = f"This user is one of my developers, I can't betray him."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                nm = a.first_name
                que[g] = []
                qeue = que.get(g)
                appendable = [g]
                qeue.append(appendable)
                text = f"Activated Reply Curse on {nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in devs:
                text = f"This user is one of my developers, I can't betray him."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                nm = b.first_name
                que[g] = []
                qeue = que.get(g)
                appendable = [g]
                qeue.append(appendable)
                text = f"Activated Reply Curse on {nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.dreplycurse"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆curse\n\nCommand:\n\n.dreplycurse <Username of User>\n\n.dreplycurse <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(revilbot[0])
            a = await e.client.get_entity(message)
            g = a.id
            nm = a.first_name
            try:
                queue = que.get(g)
                queue.pop(0)
                text = f"De-Activated Reply Curse on {nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
            except Exception as f:
                pass
            text = "Never activated reply curse on this user"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            nm = b.first_name
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
                text = f"De-Activated Reply Curse on {nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
            except Exception as f:
                pass
            text = "Never activated reply curse on this user"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Waking Up The BOT..!!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n𝗥𝐄V𝐈𝗟 Sᴘᴀᴍ BᴏT ʜᴇʀᴇ `{ms}` 𝗠𝗦")
    


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝗥𝗲𝗯𝗼𝗼𝘁𝗲𝗱\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await rdk.disconnect()
        except Exception as e:
            pass
        try:
            await mdk.disconnect()
        except Exception as e:
            pass
        try:
            await fdk.disconnect()
        except Exception as e:
            pass
        try:
            await ldk.disconnect()
        except Exception as e:
            pass   
        try:
            await xdk.disconnect()
        except Exception as e:
            pass                 
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

       
@idk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.evil"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
        message_id = event.message.id
        try:
            text = "👅 𝗥𝐄V𝐈𝗟 𝐒ᴘᴀ𝐌 𝐁ᴏ𝐓 [👅](https://telegra.ph/file/00bc1bdc3ea94c1b2adc0.jpg)\n\n\n ✧ ʀᴇᴠɪʟ sᴘᴀᴍ BᴏT ɪs ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/REVIL_BOT_SUPPORT)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝐄V𝐈𝗟](https://t.me/DARK_EAGLES_OWNER)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/RevilhunterOp/REVILSPAMBOT) 🖤"
            event = await event.client.send_file(event.chat_id, EVIL_PIC, caption = text, reply_to=message_id, link_preview=None )
        except:
            text = "👅 𝗥𝐄V𝐈𝗟 𝐒ᴘᴀ𝐌 𝐁ᴏ𝐓 [👅](https://telegra.ph/file/00bc1bdc3ea94c1b2adc0.jpg)\n\n\n ✧ ʀᴇᴠɪʟ sᴘᴀᴍ BᴏT ɪs ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17 \n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/REVIL_BOT_SUPPORT)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗥𝐄V𝐈𝗟](https://t.me/DARK_EAGLES_OWNER)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/RevilhunterOp/REVILSPAMBOT) 🖤"
            event = await event.reply(text, link_preview=None )
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.evil\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.dspam\n.bigspam\n.curse\n.replycurse\n.dreplycurse\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """
██████╗░███████╗██╗░░░██╗██╗██╗░░░░░
██╔══██╗██╔════╝██║░░░██║██║██║░░░░░
██████╔╝█████╗░░╚██╗░██╔╝██║██║░░░░░
██╔══██╗██╔══╝░░░╚████╔╝░██║██║░░░░░
██║░░██║███████╗░░╚██╔╝░░██║███████╗
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝╚══════╝ """

print(text)
print("")
print("Congrats REVIL MULTI SPAMBOT STARTED SUCCESSFULLY . TYPE .evil TO CHECK YOUR BOT'S STATUS")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        rdk.disconnect()
    except Exception as e:
        pass 
    try:
        mdk.disconnect()
    except Exception as e:
        pass
    try:
        fdk.disconnect()
    except Exception as e:
        pass 
    try:
        xdk.disconnect()
    except Exception as e:
        pass
    try:
        ldk.disconnect()
    except Exception as e:
        pass                  
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        rdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        mdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        fdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        ldk.run_until_disconnected()
    except Exception as e:
        pass                 
