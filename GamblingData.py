# 每个赌场的数据bean 包括赌场名 和每个时间的赔率bean
class GamblingData:
    def __init__(self, name, data):
        self.time = name
        self.data = data

    def obj_2_json(self):
        return {'time': self.time, 'data': self.data}
