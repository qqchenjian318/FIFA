from bs4 import BeautifulSoup

from FileDownload import FileDownload


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
                    download = FileDownload()
                    download.download(num,'download_file')
                    break

        # print(li)
