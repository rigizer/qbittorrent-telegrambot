from quart import Quart, request  # pip install quart
from datetime import datetime

import os
import telegram  # pip install python-telegram-bot
import asyncio
import platform

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

SERVER_NAME = os.environ['SERVER_NAME']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHATID = os.environ['TELEGRAM_CHATID']

bot = telegram.Bot(token=TELEGRAM_TOKEN)
app = Quart(__name__)

@app.route('/')
async def send_message():
    time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    name: str = request.args.get('name')
    size: int = size_convert(int(request.args.get('size')))
    path: str = request.args.get('path')

    content = '[Qbittorrent] 다운로드 완료\n[SERVER] {}\n\n이름: {}\n크기: {}\n저장경로 {}\n완료시간: {}'.format(SERVER_NAME, name, size, path, time)
    
    await bot.send_message(chat_id=TELEGRAM_CHATID, text=content)
    
    return 'success'

def size_convert(size):
    if size >= 1024:
        size = round(size / 1024, 2)
        if size >= 1024:
            size = round(size / 1024, 2)
            if size >= 1024:
                size = round(size / 1024, 2)
                size = "{} GBytes".format(size)
            else:
                size = "{} MBytes".format(size)
        else:
            size = "{} KBytes".format(size)
    else:
        size = "{} Bytes".format(size)
    
    return size

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)