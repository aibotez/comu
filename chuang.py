from tkinter import *
import time
import os
import threading
import requests
from lxml import etree
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
    ton.after(3,sx)
    sx()



    a= Button(ton,text='send',width=10,command=ca).place(x=754,y=495,anchor=NE)



#dl=denglu()
zhu = Tk()
zhu.geometry('180x200+600+100')
t=Button(zhu,text='tongxun',command=denglu).place(x=40,y=100)


#tt=threading.Thread(target=a)
#tt.setDaemon(True)



zhu.mainloop()




