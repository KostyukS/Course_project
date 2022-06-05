from datetime import datetime
import requests
import file_course_project
import os
import json
import class_YaUploader




if __name__ == '__main__':
    token_YAdisk = 'AQAAAAATeViuAADLWyqJ3Qq4ykievdqZkK0qGd4'
    token_VK = '38e6e9688c1e1e758bce2428e15f910a662863791d8d803a406694c5f7456f4a40c18ee3c546760c480bb'
    version = '5.131'
    id_VK = '569523'

    target = class_VKUser.VKUser(token_VK, version, id_VK)
    if target.Check_False_True_profile() == False:
        req = target.item_json()
        max_progress = len(req)
        uploaded_files = []
        json_file_data = []
        yandex_api = file_course_project.YaUploader(token_YAdisk)
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
    else:
        print(f'id_VK = {id_VK},  ==This profile is private==')