import aiogram
import constants
import randomhacks
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

bot = aiogram.Bot(token=constants.token)
dp = aiogram.Dispatcher(bot)

markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row('🥧Кухня', '🛫Путешествия').row('📆Повседневные', '🌐Google')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Из каккой категории лайфхак вас интерисует?', reply_markup=markup1)


@dp.message_handler(lambda message: message.text == "🥧Кухня")
async def without_puree(message: types.Message):
    await message.answer(randomhacks.kitchen())


@dp.message_handler(lambda message: message.text == "📆Повседневные")
async def without_puree(message: types.Message):
    await message.answer(randomhacks.living())


@dp.message_handler(lambda message: message.text == "🌐Google")
async def without_puree(message: types.Message):
    await message.answer(randomhacks.google())


@dp.message_handler(lambda message: message.text == "🛫Путешествия")
async def without_puree(message: types.Message):
    await message.answer(randomhacks.travel())


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
