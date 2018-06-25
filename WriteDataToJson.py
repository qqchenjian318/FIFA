import json
import platform

import os

from GamblingData import GamblingData

os_path = '/Users/cocoon/PycharmProjects/data'
win_path = 'C:/Users/qqche_000/PycharmProjects/data'


class WriteDataToJson:
    def __init__(self, num, time=None):
        self.time = time
        self.num = num

    def write_to_json(self, data):
        # 先从json文件中读取到数据 然后将数据添加到指定位置 然后再写入到json数据
        if platform.platform().startswith('Window'):
            file = win_path
        else:
            file = os_path

        # 根据比赛num 读取到对应比赛的所有数据
        file = file + '/' + self.num + '.json'
        folder = os.path.exists(file)
        if not folder:
            # 先写一个文件
            open(file, 'w')

        if os.path.getsize(file) == 0:
            #说明文件还没有数据  那么
            new_data = []
            s = json.dumps(data)

            gambling = GamblingData(self.time, s)
            st = gambling.obj_2_json()

            # j = json.dumps(gambling, default=gambling.obj_2_json())
            new_data.append(st)
            print(new_data)
            with open(file, 'w') as f:
                json.dump(new_data, f)
        else:
            f = open(file, 'r', encoding='utf-8')
            datas = json.load(f)
            s = json.dumps(data)
            gambling = GamblingData(self.time, s)
            st = gambling.obj_2_json()
            datas.append(st)
            print(datas)
            with open(file, 'w') as f:
                json.dump(datas, f)

    def read_from_json(self):
        # 从指定文件中读取出数据 进行返回
        if platform.platform().startswith('Window'):
            file = win_path
        else:
            file = os_path
        file = file + '/' + self.num + '.json'
        folder = os.path.exists(file)
        if not folder:
            #没有数据
            return -1
        f = open(file, 'r', encoding='utf-8')
        datas = json.load(f)
        print(datas)
        return datas
