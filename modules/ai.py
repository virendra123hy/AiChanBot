from pyrogram import filters
from pyrogram.types import Message
import requests
from config import neko, BOT_ID


@neko.on_message(filters.text, group=100)
async def ai(_, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.id == 5756340137
        ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={message.text}", timeout=5).json()["response"]
        print(ai_gen)
        await neko.send_message(chat_id=message.chat.id ,text=ai_gen , reply_to_message_id=message.id)

    

@neko.on_message(filters.command(commands=["Miss_KajalBoT"] , prefixes="@"))
async def username(_, message: Message):
    fixed_text = message.text.replace("@Miss_KajalBoT ", "")
    ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={fixed_text}", timeout=5).json()["response"]
    print(ai_gen)
    await neko.send_message(chat_id=message.chat.id ,text=ai_gen, reply_to_message_id=message.id)
