from urllib.request import urlretrieve

import os
import ReadDataFromXls

match_path = 'http://odds.cp.360.cn/jczqdatax/asiaload?cids=&ctype=&match='
os_path = '/Users/cocoon/PycharmProjects/down'
window_path = ''

class FileDownload:

    def download(self,url,fileName):
        local = os.path.join(os_path, fileName)

        print(match_path+url)
        urlretrieve(match_path+url,local)
        reader = ReadDataFromXls(local)

        dicts = reader.get_dict(0,0,1)