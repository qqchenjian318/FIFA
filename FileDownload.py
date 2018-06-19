from urllib.request import urlretrieve

import os

match_path = 'http://odds.cp.360.cn/jczqdatax/asiaload?cids=&ctype=&match='

class FileDownload:

    def download(self,url,fileName):
        local = os.path.join('C:/Users/qqche_000/Downloads', fileName)
        print(match_path+url)
        urlretrieve(match_path+url,local)