from tkinter import *
import time
from math import *
#import matplotlib.pyplot as plt
import numpy as np
import os
import threading
import requests
#from translat import tan
from lxml import etree
import hashlib
import urllib.request
import json
import threading
import random
import sys
import pyperclip
url_zc = 'http://23752ht167.wicp.vip/zc/?text=+'
url_dl='http://23752ht167.wicp.vip/dl/'
url_msg='http://23752ht167.wicp.vip/msg/?text=+'
url_msgshow='http://23752ht167.wicp.vip/msgshow/'

#url_zc='http://192.168.1.6:8000/zc/?text=+'
#url_dl='http://192.168.1.6:8000/dl/'
#url_msg='http://192.168.1.6:8000/msg/?text=+'
#url_msgshow='http://192.168.1.6:8000/msgshow/'
checkk={'p':'1','name':'n'}
user_list=[]
def denglu():
    check='1'
    deng=Tk()
    deng.geometry('560x450')
    vn=StringVar()
    vp = StringVar()

    ume=Entry(deng,textvariable=vn)
    ume.place(x=230,y=110,anchor=NW)
    ump=Entry(deng,show='*',textvariable=vp)
    ump.place(x=230,y=210,anchor=NW)



    try:
        with open(r'D:/userr.txt', 'r')as f:
           us = f.read()
    except:
        with open(r'D:/userr.txt', 'w+')as f:
            us=' '


    if len(us)>1:
        ume.insert(END, us.split('>')[0])
        ump.insert(END, us.split('>')[1])
        #user_name=us.split('>')[0]
        #user_pass=us.split('>')[1]

    s = Label(deng, text='用户名',font=('Arial',15)).place(x=150, y=105,anchor=NW)
    s = Label(deng, text='密码', font=('Arial', 15)).place(x=160, y=200, anchor=NW)
    def send():
        umee = ume.get()
        umpp = ump.get()
        try:
            res=requests.get(url_dl)
        except:
            s = Label(deng, text='服务器连接失败', font=('Arial', 15), bg='red').place(x=260, y=55, anchor=NW)
        res=res.text
        res=etree.HTML(res)
        res=res.xpath('//trn/text()')[0]
        user=[]
        res=res.split('-')
        for i in res:
            rs=i.replace('\n',"").split(' ')[0]
            user.append(rs)
        del user[-1]
        del user[-1]
        for i in user:
            user_list.append(i.split('>')[0])
        for i in user:
            if umee in i.split('>')[0] and umpp in i.split('>')[-1]:
                with open(r'D:/userr.txt', 'w')as f:
                    f.write(umee + '>' + umpp)
                checkk['p']='0'
                checkk['name']=umee
                tong()
                deng.destroy()
        if checkk['p']=='1':
            s = Label(deng, text='登陆失败', font=('Arial', 15), bg='red').place(x=260, y=55, anchor=NW)
        checkk['name']=umee
        

  
            #user.append(ur.split(' ')[0])

    def zc():



        zcc=Toplevel()
        zcc.geometry('560x450')
        vn = StringVar()
        vp = StringVar()

        ume = Entry(zcc, textvariable=vn)
        ume.place(x=230, y=110, anchor=NW)
        ump = Entry(zcc, show='*', textvariable=vp)
        ump.place(x=230, y=210, anchor=NW)
        s = Label(zcc, text='用户名', font=('Arial', 15)).place(x=150, y=105, anchor=NW)
        s = Label(zcc, text='密码', font=('Arial', 15)).place(x=160, y=200, anchor=NW)
        def wc():
            
            global user_list
            try:
                res=requests.get(url_dl)
            except:
                s = Label(zcc, text='服务器连接失败', font=('Arial', 15), bg='red').place(x=260, y=55, anchor=NW)

            res=res.text
            res=etree.HTML(res)
            res=res.xpath('//trn/text()')[0]
            user=[]
            res=res.split('-')
            for i in res:
                rs=i.replace('\n',"").split(' ')[0]
                user.append(rs)
            del user[-1]
            del user[-1]
            for i in user:
                user_list.append(i.split('>')[0])
            
            umee=ume.get()
            umpp=ump.get()
            s = Label(zcc, text='', font=('Arial', 15)).place(x=260, y=55, anchor=NW)
            if umee in user_list:
                s = Label(zcc, text='用户名已被注册', font=('Arial', 15),bg='red').place(x=260, y=55, anchor=NW)
            else:
                url_zcc=url_zc+umee+'>'+umpp
                try:
                    res=requests.get(url_zcc)
                except:
                    s = Label(zcc, text='服务器连接失败', font=('Arial', 15), bg='red').place(x=260, y=55, anchor=NW)
                #res=requests.get(url_zcc)
                res=str(res)
                if res=='<Response [200]>':
                    
                    s = Label(zcc, text='注册成功', font=('Arial', 15),bg='red').place(x=260, y=55, anchor=NW)
                    with open(r'D:/userr.txt', 'w')as f:
                        
                        f.write(umee + '>' + umpp)
                
            user_list=[]


        a = Button(zcc, text='注册', command=wc).place(x=160, y=300, anchor=NW)


    a=Button(deng,text='登陆',command=send).place(x=160, y=300,anchor=NW)
    a = Button(deng, text='注册', command=zc).place(x=400, y=300, anchor=NW)
    return checkk




