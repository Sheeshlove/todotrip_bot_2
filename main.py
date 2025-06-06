"""
Main entry point for ToDoTrip Telegram bot
Основная точка входа для Telegram бота ToDoTrip
"""

import telebot
from config.config import BOT_TOKEN
from handlers.start_handler import register_start_handler
from handlers.help_handler import register_help_handler
from handlers.info_handler import register_info_handler
from handlers.site_handler import register_site_handler
from handlers.dagestan_handler import register_dagestan_handler
from handlers.contact_handler import register_contact_handler
from handlers.message_handler import register_message_handler
from handlers.user_tracker import register_user_tracker

def main():
    """
    Initialize and run the bot
    Инициализировать и запустить бота
    """
    # Initialize bot
    # Инициализация бота
    bot = telebot.TeleBot(BOT_TOKEN)

    # Register user tracker first (middleware)
    # Зарегистрировать отслеживание пользователей первым (middleware)
    register_user_tracker(bot)

    # Register all handlers
    # Регистрация всех обработчиков
    register_start_handler(bot)
    register_help_handler(bot)
    register_info_handler(bot)
    register_site_handler(bot)
    register_dagestan_handler(bot)
    register_contact_handler(bot)
    register_message_handler(bot)

    # Start the bot
    # Запуск бота
    print("Бот запущен, нажмите Ctrl+C для остановки.")
    bot.infinity_polling()

if __name__ == "__main__":
    main()