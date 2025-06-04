"""
General message handler for ToDoTrip Telegram bot
Обработчик общих сообщений для Telegram бота ToDoTrip
"""

from telebot import TeleBot
from utils.helpers import get_user_name

def register_message_handler(bot: TeleBot):
    """
    Register the general message handler
    Зарегистрировать обработчик общих сообщений
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def echo_all(message):
        """
        Handle all text messages
        Обработать все текстовые сообщения
        """
        first_name = get_user_name(message)
        bot.send_message(
            message.chat.id,
            f"К сожалению, я не понимаю твоего сообщения. Пожалуйста, используй команду /help для начала работы с ботом.\n"
            f"\n"
            f"Если ты хочешь пообщаться с нашим менеджером, то воспользуйся командой /contact.\n"
            f"\n"
            f"Спасибо за понимание!"
        ) 