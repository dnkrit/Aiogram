import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, WEATHER_API_KEY
import random
import aiohttp
import os

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка текста "Что такое ИИ?"
@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ — это искусственный интеллект. Он умеет учиться, анализировать и помогать людям. Я — его пример 😊')

# Обработка и сохранение фото пользователя
@dp.message(F.photo)
async def react_photo(message: Message):
    phrases = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(phrases)
    await message.answer(rand_answ)

    # Создание папки tmp при необходимости
    os.makedirs("tmp", exist_ok=True)

    file_id = message.photo[-1].file_id
    await bot.download(message.photo[-1], destination=f'tmp/{file_id}.jpg')

# Команда /photo — бот отправляет случайное изображение
@dp.message(Command("photo"))
async def send_photo(message: Message):
    images = [
        'https://news-img.gismeteo.st/ru/2021/01/shutterstock_1390386575-768x512.jpg',
        'https://cdn1.ozone.ru/s3/multimedia-1-9/c600/6917064525.jpg',
        'https://i.pinimg.com/736x/f7/57/65/f7576577cb0919bdb2d52bd199390c24--panda-funny-nature-animals.jpg'
    ]
    rand_image = random.choice(images)
    await message.answer_photo(photo=rand_image, caption="Это супер крутая картинка")

# Команда /weather — прогноз погоды
@dp.message(Command("weather"))
async def get_weather(message: Message):
    city = "Moscow"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                await message.answer(f"Погода в {city}:\nТемпература: {temp}°C\nСостояние: {desc}")
            else:
                text = await resp.text()
                await message.answer(f"Ошибка {resp.status}:\n{text}")

# Команда /help
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Яботик может:\n/start — приветствие\n/help — список команд\n/photo — случайная картинка\n/weather — погода в Москве\nИли спроси: "Что такое ИИ?"')

# Команда /start
@dp.message(CommandStart())
async def start(message: Message):
    print(f"Получена команда /start от {message.from_user.id}")
    await message.answer(f'Приветики, {message.from_user.first_name}!')

# Общий хендлер: если пользователь напишет "test"
@dp.message()
async def text(message: Message):
    if message.text and message.text.lower() == "test":
        await message.answer("Тестируем")
    else:
        await message.send_copy(chat_id=message.chat.id)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
