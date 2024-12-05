from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.config import config_settings

APP_URL = config_settings.APP_URL


def inline(tg_id, tg_nickname, phone_number):
    url = f"{APP_URL}?phone_number={phone_number}&tg_id={tg_id}&tg_nickname={tg_nickname}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="🍞 dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()
