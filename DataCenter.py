import urllib
import urllib.request

import time

from DataAnalysis import DataAnalysis


class DataCenter:

    def load_menu(self, basePath, matchPath):
        req = urllib.request.Request(basePath)
        data = urllib.request.urlopen(req).read()
        anal = DataAnalysis()
        int(time.time())
        anal.analysis_html(data,int(time.time()))

