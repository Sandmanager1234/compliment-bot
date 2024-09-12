import os
import sys
import logging
import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from dbmanager import DBmanager

TOKEN = os.getenv('BOT_TOKEN')

with open('compliments.txt', 'r', encoding='utf8') as file:
    COMPLIMENTS = file.read().split('\n')

bot = Bot(token=TOKEN)
dp = Dispatcher()
db = DBmanager()

@dp.message(Command('govstr'))
async def start_vstr(msg: types.Message):
    tg_id = msg.from_user.id
    if db.user_exists(tg_id):
        if db.user_is_active(tg_id):
            await msg.answer('Зайка, ты уже подписана на комплименты, жди их утром и вечером каждый день!')
        else:
            await msg.answer('Милая, ты снова подписана на комплименты! Жди их с утра и вечером!')
            db.change_user(tg_id, True)
    else:
        await msg.answer('С этого дня ты будешь получать комплименты утром и вечером. Держи первый комплимент!')
        await msg.answer(f'{random.choice(COMPLIMENTS)}')
        db.add_user(tg_id)


@dp.message(Command('stop'))
async def stop_vsrt(msg: types.Message):
    await msg.answer('Вы больше получите комплименты((\nЕсли передумаете напишите комманду /govstr')
    tg_id = msg.from_user.id
    db.change_user(tg_id)


@dp.message(CommandStart())
async def start_message(msg: types.Message):
    await msg.answer('Привет, зайка! Хочешь получать комплименты ежедневно? Введи команду /govstr, если надоест ты можешь от них отказаться командой /stop.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    