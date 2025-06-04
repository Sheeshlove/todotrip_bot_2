# ToDoTrip Telegram Bot

Telegram бот для проекта ToDoTrip, предоставляющий информацию о поездках в Дагестан.

## Установка / Installation

1. Клонируйте репозиторий / Clone the repository:
```bash
git clone <repository-url>
cd todotrip_bot
```

2. Создайте виртуальное окружение / Create a virtual environment:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение / Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Установите зависимости / Install dependencies:
```bash
pip install -r requirements.txt
```

## Конфигурация / Configuration

1. Получите токен бота у @BotFather в Telegram
2. Отредактируйте файл `config/config.py` и вставьте ваш токен
3. При необходимости настройте другие параметры в `config/config.py`

## Запуск / Running

```bash
python main.py
```

## Структура проекта / Project Structure

```
todotrip_bot/
├── config/
│   └── config.py          # Конфигурация бота / Bot configuration
├── handlers/
│   ├── __init__.py
│   ├── start_handler.py   # Обработчик /start / Start command handler
│   ├── help_handler.py    # Обработчик /help / Help command handler
│   ├── info_handler.py    # Обработчик /info / Info command handler
│   ├── site_handler.py    # Обработчик /site / Site command handler
│   ├── dagestan_handler.py # Обработчик /dagestan / Dagestan command handler
│   ├── contact_handler.py # Обработчик /contact / Contact command handler
│   └── message_handler.py # Обработчик общих сообщений / General message handler
├── utils/
│   ├── __init__.py
│   └── helpers.py         # Вспомогательные функции / Helper functions
├── main.py               # Точка входа / Entry point
├── requirements.txt      # Зависимости / Dependencies
└── README.md            # Документация / Documentation
```

## Команды бота / Bot Commands

- `/start` - Начало работы с ботом / Start working with the bot
- `/help` - Список всех команд / List of all commands
- `/info` - Информация о ToDoTrip / Information about ToDoTrip
- `/site` - Переход на веб-сайт / Go to website
- `/dagestan` - Вопросы по Дагестану / Questions about Dagestan
- `/contact` - Связаться с поддержкой / Contact support 