from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def inlines():
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="Поделится контактом", request_contact=True)
    )
    return builder.as_markup()
