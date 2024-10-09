from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


bot = Bot(token='<KEY>')
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_inf = KeyboardButton(text='Информация')
button_kkal = KeyboardButton(text='Рассчитать')
keyboard.add(button_kkal, button_inf)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.reply("Информация о боте пока в разработке")


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.reply('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.reply('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.reply(f"Ваша расчетное потребление "
                        f"калорий:{10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.reply('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
