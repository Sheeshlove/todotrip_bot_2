"""
Info command handler for ToDoTrip Telegram bot
Обработчик команды info для Telegram бота ToDoTrip
"""

from telebot import TeleBot
from config.config import FORWARD_CHANNEL_ID

def register_info_handler(bot: TeleBot):
    """
    Register the info command handler
    Зарегистрировать обработчик команды info
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(commands=['info'])
    def forward_specific_post(message):
        """
        Handle /info command by forwarding a specific post
        Обработать команду /info путем пересылки определенного поста
        """
        chat_id = message.chat.id
        message_id = 59  # ID of the specific post to forward
        try:
            bot.forward_message(chat_id, FORWARD_CHANNEL_ID, message_id)
        except Exception as e:
            bot.send_message(chat_id, f"Ой, что-то пошло не так: {e}") 