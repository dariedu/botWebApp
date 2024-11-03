import json
from pprint import pprint
from aiogram import Bot, Router, types
import re

from webApp.handlers.request_django import send_refuse_task, send_refuse_delivery, send_refuse_promotion, get_task_name, \
    post_promo_is_active, send_accept_task

router_task = Router()


@router_task.callback_query()
async def handling_task_call(call: types.CallbackQuery, bot: Bot):
    if call.data == 'accept_task':
        data_str = call.data.split(':', 1)[1]
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return
        task_id = data['task_id']
        tg_id = call.from_user.id
        send_accept_task(task_id, tg_id)
        await call.message.edit_text("Подтверждено")
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
        tg_id = call.from_user.id
        pprint(tg_id)
        task_id = data['task_id']
        task_name = get_task_name(task_id, tg_id)
        await call.message.edit_text("Отклонено")
        await bot.send_message(curator_id, f"Волонтер {user_nickname} отказался от Доброго дела '{task_name}'")
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
        tg_id = call.from_user.id
        delivery_id = data['delivery_id']
        await call.message.edit_text("Отклонено")
        pattern = r'Подтвердите участие в Благотворительной доставке (\d{2}\.\d{2}\.\d{4}) в (\d{2}:\d{2})!'
        match = re.search(pattern, call.message.text)
        if match:
            date_str = match.group(1)
            time_str = match.group(2)
        await bot.send_message(curator_id, f"Волонтёр {user_nickname} "
                                           f"отказался от Благотворительной доставки {date_str} в {time_str}")
        send_refuse_delivery(delivery_id, tg_id)
    elif call.data.startswith('accept_promotion'):
        data_str = call.data.split(':', 1)[1]
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return
        await call.message.edit_text("Подтверждено")
        tg_id = call.from_user.id
        promotion_id = data['promotion_id']
        post_promo_is_active(promotion_id, tg_id)
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
