import requests


class YaFolder:
    url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}',
            'Accept': 'application/json'
         }

    def create_folder(self, fldr_name: str):
        params_folder = {'path': f'{fldr_name}'}
        headers = self.get_headers()
        create_folder_url = f'{self.url}resources'
        response = requests.put(create_folder_url, params=params_folder, headers=headers)
        return response.status_code

    def delete_folder(self, fldr_name: str):
        params_folder = {'path': f'{fldr_name}'}
        headers = self.get_headers()
        del_folder_url = f'{self.url}resources'
        response = requests.delete(del_folder_url, params=params_folder, headers=headers)
        return response.status_code
