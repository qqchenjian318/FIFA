import urllib
import urllib.request

from DataAnalysis import DataAnalysis


class DataCenter:

    def load_menu(self, basePath, matchPath):
        req = urllib.request.Request(basePath)
        data = urllib.request.urlopen(req).read()
        anal = DataAnalysis()
        anal.analysis_html(data)

