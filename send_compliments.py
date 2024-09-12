import random
import asyncio
from bot import bot, COMPLIMENTS, db


async def send_compliment(tg_id):
    compliment = random.choice(COMPLIMENTS)
    await bot.send_message(tg_id, compliment)

if __name__ == '__main__':
    users = db.get_users()
    for user in users:
        tg_id = user[0]
        asyncio.run(send_compliment(tg_id))