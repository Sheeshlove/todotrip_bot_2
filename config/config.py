"""
Configuration settings for the ToDoTrip Telegram bot
Настройки конфигурации для Telegram бота ToDoTrip
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot token from @BotFather (use environment variable for security)
# Токен бота, полученный от @BotFather (используйте переменную окружения для безопасности)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Channel ID for forwarding messages
# ID канала для пересылки сообщений
FORWARD_CHANNEL_ID = "-1002477474060"

# Website URL
# URL веб-сайта
WEBSITE_URL = "https://todotrip.pro/"

# Support contact
# Контакт поддержки
SUPPORT_CONTACT = "@insendro"