import requests


class YaUploader:
    def __init__(self, tok: str):
        self.token = tok

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': 'Folder_Photos_VK'}
        requests.put(url, headers=headers, params=params)

    def get_upload_link(self, filename):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': f'Folder_Photos_VK/{filename}', 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, filename):
        href = self.get_upload_link(filename=filename).get('href', '')
        requests.put(href, data=open(filename, 'rb'))
        return

    def upload(self, filename):
        self.create_folder()
        self.get_upload_link(filename=filename)
        self.upload_file_to_disk(filename=filename)
        return 1


if __name__ == '__main__':
    file = 'example.txt'
    token = 'AQAAAAATeViuAADLWyqJ3Qq4ykievdqZkK0qGd4'
    uploader = YaUploader(token)
    result = uploader.upload(file)
