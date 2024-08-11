from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline():
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="dari edu", web_app=types.WebAppInfo
                (url="https://github.com/dariedu")))

    return builder.as_markup()
