import asyncio
from aiogram import Bot, Dispatcher
import logging
from data.config import config_settings
from utils.commands import set_commands
from webApp.handlers.start_handler import router


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config_settings.ADMIN_ID, "Бот запущен")

async def stop_bot(bot: Bot):
    await bot.send_message(config_settings.ADMIN_ID, "Бот остановлен")

async def start():

    bot = Bot(token=config_settings.BOT_TOKEN.get_secret_value())

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        dp.include_router(router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"An error occurred during bot polling: {e}")
        await bot.send_message(config_settings.ADMIN_ID, f"An error occurred during bot polling: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        loop.close()
