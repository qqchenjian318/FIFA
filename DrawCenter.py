import numpy
import matplotlib.pyplot as plt


class DrawCenter:

    def drawSimple(self, data):
        # 拿到了datas 需要绘制多条曲线
        # x是x轴的基准线 a b c 是主 盘 客 三条初始盘口
        # x y z 是线路变化趋势
        # data 是经过处理的数据  多个数组的集合
        # 0 集合 是时间的集合 也就是 x
        # 1 是初始 主 red 虚线
        # 2 是初始 盘 black 虚线
        # 3 是初始 客 yellow 虚线
        # 4 是变化 主 r  实线
        # 5 是变化 盘 b  实线
        # 6 是变化 客 c  实线
        print('要绘制的 data  %s ' % data)
        times = data.get(0)
        a = data.get(1)
        b = data.get(1)
        c = data.get(2)

        x = data.get(4)
        y = data.get(5)
        z = data.get(6)

        plt.figure()
        plt.plot(times, a, color='red', linestyle='dashed')
        plt.plot(times, b, color='black', linestyle='dashed')
        plt.plot(times, c, color='yellow', linestyle='dashed')

        plt.plot(times, x, color='red', linestyle='solid')
        plt.plot(times, y, color='black', linestyle='solid')
        plt.plot(times, z, color='yellow', linestyle='solid')

        plt.xlabel('time(s)')
        plt.ylabel('value(m)')
        plt.title(' a simple plot ')
        plt.show()
