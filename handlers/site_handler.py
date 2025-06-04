"""
Site command handler for ToDoTrip Telegram bot
Обработчик команды site для Telegram бота ToDoTrip
"""

from telebot import TeleBot, types
from config.config import WEBSITE_URL

def register_site_handler(bot: TeleBot):
    """
    Register the site command handler
    Зарегистрировать обработчик команды site
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(commands=['site'])
    def send_site(message):
        """
        Handle /site command by sending a web app button
        Обработать команду /site путем отправки кнопки веб-приложения
        """
        markup = types.InlineKeyboardMarkup()
        webapp_info = types.WebAppInfo(url=WEBSITE_URL)
        button = types.InlineKeyboardButton(
            text=f"Открыть {WEBSITE_URL}",
            web_app=webapp_info
        )
        markup.add(button)
        bot.send_message(
            chat_id=message.chat.id,
            text="Нажми на кнопку, чтобы перейти на сайт:",
            reply_markup=markup
        ) 