def tong():
    global user_list
    ton=Toplevel()
    ton.geometry('755x602+0+0')
    s=user_list
    self=''
    j=0
    for i in s:
        if i ==checkk['name']:
            print(self)
            self='<--'
        s=Label(ton,text=i+self,font=('Arial',20)).place(width=191,height=60,x=0,y=j,anchor=NW)
        j=j+60
        self=''
    user_list=[]
    #s=Label(ton,text='22',bg='green',font=('Arial',20)).place(width=191,height=61,x=0,y=60,anchor=NW)
    l = Text(ton,font=('Arial',12))
    l.place(height=495,width=562,x=754,y=0,anchor=NE)
    e=Entry(ton)
    e.place(width=500,x=192,y=495,anchor=NW)




    
    def ca():
        msg=[]
        res= requests.get(url_msg+checkk['name']+'：'+e.get())
        res=requests.get(url_msgshow)
        e.delete(0,END)
        res=res.text
        res=etree.HTML(res)
        res_m=res.xpath('//trn/text()')[0]
        res_m=res_m.split('=')
        for i in res_m:
            msg.append(i.replace('\n',""))
        del msg[-1]
        l.delete('1.0','end')
        print(e.get())
        for i in msg:
            l.insert('end',i)
            l.insert('end','\n')

    def sx():
        msg=[]
        res=requests.get(url_msgshow)
        #e.delete(0,END)
        res=res.text
        res=etree.HTML(res)
        res_m=res.xpath('//trn/text()')[0]
        res_m=res_m.split('=')
        for i in res_m:
            msg.append(i.replace('\n',""))
        del msg[-1]
        l.delete('1.0','end')
        for i in msg:
            l.insert('end',i)
            l.insert('end','\n')
    def a():
        while True:
            sx()
            time.sleep(3)


        #l.after(1000,a)
    th=threading.Thread(target=a)
    th.setDaemon(True)
    th.start() 
    #l.after(1000,a)
    #ton.after(3,sx)
    sx()



    a= Button(ton,text='send',width=10,command=ca).place(x=754,y=495,anchor=NE)







def tan():
    p=0
    def trans(q):
        if sys.getsizeof(q[0]) > 60:
            fromLang = 'zh'
            toLang = 'en'
        else:
            fromLang = 'en'
            toLang = 'zh'
        appid = '20190330000282694'
        key = 'rIdsByrSbAA4P1fBVDLL'
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + key
        m1 = hashlib.md5()
        m1.update(sign.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        myurl = url + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        response = urllib.request.urlopen(myurl).read().decode('utf8')
        getJson = json.loads(response)
        getInfo = getJson['trans_result']
        s = getInfo[0]
        re = s['dst']
        return re
    def run():
        text0=''
        txt.insert('0.0', 'xc')
        while True:
            text = pyperclip.paste()
            if text != text0:
                txt.delete('1.0','end')
                txt.insert('0.0','翻译中')
                txt.delete('1.0','end')
                text0 = text
                ft=trans(text)
                txt.insert('0.0',ft)
            time.sleep(2)
    #th = threading.Thread(target=run)
    #th.setDaemon(True)

    tr=Toplevel()
    tr.title('翻译')
    tr.geometry('726x500')
    #print(tr.bind('<Configure>'))
    txt = Text(tr)
    txt.place(height=300, width=726, x=0, y=0, anchor=NW)
    inp = Text(tr, font=('Arial', 12))
    inp.place(height=200, width=600, x=0, y=300, anchor=NW)
    # bt = Button(tr, text='监听黏贴并置顶', command=jt).place(height=66, width=126, x=600, y=432, anchor=NW)
    # jt = Button(tr, text='翻译', command=tx).place(height=66, width=126, x=600, y=300, anchor=NW)
    # jtb = Button(tr, text='关闭监听和置顶', command=jtb).place(height=66, width=126, x=600, y=366, anchor=NW)

    def tx():
        tt = inp.get(0.0, 'end')
        txt.delete('1.0', 'end')
        txt.insert(0.0,trans(tt))
        #tt.delete('1.0', 'end')

    def jtxc():
        tr.wm_attributes('-topmost',1)
        th = threading.Thread(target=run)
        th.setDaemon(True)
        th.start()


    def jtb():
        p=1
        tr.wm_attributes('-topmost',0)


    # def jianting():
    #     text0 = ''
    #     while True:
    #         text = pyperclip.paste()
    #         if text != text0:
    #
    #             text0 = text
    #             ft = trans(text)
    #             txt.insert('0.0',ft)
    #         time.sleep(2)


    #Label(ton, text=i + self, font=('Arial', 20)).place(width=191, height=60, x=0, y=j, anchor=NW)
    # txt=Text(tr)
    # txt.place(height=300,width=726,x=0,y=0,anchor=NW)
    # inp=Text(tr,font=('Arial',12))
    # inp.place(height=200,width=600,x=0,y=300,anchor=NW)
    bt=Button(tr,text='监听黏贴并置顶',command=jtxc).place(height=66,width=126,x=600,y=432,anchor=NW)
    jt = Button(tr, text='翻译', command=tx).place(height=66, width=126, x=600, y=300, anchor=NW)
    jtb = Button(tr, text='关闭监听和置顶', command=jtb).place(height=66, width=126, x=600, y=366, anchor=NW)
    #tr.mainloop()


def pot():
    import matplotlib.pyplot as plt
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

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
            plt.plot(i, yn[j], '-', color=g,label='y = '+a)
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



zhu = Tk()
zhu.geometry('260x300')
t=Button(zhu,text='通讯',command=denglu).place(height=50, width=80,x=0,y=60)
fan=Button(zhu,text='翻译',command=tan).place(height=50, width=80,x=180,y=60)
plt=Button(zhu,text='函数图像',command=pot).place(height=50, width=80,x=0,y=180)
#tt=threading.Thread(target=a)
#tt.setDaemon(True)


zhu.mainloop()




