from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline(tg_id, tg_nickname, phone_number):
    url = f"https://ваш_адрес_приложения?phone_number={phone_number}&tg_id={tg_id}&tg_nickname={tg_nickname}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()


def inline_app(tg_id, tg_nickname):
    url = f"https://ваш_адрес_приложения?tg_id={tg_id}&tg_nickname={tg_nickname}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()
