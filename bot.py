import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

# Твой токен и ссылка
TOKEN = "8151247032:AAGy-zCuwyji9gMJ8FjBqcO5GMlJK_ySIbg"

# Создаем простую веб-страничку прямо внутри бота
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delta Direct Install</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--tg-theme-bg-color, #ffffff);
            color: var(--tg-theme-text-color, #000000);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }
        h1 { font-size: 22px; margin-bottom: 24px; }
        .install-btn {
            background-color: var(--tg-theme-button-color, #2481cc);
            color: var(--tg-theme-button-text-color, #ffffff);
            border: none;
            border-radius: 12px;
            padding: 14px 28px;
            font-size: 16px;
            font-weight: 600;
            width: 100%;
            max-width: 300px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Delta Direct Install</h1>
    <a href="Itms-services://?action=download-manifest&url=https://github.com/royilkom-alt/downloads/raw/refs/heads/main/delta-executor-ios-directinstall.plist" class="install-btn">Скачать и установить</a>
    <script>
        let tg = window.Telegram.WebApp;
        tg.expand();
    </script>
</body>
</html>
"""

async def start_cmd(message: Message):
    # Вместо сайта сделаем кнопку, которая откроет красивое окно с установкой
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📥 Установить Delta",
                    web_app=WebAppInfo(url="https://telegra.ph/Delta-Install-03-30") # Временная ссылка на сайт
                )
            ]
        ]
    )
    
    await message.answer(
        "<b>Delta Direct Install</b>\n\nНажмите на кнопку ниже, чтобы открыть установку.",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.message.register(start_cmd, CommandStart())
    
    logging.basicConfig(level=logging.INFO)
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
