from aiogram import Bot, Dispatcher, executor, types
import aiohttp
import my_token

URL = ""

bot = Bot(my_token.TOKEN)
dp = Dispatcher(bot)


async def process(photo_url):
    params = {"photo_url": photo_url}
    return None


@dp.message_handler(commands=['start', 'help'])
async def start(message):
    await bot.send_message(message.chat.id, 'Жду фотографию для поиска человека в сети')


@dp.message_handler(content_types=["photo"])
async def get_photo(message: types.Message):
    file = await bot.get_file(message.photo[0].file_id)
    photo_url = bot.get_file_url(file.file_path)
    link = await process(photo_url)
    await message.reply(link if link else "Не нашел")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
