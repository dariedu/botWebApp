from aiogram import Router, types, F
from aiogram.filters import Command

from webApp.handlers.request_django import get_user_request
from webApp.keyboard.inline_app import inline
from webApp.keyboard.inline_registration import inlines, cmd_start

router = Router()

@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.reply("Пройдите регистрацию, либо зайдите в приложение!", reply_markup=cmd_start())


@router.message(F.text == '📝Регистрация')
async def text_received(message: types.Message):
    if message.text == '📝Регистрация':
        responses = get_user_request(tg_id=message.from_user.id)
        if responses:
            await message.answer("Вы уже зарегистрированы")
        else:
            await message.answer("Для регистрации вам необходимо поделиться с приложением своим номером телефона",
                                 reply_markup=inlines())
    # if message.text == 'Изменить номер телефона':
    #     await message.answer("Изменить номер телефона")

@router.message(F.contact)
async def contact_received(message: types.Message):
    tg_id = message.from_user.id
    tg_nickname = f"@{message.from_user.username}"
    if message.contact:
        phone_number = message.contact.phone_number
        await message.answer(f"Спасибо!", reply_markup=cmd_start())
        await message.answer("Теперь нажмите на кнопку для перехода в приложение",
                             reply_markup=inline(tg_id, tg_nickname, phone_number))

@router.message(F.text == '🚫не делиться')
async def text_received(message: types.Message):
    if message.text == '🚫не делиться':
        await message.answer("регистрация не возможна")
