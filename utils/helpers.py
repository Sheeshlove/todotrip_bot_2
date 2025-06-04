"""
Utility functions for the ToDoTrip Telegram bot
Вспомогательные функции для Telegram бота ToDoTrip
"""

def get_user_name(message):
    """
    Get user's first name or return default value
    Получить имя пользователя или вернуть значение по умолчанию
    
    Args:
        message: Telegram message object
        message: Объект сообщения Telegram
        
    Returns:
        str: User's first name or 'друг' if not available
        str: Имя пользователя или 'друг', если недоступно
    """
    first_name = message.from_user.first_name or ""
    return first_name if first_name else "друг" 