# Aiogram Telegram Bot

Бот написан на библиотеке [aiogram](https://docs.aiogram.dev/), с использованием асинхронного подхода.

## 📦 Возможности
- Команда /start и /help
- Ответ на фразу "Что такое ИИ?"
- Реакция на фото
- Скачивание изображений
- Отправка случайных картинок
- Получение погоды через OpenWeatherMap API

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/dnkrit/Aiogram.git
cd Aiogram
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` на основе `.env.example`:
```
cp .env.example .env
```
И вставьте свои ключи.

4. Запустите бота:
```bash
python main.py
```

## 🛡 Защита ключей

- **НЕ размещайте `.env` и `config.py` в GitHub**
- Файл `.env.example` — только шаблон без ключей
- Все чувствительные данные хранятся локально или на сервере

## 🧾 Структура проекта

```
project/
├── main.py
├── config.py
├── .env             # (НЕ в GitHub)
├── .env.example     # ✅ безопасный шаблон
├── requirements.txt
├── .gitignore
└── README.md
```

## 📬 Контакты

Автор: [dnkrit](https://github.com/dnkrit)
