from aiogram import Router, types, F
from aiogram.filters import Command

from webApp.keyboard.inline_app import inline
from webApp.keyboard.inline_registration import inlines

router = Router()

@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.reply("Привет! Для регистрации необходимо получить контактный номер телефона и id телеграмм."
                        "Для этого нажми на кнопку ниже:", reply_markup=inlines())

@router.message(F.contact)
async def contact_received(message: types.Message):
    tg_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        await message.answer(f"Спасибо! Ваш номер телефона: {phone_number}, id телеграмм: {tg_id}",
                             reply_markup=types.ReplyKeyboardRemove())
        await message.answer("теперь нажмите на кнопку для перехода в приложение", reply_markup=inline())
    else:
        await message.answer("Вы не отправили номер телефона.")

