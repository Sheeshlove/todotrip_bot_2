"""
User tracking handler for ToDoTrip Telegram bot
Обработчик отслеживания пользователей для Telegram бота ToDoTrip
"""

import os
from telebot import TeleBot

# File to store user IDs
USER_IDS_FILE = "user_ids.txt"

def initialize_user_file():
    """
    Create user_ids.txt file if it doesn't exist
    Создать файл user_ids.txt, если он не существует
    """
    if not os.path.exists(USER_IDS_FILE):
        with open(USER_IDS_FILE, 'w', encoding='utf-8') as f:
            f.write("")  # Create empty file
        print(f"Created {USER_IDS_FILE}")

def is_user_tracked(user_id):
    """
    Check if user ID is already in the file
    Проверить, есть ли ID пользователя уже в файле
    
    Args:
        user_id: Telegram user ID
        user_id: ID пользователя Telegram
        
    Returns:
        bool: True if user is already tracked, False otherwise
        bool: True если пользователь уже отслеживается, False в противном случае
    """
    try:
        with open(USER_IDS_FILE, 'r', encoding='utf-8') as f:
            tracked_users = f.read().strip().split('\n')
            return str(user_id) in tracked_users
    except FileNotFoundError:
        return False

def add_user_to_file(user_id):
    """
    Add user ID to the tracking file
    Добавить ID пользователя в файл отслеживания
    
    Args:
        user_id: Telegram user ID
        user_id: ID пользователя Telegram
    """
    with open(USER_IDS_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{user_id}\n")
    print(f"Added user {user_id} to tracking file")

def register_user_tracker(bot: TeleBot):
    """
    Register the user tracking handler for all commands
    Зарегистрировать обработчик отслеживания пользователей для всех команд
    
    Args:
        bot: TeleBot instance
        bot: Экземпляр TeleBot
    """
    
    # Initialize the user file on startup
    # Инициализировать файл пользователей при запуске
    initialize_user_file()
    
    @bot.middleware_handler(update_types=['message'])
    def track_user_commands(bot_instance, message):
        """
        Middleware to track users who use any command
        Промежуточный обработчик для отслеживания пользователей, использующих любые команды
        """
        # Check if message contains a command (starts with '/')
        # Проверить, содержит ли сообщение команду (начинается с '/')
        if message.content_type == 'text' and message.text and message.text.startswith('/'):
            user_id = message.from_user.id
            
            # Check if user is already tracked
            # Проверить, отслеживается ли пользователь уже
            if not is_user_tracked(user_id):
                add_user_to_file(user_id)
                print(f"New user tracked: {user_id} (command: {message.text})")
            else:
                print(f"Existing user used command: {user_id} (command: {message.text})")