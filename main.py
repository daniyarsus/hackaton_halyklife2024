from aiogram import Bot, Dispatcher, types
import openai
from src.settings.config import Settings

openai.api_key = Settings.OPEN_API_KEY
bot = Bot(token=Settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


def get_info_about_book():
    return "Информация о книгах..."


def get_info_about_server():
    # Ваш код для получения информации о сервере
    return "Информация о сервере..."


async def process_command(message_text):
    # Использование OpenAI для определения команды
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-0301",
        prompt=message_text,
        max_tokens=50
    )
    interpreted_command = response.choices[0].text.strip()

    # Определение и вызов функции на основе интерпретации
    if "данные обо мне" in interpreted_command:
        return get_info_about_user()
    elif "данные о сервере" in interpreted_command:
        return get_info_about_server()
    else:
        return "Команда не распознана."


@dp.message_handler()
async def echo(message: types.Message):
    response = await process_command(message.text)
    await message.reply(response)


if __name__ == '__main__':
    from aiogram.utils.executor import start_polling
    start_polling(dp, skip_updates=True)

