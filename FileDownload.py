import platform
from urllib.request import urlretrieve

import os

from ReadDataFromXls import ReadDataFromXls
from WriteDataToJson import WriteDataToJson

match_path = 'http://odds.cp.360.cn/jczqdatax/asiaload?cids=&ctype=&match='
os_path = '/Users/cocoon/PycharmProjects/down'
window_path = 'C:/Users/qqche_000/PycharmProjects/download'


class FileDownload:
    def download(self, url, fileName):
        print(platform.platform())
        if platform.platform().startswith('Window'):
            file = window_path
        else:
            file = os_path

        local = os.path.join(file, fileName)

        print(match_path + url)
        urlretrieve(match_path + url, local)
        reader = ReadDataFromXls(local)

        # dicts = reader.get_dict(0, 0, 1)
        di = reader.get_dict(0)
        print(di)
        writer = WriteDataToJson('123456')
        writer.write_to_json(di)
