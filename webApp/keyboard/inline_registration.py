from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from data.config import config_settings

APP_URL = config_settings.APP_URL

def inlines():
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="📞 Поделиться контактом", request_contact=True),
        types.KeyboardButton(text="🚫Не делиться", request_contact=False),
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
    url = f"{APP_URL}?tg_id={tg_id}"
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="🍞 dari edu", web_app=types.WebAppInfo
                (url=url)))

    return builder.as_markup()


def update_phone():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Нажмите кнопку ⬇️ ⬇️ ⬇️",)
