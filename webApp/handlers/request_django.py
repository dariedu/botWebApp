from pprint import pprint
import requests


url_token = f"https://skillfactory.dariedu.site/api/token/"

def send_refuse_delivery(delivery_id, tg_id):
    url = f"https://skillfactory.dariedu.site/api/deliveries/{delivery_id}/cancel/"

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        requests.post(url, headers={'Authorization': f'Bearer {token}'},
                      json={"volunteer_tg_id": tg_id}).json()
    else:
        print("Токен не получен")


def send_refuse_task(task_id, tg_id):
    url = f"https://skillfactory.dariedu.site/api/tasks/{task_id}/refuse//"

    response = requests.post(url_token, json={"tg_id": tg_id})
    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        requests.post(url, headers={'Authorization': f'Bearer {token}'},
                      json={"volunteer_tg_id": tg_id}).json()
    else:
        print("Токен не получен")


def send_refuse_promotion(promotion_id, tg_id):
    url = f"https://skillfactory.dariedu.site/api/promotions/{promotion_id}/cancel/"
    url_notification = f"https://skillfactory.dariedu.site/api/notifications/"

    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        title = 'Отказ от записи поощрения'
        request_notification = requests.post(url_notification, headers={'Authorization': f'Bearer {token}'},
                                             json={
                                                 'promotion_id': promotion_id,
                                                 'title': title
                                             }).json()
        if request_notification:
            requests.post(url, headers={'Authorization': f'Bearer {token}'},
                          json={"volunteer_tg_id": tg_id}).json()
    else:
        print("Токен не получен")


def get_task_name(task_id, tg_id):
    url = f"https://skillfactory.dariedu.site/api/tasks/my/"
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        pprint(token)

        request = requests.get(url, headers={'Authorization': f'Bearer {token}'}).json()
        pprint(request)
        if request:
            for task in request:
                if task['id'] == task_id:
                    return task['name']
    else:
        print("Токен не получен")


def get_user_request(tg_id):
    response = requests.post(url_token, json={"tg_id": tg_id})

    if response.status_code == 200:
        return True

    return False

def post_promo_is_active(promotion_id, tg_id):
    url = f"http://127.0.0.1:8000/api/participation/"

    response = requests.post(url_token, json={"tg_id": tg_id})
    print(response.status_code)

    if response.status_code == 200 and 'access' in response.json():
        token = response.json()['access']
        is_active = True
        posts = requests.post(url, headers={'Authorization': f'Bearer {token}'},
                              json={"user": tg_id, "promotion": promotion_id, "is_active": is_active}).json()
        if posts == 200:
            return True
    else:
        print(response.json())
        return response.status_code
