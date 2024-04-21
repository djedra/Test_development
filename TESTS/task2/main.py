import requests


class YandexDisk:
    def __init__(self, token_yandex: str) -> None:
        self.token = token_yandex

    def create_folder(self, path: str) -> int:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'

        params = {
            'path': path
        }
        headers = {
            'Authorization': self.token
        }

        res = requests.put(url, headers=headers, params=params)

        return res.status_code

    def delete_file_folder(self, path: str) -> int:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'

        params = {
            'path': path
        }
        headers = {
            'Authorization': self.token
        }

        res = requests.delete(url, headers=headers, params=params)

        return res.status_code

    def file_list_last_uploaded(self) -> requests.Response:
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'

        headers = {
            'Authorization': self.token
        }

        res = requests.get(url, headers=headers)

        return res

    def file_folder_metainfo(self, path: str) -> requests.Response:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'

        params = {
            'path': path
        }
        headers = {
            'Authorization': self.token
        }

        res = requests.get(url, headers=headers, params=params)

        return res