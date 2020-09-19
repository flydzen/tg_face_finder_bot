from aiogram import Bot, Dispatcher, executor, types
import aiohttp
from settings import settings

import asyncio


asyncio.run
URL = ""

DEBUG = True
class FinderClient:
    def __init__(self):
        self.session = aiohttp.ClientSession

    async def process(self, photo_url):
        if DEBUG:
            return print(photo_url)
        params = {"photo_url": photo_url}
        async with self.session as s:
            async with s.post(settings.finder_url, data=params) as resp:
                return await resp.json()

bot = Bot(settings.token)
dp = Dispatcher(bot)
finder = FinderClient()

@dp.message_handler(commands=['start', 'help'])
async def start(self, message):
    await self.bot.send_message(message.chat.id, 'Жду фотографию для поиска человека в сети')


@dp.message_handler(content_types=["photo"])
async def get_photo(message: types.Message):
    file = await bot.get_file(message.photo[0].file_id)
    photo_url = bot.get_file_url(file.file_path)
    link = await finder.process(photo_url)
    await message.reply(link if link else "Не нашел")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
