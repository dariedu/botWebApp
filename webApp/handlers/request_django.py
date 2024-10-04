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


# if __name__ == '__main__':
#     send_refuse_delivery(),
