import requests
from pprint import pprint

class Ya_api:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_name):
        reference = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            "path": folder_name,
        }
        resp = requests.put(reference, headers=self.get_header(), params=params)
        if resp.status_code == 201:
            print(f'Папка {folder_name} создана')
        elif resp.status_code == 409:
            print(f'Папка {folder_name} уже существует')
        return resp.status_code

    def delete_folder(self, folder_name):
        reference = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            "path": folder_name,
        }
        resp = requests.delete(reference, headers=self.get_header(), params=params)
        if resp.status_code == 204:
            print(f'Папка {folder_name} удалена')
        elif resp.status_code == 404:
            print(f'Папка {folder_name} не существует')
        print(resp.status_code)


if __name__ == "__main__":
    with open('ya_token.txt') as token:
        ya_token = token.read()
    cur = Ya_api(ya_token)
    cur.create_folder("new")

    cur.delete_folder("new")