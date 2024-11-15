from aiogram.fsm.state import StatesGroup, State


class StateNumberPhone(StatesGroup):
    phone_number = State()
    update_phone = State()
    start_state = State()
