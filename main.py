from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hi, I am ANONYMOUS SENDER BOT.\n\n"
                 "Just Forward me Some messages or\n"
                 "media and I will Erase the\n"
                 "sender tag & will give U.\n\n"
                 "**Note -** Dont Spoil Bot with Porn\n__"
                 "Contents. This Bot is\n__"
                 "free to use\n__"
                 "__for all !!\n\n__"
                 "Please Support Us\n"
                 "By Joining the Support Group👇👇")

START_IMG = os.environ.get('START_IMG', None)
if START_IMG is None:
    img = "https://telegra.ph/file/fc734b227985a1524e715.jpg"
else:
  img = START_IMG

if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("👨‍💻 My Dev 👨‍💻","https://t.me/Sunisk")],[Button.url("🧑‍🔧 Maintained By 🧑‍🔧","https://t.me/Physic_hybrid")],
                                         [Button.url("🧑‍🔧 Support Group 🧑‍🔧","https://t.me/InFoTelGroup")]])                                                                 
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
