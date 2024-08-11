from aiogram import Router, types
from aiogram.filters import Command
from webApp.keyboard.inline_app import inline


router = Router()

@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.reply("Hello!", reply_markup=inline())
