from aiogram import Dispatcher, html, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile, FSInputFile
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv
import os
import logging
import sys
import asyncio

load_dotenv()

TOKEN = os.getenv('TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def start_message(message: Message) -> None:
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')

@dp.message()
async def another_message(message: Message | InputFile) -> None:
    ans = {"hello": "Hi", "hi": "Hi", "howareyou?":"I'm good!"}

    if message.text:

        msg = str(message.text).lower().replace(' ', '')
        try:
            if msg in ans:
                await message.answer(ans[msg])
            else:
                await message.answer("I can't understand you :(")
        except:
            await message.answer("WRONG!!! 0_0-_0-_-0_-")
    
    if message.photo:
        
        try:
            await message.answer_photo(photo=FSInputFile('222.jpg', filename='telegram'), caption='This telegram!')
        except:
            await message.answer("WRONG!!! 0_0-_0-_-0_-")

    if message.sticker:
        try:
            await message.answer('😍')
        except:
            await message.answer("WRONG!!! 0_0-_0-_-0_-")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())