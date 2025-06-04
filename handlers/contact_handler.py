"""
Contact command handler for ToDoTrip Telegram bot
Обработчик команды contact для Telegram бота ToDoTrip
"""

from telebot import TeleBot
from config.config import SUPPORT_CONTACT

def register_contact_handler(bot: TeleBot):
    """
    Register the contact command handler
    Зарегистрировать обработчик команды contact
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(commands=['contact'])
    def send_contact(message):
        """
        Handle /contact command
        Обработать команду /contact
        """
        contact_text = f'Конечно! На все твои вопросы ответит Алексей {SUPPORT_CONTACT}'
        bot.reply_to(message, contact_text) 