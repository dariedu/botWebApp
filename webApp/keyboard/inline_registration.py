from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def inlines():
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="Поделится контактом", request_contact=True),
        types.KeyboardButton(text="не делиться", request_contact=False),
    )
    return builder.as_markup(resize_keyboard=True)


def cmd_start():
    builder = ReplyKeyboardBuilder()
    url = "https://dariedufront.vercel.app"

    builder.add(
        types.KeyboardButton(text="Регистрация"),
        types.KeyboardButton(text="Вход", web_app=types.WebAppInfo(url=url)),
    )

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите действие",)
