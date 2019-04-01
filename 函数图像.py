from math import *
import numpy as np
import time
import matplotlib.pyplot as plt
from tkinter import *
#import threading
#import random
def pot():
    import matplotlib.pyplot as plt
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    a = ''

    def tu0(a, g, mi, mx):
        if len(a) < 1:
            with open('fun.txt') as f:
                a = f.read()

        def ys(x):
            x = x
            return eval(a)

        xmin = float(mi)
        xmax = float(mx)
        weth = (xmax - xmin) / 1000
        xi = []
        xi = np.arange(xmin, xmax, weth)
        # for i in xz:
        #    xi.append(i)
        xii = []
        j = 0

        while True:
            if xi[j] == xi[-1]:
                break
            try:
                n = ys(xi[j])
                xii.append(xi[j])
                j = j + 1
            except:
                j = j + 1
                continue
        # print(weth)
        del xii[0]

        xn = []
        xnn = []
        for x in xii:
            i = round((ys(x) - ys(x - weth)) / weth, 3)

            if abs(i) < 500:
                xn.append(x)
            else:
                xnn.append(xn)
                xn = []
        xnn.append(xn)
        xn = []
        yn = []
        ynn = []
        for i in xnn:
            if len(i) > 0:
                xn.append(i)
        for i in xn:
            for m in i:
                ynn.append(ys(m))
            yn.append(ynn)
            ynn = []
        j = 0
        ym = []
        for i in xn:
            ym = yn[j] + ym
            j = j + 1
        j=0
        for i in xn:
            plt.plot(i, yn[j], '-', color=g,label='y='+a)
            plt.legend()
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(u'函数图像')
            #ym = yn[j] + ym
            j = j + 1
        plt.plot([xmin, xmax], [0, 0], '-.', color='green')
        plt.plot([0, 0], [min(ym), max(ym)], '-.', color='green')
        # plt.show()

    def tu():

        rs = 0
        rgb = ['red', 'dodgerblue', 'darkorange', 'y', 'deeppink']
        a = l.get(0.0, 'end')
        al = a.replace('\n', "#").split('#')
        del al[-1]

        for i in al:
            # print(len(i),i)
            if rs == 5:
                rs = 0

            g = rgb[rs]
            # print(tmi.get(0.0,'end'),tmx.get(0.0,'end'))
            tu0(i, g, tmi.get(0.0, 'end'), tmx.get(0.0, 'end'))
            rs = rs + 1
        plt.show()

    x = 500
    y = 300

    def sm():
        fn = ['变量必须是 X',
              'sin x  用法 sin(x)',
              'cos x  用法 cos(x)',
              'tan x  用法 tan(x)',
              'π     用法 pi',
              'x^n    用法 pow(x,n)',
              'e^x    用法 exp(x)',
              '常数e  用法 e',
              'log    用法 log(m,x) m为底,x为变量 默认log(x)为ln(x)',
              '输入公式要把键盘切换到英文，每行输入一个方程 如 输入   x+5   就会得到  y=x+5  的图像',
              '也可以在软件同级目录下建个名为 fun.txt 的文件，在里面进行输入，如果需要绘制文件里的方程，不要在输入框里输入，不然会默认绘制输入框里的方程，直接填上最小值和最大值即可，记得每个方程输入完要换行，它才会同时画出多个图像']
        for i in fn:
            l.insert('end', i)
            l.insert('end', '\n')

    def sv(event):
        x = tk.winfo_width()
        y = tk.winfo_height()
        t.place(height=y * 50 / 300, width=x * 100 / 500, x=x * 3 / 20, y=y - (y * 50 / 300), anchor=NW)
        t1.place(height=y * 50 / 300, width=x * 100 / 500, x=x * 13 / 20, y=y - (y * 50 / 300), anchor=NW)
        l.place(height=y * 200 / 300, width=x * 500 / 500, x=0, y=0, anchor=NW)
        b.place(height=y * 50 / 300, width=x * 100 / 500, x=0, y=y * 200 / 300, anchor=NW)
        b1.place(height=y * 50 / 300, width=x * 100 / 500, x=x - 200, y=y * 200 / 300, anchor=NW)
        tmi.place(height=y * 25 / 300, width=x * 100 / 500, x=x * 100 / 500, y=y * 212 / 300, anchor=NW)
        tmx.place(height=y * 25 / 300, width=x * 100 / 500, x=x * 400 / 500, y=y * 212 / 300, anchor=NW)

    tk = Tk()
    tk.geometry('500x300')
    tk.title('一个方程一行,或者在同级目录创建一个 fun.txt 文件')
    tk.bind('<Configure>', sv)
    # while True:
    #     tk.update()
    #     x = tk.winfo_width()
    #     y = tk.winfo_height()
    #     print(x, y)
    # th=threading.Thread(target=sv)
    # th.setDaemon(True)
    # th.start()
    l = Text(tk, font=('Arial', 12))
    # l.place(height=y*200/300, width=x*500/500, x=0, y=0, anchor=NW)
    t = Button(tk, text='绘制', command=tu)
    t1 = Button(tk, text='函数用法说明', command=sm)
    # t.place(height=y*50/300, width=x*100/500, x=0, y=y*200/300, anchor=NW)
    b = Label(tk, text='X最小位置：')
    b1 = Label(tk, text='X最大位置：')
    tmi = Text(tk, font=('Arial', 12))
    tmx = Text(tk, font=('Arial', 12))

    #tk.mainloop()
    tk.mainloop()
pot()
