from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start", description="Старт"
        ),
        BotCommand(
            command='update_phone_number', description='Обновить номер телефона'
        )
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
