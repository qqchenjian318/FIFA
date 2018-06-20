from bs4 import BeautifulSoup

from FileDownload import FileDownload
from bs4 import BeautifulSoup


class DataAnalysis:

    def analysis_html(self, by):
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
                                print (a[0].text)
                                li.append(a[0].text)

                    download = FileDownload()
                    v = ''
                    if len(li) > 1:
                        v = li[0] +'_vs_'+li[1]+'.xls'
                    else:
                        v = 'download_file.xls'

                    download.download(num, v)
                    break


        # print(li)
