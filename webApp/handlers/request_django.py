from pprint import pprint
import requests


def send_refuse_delivery(delivery_id, tg_id):
    url = f"http://127.0.0.1:8000//api/deliveries/{delivery_id}/cancel/"
    url_token = f"http://127.0.0.1:8000/api/token/"

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)
        request = requests.post(url, headers={'Authorization': f'Bearer {token}'},
                                json={"volunteer_tg_id": tg_id}).json()
        pprint(request)
    else:
        print("Токен не получен")


def send_refuse_task(task_id, tg_id):
    url = f"http://127.0.0.1:8000/api/tasks/{task_id}/refuse//"
    url_token = f"http://127.0.0.1:8000/api/token/"

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)
        request = requests.post(url, headers={'Authorization': f'Bearer {token}'},
                                json={"volunteer_tg_id": tg_id}).json()
        pprint(request)
    else:
        print("Токен не получен")


def send_refuse_promotion(promotion_id, tg_id):
    url = f"http://127.0.0.1:8000/api/promotions/{promotion_id}/cancel/"
    url_token = f"http://127.0.0.1:8000/api/token/"
    url_notification = f"http://127.0.0.1:8000/api/notifications/"

    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)
        title = 'Отмена использования поощрения'
        request_notification = requests.post(url_notification, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'promotion_id': promotion_id,
                                                 'title': title
                                             }).json()
        pprint(request_notification)
        if request_notification:
            request = requests.post(url, headers={'Authorization': f'Bearer {token}'},
                                    json={"volunteer_tg_id": tg_id}).json()
            pprint(request)
    else:
        print("Токен не получен")


def get_task_name(task_id, tg_id):
    url_token = f"http://127.0.0.1:8000/api/token/"
    url = f"http://127.0.0.1:8000/api/tasks/my/"
    response = requests.post(url_token, json={"tg_id": tg_id})
    # request = requests.get(url).json()
    # pprint(request)

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)

        request = requests.get(url, headers={'Authorization': f'Bearer {token}'}).json()
        pprint(request)
        if request:
            for task in request:
                if task['id'] == task_id:
                    return task['name']
                print(task['id'])
                print(task['name'])
    else:
        print("Токен не получен")
