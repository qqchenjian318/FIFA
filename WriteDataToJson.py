import json
import platform

import os

os_path = '/Users/cocoon/PycharmProjects/data'
win_path = 'C:/Users/qqche_000/PycharmProjects/data'
class WriteDataToJson:

    def __init__(self,num):
        self.num = num

    def write_to_json(self,data):
        # 先从json文件中读取到数据 然后将数据添加到指定位置 然后再写入到json数据
        if platform.platform().startswith('Window'):
            file = win_path
        else:
            file = os_path
        file = file+'/'+'123.json'

        f = open(file, encoding='utf-8')
        datas = json.load(f)
        print(datas)
        with open(file, 'w') as f:
            json.dump(data, f)
