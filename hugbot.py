import argparse
import asyncio
import os
import telegram
import time

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
assert BOT_TOKEN is not None
STICKER_ID = os.getenv('STICKER_ID')
assert STICKER_ID is not None

parser = argparse.ArgumentParser(description='Takes in a list of user IDs')
parser.add_argument('--ids', nargs='+', type=int, help='List of Telegram user IDs to hug')
    
args = parser.parse_args()
    
target_users = []
if args.ids:
    target_users = args.ids

print("Will hug these users: ", target_users)
bot = telegram.Bot(token=BOT_TOKEN)

async def hug_friends():
    try:
        for id in target_users:
            await bot.send_sticker(chat_id=id, sticker=STICKER_ID)
    except telegram.error.TelegramError as e:
        print(f'Error sending message: {e}')

async def hug_loop():
    while True:
        await hug_friends()
        print("Friends hugged~")
        time.sleep(3540)

if __name__ == "__main__":
    asyncio.run(hug_loop())
