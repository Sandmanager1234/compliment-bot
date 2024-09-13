import random
import asyncio
from bot import bot, COMPLIMENTS, db


async def send_compliment(tg_id):
    compliment = random.choice(COMPLIMENTS)
    await bot.send_message(tg_id, compliment)

async def main():
    users = db.get_users()
    tasks = []
    for user in users:
        tg_id = user[0]
        tasks.append(asyncio.create_task(send_compliment(tg_id)))
    asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())