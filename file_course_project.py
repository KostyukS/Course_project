from datetime import datetime
import requests
import class_YaUploader
import os
import json
import class_VKUser




if __name__ == '__main__':
    token_YAdisk = ''
    token_VK = ''
    version = '5.131'
    id_VK = ''

    target = class_VKUser.VKUser(token_VK, version, id_VK)
    if len(target.Check_resp()) == 0:
        print(f'\nid_VK = {id_VK},  ==No profile information==')
    else:
        if target.Check_False_True_profile() == False:
            req = target.item_json()
            max_progress = len(req)
            uploaded_files = []
            json_file_data = []
            yandex_api = class_YaUploader.YaUploader(token_YAdisk)
            print('Download start:')
            for index, item in enumerate(req, 1):
                file_name = target.file_name(item)
                date = target.file_date(item)
                image_url = target.image_url_max(item)
                if file_name in uploaded_files:
                    file_name = '{}_{}'.format(file_name, date)
                target.save_file_locally(file_name, image_url)
                yandex_api.upload(file_name)
                json_file_data.append({
                    'file_name': file_name,
                    'size': os.path.getsize(file_name),
                })
                target.delete_uploaded_file(file_name)
                uploaded_files.append(file_name)
                print('{} step from {} steps'.format(index, max_progress))

            open('result.json', 'w').write(json.dumps(json_file_data, indent=4, sort_keys=True))

            print('Download is done')
            print('\nDownloaded {} images'.format(max_progress))

        elif target.Check_Del_Profile() == 'deleted':
            print(f'\nid_VK = {id_VK},  ==This profile has been deleted==')
        else:
            print(f'\nid_VK = {id_VK},  ==This profile is private==')
