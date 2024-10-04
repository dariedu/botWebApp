from aiogram import Router, types, F
from aiogram.filters import Command

from webApp.keyboard.inline_app import inline
from webApp.keyboard.inline_registration import inlines

router = Router()

@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.reply("Для регистрации вам необходимо поделиться с приложением своим номером телефона",
                        reply_markup=inlines())

@router.message(F.contact)
async def contact_received(message: types.Message):
    tg_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        await message.answer(f"Спасибо!", reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Теперь нажмите на кнопку для перехода в приложение", reply_markup=inline())

@router.message(F.text == 'не делиться')
async def text_received(message: types.Message):
    if message.text == 'не делиться':
        await message.answer("регистрация не возможна")
