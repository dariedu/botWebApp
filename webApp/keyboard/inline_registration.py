from aiogram import types

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def inlines():
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="📞 Поделится контактом", request_contact=True),
        types.KeyboardButton(text="🚫не делиться", request_contact=False),
    )

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def cmd_start():
    builder = ReplyKeyboardBuilder()

    builder.add(
        types.KeyboardButton(text="📝Регистрация"),
        types.KeyboardButton(text="🔑Вход"),
    )

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите действие ⬇️ ⬇️ ⬇️",
                             one_time_keyboard=False)


def up(tg_id):
    url = f"https://dariedufront.vercel.app?tg_id={tg_id}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="🍞 dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()
