"""
Start command handler for ToDoTrip Telegram bot
Обработчик команды start для Telegram бота ToDoTrip
"""

from telebot import TeleBot
from utils.helpers import get_user_name

def register_start_handler(bot: TeleBot):
    """
    Register the start command handler
    Зарегистрировать обработчик команды start
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        """
        Handle /start command
        Обработать команду /start
        """
        first_name = get_user_name(message)
        bot.reply_to(
            message,
            f"Привет, {first_name}! Рад тебя видеть! "
            "Если у тебя есть какие вопросы по Дагестану, введи команду /dagestan, "
            "если ты хочешь задать вопросы одному из организаторов, пиши @insendro, "
            "для всего остального есть /help"
        ) 