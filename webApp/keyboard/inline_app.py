from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline(tg_id, tg_nickname, phone_number):
    url = f"https://dariedufront.vercel.app?phone_number={phone_number}&tg_id={tg_id}&tg_nickname={tg_nickname}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()
