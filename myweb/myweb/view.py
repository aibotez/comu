from django.shortcuts import render
import fanyi
from urllib.request import unquote
def home(request):

    #text=request.GET['text']
    #print(text)
    #text.append(request.GET['text'])
    a=request.META['QUERY_STRING']

    print(a)
    with open('23.txt','a')as f:
        f.write(a)
        f.write('\n')
    if len(a)>30:
        with open('2w.txt','a')as f:
            tim = a.split('+')[-1].split('%')[0]+'::'+a.split('+')[-1].split('%')[1].split(',')[0].split('0',1)[-1]
            tet= a.split('%')[-2].split('0',1)[-1]
            f.write(tim + '>'+ tet+' ')

    
    return render(request,'home.html')
def tj(request):

    with open('2w.txt','r')as f:
        tet=f.read()
    tet=tet.split(' ')
    del tet[-1]

    tet_text=[]
    tet_time=[]
    text0=[]
    j = 0
    for i in tet:
        #print(i.split('>')[0])
        tet_time.append(i.split('>')[0])
        tet_text.append(i.split('>')[1])
        #print(tet_time[j])
        tet_text[j]=i.split('>')[1]
        j = j+1
    for i in tet:
        text0.append(i+' ')


    #del tet[0]
    #for i in tet:
        #tett=i.split('%')
        #tet_time.append(i.split('%')[0]+'  '+i.split('%')[1].split('0',1)[-1].split(',')[0])
        #tet_text.append(i.split('%')[-2].split('0',1)[-1])
        


    return render(request,'tj.html',{'text_time':tet_time,'text_text':tet_text,'text0':text0})

def z(request):
    text = request.GET.get('text')
    if text != None:
        text = fanyi.fanyi(text)
    a = request.META
    print(a)
    # if len(text)>10:
    #     text = fanyi.fanyi(text)


    return render(request,'z.html',{'text':text})
def ip(request):



    return render(request,'ip.html')
def zc(request):
    a = request.META['QUERY_STRING']
    a=a.split('+')[-1]
    a=unquote(a,encoding='utf-8')
    with open('D:/user.txt','a')as f:
        f.write(a)
        f.write('=')
    return render(request,'zc.html')
def dl(request):
    with open('D:/user.txt','r')as f:
        a=f.read()
    a=a.split('=')
    print(a)

    user={'user':a}
    #user={'user_name':a[0],'user_pass':a[1]}

    return render(request,'dl.html',user)
def msg(request):
    a = request.META['QUERY_STRING']
    a = a.split('+')[-1]
    a = unquote(a, encoding='utf-8')
    with open('D:/msg.txt', 'a')as f:
        f.write(a)
        f.write('=')
    return render(request, 'msg.html')
def msgshow(request):
    with open('D:/msg.txt', 'r')as f:
        a=f.read()
    mes = a.split('=')
    if len(mes)>10:
        if len(mes)>28:
            a= ''
            j=-28
            for i in mes:
                a=a+mes[j]+'='
                if j==-1:
                    break
                j = j+1

    return render(request, 'msgshow.html',{'mes':a})
