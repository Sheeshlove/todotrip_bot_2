"""
Help command handler for ToDoTrip Telegram bot
Обработчик команды help для Telegram бота ToDoTrip
"""

from telebot import TeleBot

def register_help_handler(bot: TeleBot):
    """
    Register the help command handler
    Зарегистрировать обработчик команды help
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    @bot.message_handler(commands=['help'])
    def send_help(message):
        """
        Handle /help command
        Обработать команду /help
        """
        help_text = (
            "Вот все мои команды:\n"
            "\n"
            "/info - что такое ToDoTrip?\n"
            "\n"
            "/site - наш веб-сайт\n"
            "\n"
            "/dagestan - отвечаем на самые важные вопросы по Дагестану\n"
            "\n"
            "/contact - переведём тебя на живого сотрудника, чтобы он ответил тебе на всё и за всё"
        )
        bot.reply_to(message, help_text) 