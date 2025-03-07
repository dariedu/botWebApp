from pprint import pprint
import requests

from data.url import *


def send_refuse_delivery(delivery_id, tg_id):
    url = f"{url_deliveries}/{delivery_id}/cancel/"

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        cancel_response = requests.post(url, headers={'Authorization': f'Bearer {token}'},
                                        json={"volunteer_tg_id": tg_id})
        if cancel_response.status_code != 200:
            return cancel_response.status_code

    else:
        return response.status_code


def send_refuse_task(task_id, tg_id):
    url = f"{url_tasks}/{task_id}/refuse/"
    print('url', url)

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        requests.post(url, headers={'Authorization': f'Bearer {token}'},
                      json={"volunteer_tg_id": tg_id}).json()
        title = 'Отказ от записи на Доброе дело'
        action_type = 'cancel'
        request_notification = requests.post(url_notifications, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'task_id': task_id,
                                                 'title': title,
                                                 'action_type': action_type
                                             }).json()
        if request_notification:
            return response.status_code
    else:
        return response.status_code

def send_accept_task(task_id, tg_id):
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        print('token', token)
        title = 'Подтверждение записи на Доброе дело'
        action_type = 'confirm'
        request_notification = requests.post(url_notifications, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'task_id': task_id,
                                                 'title': title,
                                                 'action_type': action_type
                                             }).json()
        if request_notification:
            pprint(request_notification)
            return response.status_code
    else:
        return response.status_code


def send_refuse_promotion(promotion_id, tg_id):
    url = f"{url_promotions}/{promotion_id}/cancel/"
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        title = 'Отказ от записи поощрения'
        action_type = 'cancel'
        request_notification = requests.post(url_notifications, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'promotion_id': promotion_id,
                                                 'title': title,
                                                 'action_type': action_type
                                             }).json()
        if request_notification:
            requests.post(url, headers={'Authorization': f'Bearer {token}'},
                          json={"volunteer_tg_id": tg_id}).json()
    else:
        return response.status_code


def get_task_name(task_id, tg_id):
    url = f"{url_tasks}/my/"
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)

        request = requests.get(url, headers={'Authorization': f'Bearer {token}'})

        if request.status_code == 200:
            try:
                data = request.json()
                pprint(data)
                for task in data:
                    if task['id'] == task_id:
                        pprint(task['id'])
                        name = task['name']
                        print('NAME', name)
                        return name
            except ValueError:
                print("Ошибка декодирования JSON:", request.text)
        else:
            print(f"Ошибка при получении задач: {request.status_code} - {request.text}")
    else:
        return print(f"Ошибка при получении токена: {response.status_code} - {response.text}")

    return None


def get_user_request(tg_id):
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200:
        return True

    return False

def post_promo_is_active(promotion_id, tg_id):
    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        is_active = True
        posts = requests.post(url_participation, headers={'Authorization': f'Bearer {token}'},
                              json={"tg_id": tg_id, "promotion_id": promotion_id, "is_active": is_active})

        if posts.status_code != 200:
            return posts.status_code

        action_type = 'confirm'
        title = 'Подтверждение записи поощрения'
        request_notification = requests.post(url_notifications, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'promotion_id': promotion_id,
                                                 'title': title,
                                                 'action_type': action_type
                                             })
        if request_notification.status_code == 200:
            return 200
        else:
            return request_notification.status_code
    else:
        return response.status_code


def update_phone_numbers(tg_id, phone_number):
    url_id = f"{url_users}?tg_id={tg_id}"
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        user_response = requests.get(url_id, headers={'Authorization': f'Bearer {token}'}).json()

        if user_response:
            for user_data in user_response:
                pk = user_data.get('id')
                if pk:
                    update_url = f"{url_users}{pk}/update_phone/"
                    update_response = requests.post(update_url, headers={'Authorization': f'Bearer {token}'},
                                                     json={"phone": phone_number})

                    if update_response.status_code == 200:
                        return True
                    else:
                        print("Не удалось обновить номер телефона.:", update_response.status_code, update_response.text)
                        return False
        else:
            print("Не удалось получить данные пользователя.:", user_response)
            return False
    else:
        print("Не удалось получить токен доступа или неверный ответ.:", response.status_code, response.text)
        return False
