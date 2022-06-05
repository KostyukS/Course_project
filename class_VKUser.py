class VKUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, tok, version, id_VK):
        self.token = tok
        self.version = version
        self.id_VK = id_VK

        self.params = {
            'access_token': tok,
            'v': version,
        }
        self.add_params = {
            'owner_id': id_VK,
            'count': '5',
            'album_id': 'profile',
            'extended': 1,
        }

    def item_json(self):
        url_photos_get = self.url + 'photos.get'
        res = requests.get(url_photos_get, params={**self.params, **self.add_params})
        req = res.json()['response']['items']
        return req

    def Check_False_True_profile(self):
        url_check = self.url + 'users.get'
        params = {
            'user_ids': self.id_VK,
            'access_token': self.token,
            'v': '5.131',
        }
        res = requests.get(url_check, params=params)
        res = res.json()['response'][0]['is_closed']
        return res



    def file_name(self, res):
        file_name = str(res.get('likes').get('count'))
        return file_name

    def file_date(self, res):
        file_date = datetime.fromtimestamp(res.get('date')).date().strftime("%d.%m.%Y")
        return file_date

    def image_url_max(self, res):
        sizes = {}
        for index, item in enumerate(res.get('sizes')):
            sizes[item.get('width')] = index
        target_width = max(list(sizes.keys()))
        url_max = res.get('sizes')[sizes.get(target_width)].get('url')
        return url_max

    def save_file_locally(self, file_name, url_max):
        res = requests.get(url_max, allow_redirects=True)
        local_file = open(file_name, 'wb')
        local_file.write(res.content)

    def delete_uploaded_file(self, file_name):
        os.remove(file_name)
