import json

from bs4 import BeautifulSoup

from FileDownload import FileDownload
from bs4 import BeautifulSoup
import time

from GamblingData import GamblingData
from WriteDataToJson import WriteDataToJson


class DataAnalysis:

    def analysis_html(self, by, times):
        # print(by)
        bs = BeautifulSoup(by, 'html.parser', from_encoding='utf-8')

        li = bs.find_all('tr')
        for node in li:
            num = node.get('match')
            if num is not None:
                if num is not None and num.startswith('148'):
                    print('%s  状态  %s' % (num, node.get('mtime')))

                    # print(node)
                    n = node.find_all('span')
                    li = []
                    for i in n:
                        a = i.find_all('a')
                        if len(a) > 0:
                            if '世界杯' != a[0].text:
                                print(a[0].text)
                                li.append(a[0].text)

                    download = FileDownload()
                    if len(li) > 1:
                        v = li[0] + '_vs_' + li[1] + '.xls'
                    else:
                        v = 'download_file.xls'

                    download.download(num, v, times)
                    break

    def analysis_data(self, num,index):
        # 从file中读取出来的数据 然后进行解析成可以绘制的数据
        # 然后进行返回
        reader = WriteDataToJson(num)
        datas = reader.read_from_json()
        if datas == -1:
            print(' 没有读取到数据')
        else:
            result_data = []
            times = []
            start_zhu = []
            start_pan = []
            start_ke = []

            new_zhu = []
            new_pan = []
            new_ke = []
            data = datas[0]
            print('打印出来的哈哈哈  %s ' % data)
            print(data.get('time'))
            start_time = data.get('time')
            li = data.get('data')
            print(li)
            js = json.loads(li)
            print(js)
            gambing = js[index]

            print(gambing)
            start_z = gambing[1]
            start_p = gambing[2]
            start_k = gambing[3]
            for da in datas:
                time = da.get('time')
                times.append(time - start_time)
                start_zhu.append(start_z)
                start_pan.append(start_p)
                start_ke.append(start_k)

                dat = da.get('data')
                new_zhu.append(dat[4])
                new_pan.append(dat[5])
                new_ke.append(dat[6])

            result_data.append(times)
            result_data.append(new_zhu)
            result_data.append(new_pan)
            result_data.append(new_ke)
            result_data.append(start_z)
            result_data.append(start_p)
            result_data.append(start_k)
            return result_data


