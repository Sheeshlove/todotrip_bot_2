@echo off
REM Batch file to run ToDoTrip bot
REM Батник для запуска бота ToDoTrip

echo Starting ToDoTrip bot... (Запуск бота ToDoTrip...)

REM Activate virtual environment and run bot
REM Активация виртуального окружения и запуск бота
call "%~dp0.venv\Scripts\activate.bat" && python "%~dp0main.py"

REM Keep window open if there's an error
REM Оставить окно открытым в случае ошибки
if errorlevel 1 (
    echo.
    echo An error occurred! (Произошла ошибка!)
    echo Press any key to exit... (Нажмите любую клавишу для выхода...)
    pause
) 