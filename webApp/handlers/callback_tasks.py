import json
from pprint import pprint
from aiogram import Bot, Router, types

from webApp.handlers.request_django import send_refuse_task, send_refuse_delivery, send_refuse_promotion

router_task = Router()


@router_task.callback_query()
async def handling_task_call(call: types.CallbackQuery, bot: Bot):
    if call.data == 'accept_task':
        await call.message.edit_text("Подтверждено task")
    elif call.data.startswith('refuse_task'):
        data_str = call.data.split(':', 1)[1]
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return
        pprint(data)
        curator_id = data['curator_tg_id']
        user_nickname = f"@{call.from_user.username}"
        tg_id = data['volunteer_tg_id']
        task_id = data['task_id']
        await call.message.edit_text("Отклонено")
        await bot.send_message(curator_id, f"Пользователь {user_nickname} отклонил задачу {task_id}")
        send_refuse_task(task_id, tg_id)
    elif call.data == 'accept_delivery':
        await call.message.edit_text("Подтверждено")
    elif call.data.startswith('refuse_delivery'):
        data_str = call.data.split(':', 1)[1]
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return
        pprint(data)
        curator_id = data['curator_tg_id']
        user_nickname = f"@{call.from_user.username}"
        tg_id = data['volunteer_tg_id']
        delivery_id = data['delivery_id']
        await call.message.edit_text("Отклонено")
        await bot.send_message(curator_id, f"Пользователь {user_nickname} отклонил участие в доставке ")
        send_refuse_delivery(delivery_id, tg_id)
    elif call.data == 'accept_promotion':
        await call.message.edit_text("Подтверждено")
    elif call.data.startswith('refuse_promotion'):
        data_str = call.data.split(':', 1)[1]
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return
        pprint(data)
        tg_id = call.from_user.id
        promotion_id = data['promotion_id']
        await call.message.edit_text("Отклонено")
        send_refuse_promotion(promotion_id, tg_id)
